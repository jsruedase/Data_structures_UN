import random
from typing import Any, List, Optional, Tuple, TypeVar, Generic, Protocol
from abc import ABC, abstractmethod
import time
import matplotlib.pyplot as plt
K = TypeVar('K', int, str)

class HashMap(Protocol, Generic[K]):
    @abstractmethod
    def put(self, key: K, value: Any) -> None:
        """Insert or update a key-value pair in the hash map."""
        pass
    
    @abstractmethod
    def get(self, key: K) -> Optional[Any]:
        """Retrieve a value by key."""
        pass
    
    @abstractmethod
    def remove(self, key: K) -> bool:
        """Remove a key-value pair by key."""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Get the current size of the hash map."""
        pass


class FixedSizeHashMap(Generic[K]):
    def __init__(self, m: int):
        self.m = m
        self.buckets: List[List[Tuple[K, Any]]] = [[] for _ in range(m)]
        self._count = 0
        
        # For integer hashing (ax + b) mod p mod m
        self.p = self._find_prime_larger_than(m * 100)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        
        # For string hashing (polynomial hash)
        self.x = random.randint(1, self.p - 1)
    
    def _find_prime_larger_than(self, n: int) -> int:
        """Find a prime number larger than n."""
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        while not is_prime(n):
            n += 1
        return n
    
    def _hash_int(self, key: int) -> int:
        return ((self.a * key + self.b) % self.p) % self.m
    
    def _hash_str(self, key: str) -> int:
        hash_value = 0
        for char in key:
            hash_value = (hash_value * self.x + ord(char)) % self.p
        return hash_value % self.m
    
    def _hash(self, key: K) -> int:
        if isinstance(key, int):
            return self._hash_int(key)
        elif isinstance(key, str):
            return self._hash_str(key)
        else:
            raise TypeError("Key must be an integer or string")
    
    def put(self, key: K, value: Any) -> None:
        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update value
                return
        
        # Key not found, append new key-value pair
        bucket.append((key, value))
        self._count += 1
    
    def get(self, key: K) -> Optional[Any]:
        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def remove(self, key: K) -> bool:
        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._count -= 1
                return True
        
        return False
    
    def size(self) -> int:
        return self._count


class ResizableHashMap(Generic[K]):
    def __init__(self, initial_size: int = 16, load_factor_threshold: float = 0.75):
        self.load_factor_threshold = load_factor_threshold
        self.count = 0
        self.capacity = initial_size
        self.map = FixedSizeHashMap[K](initial_size)
    
    def put(self, key: K, value: Any) -> None:
        # Check if key already exists
        old_value = self.map.get(key)
        if old_value is not None:
            self.map.put(key, value)
            return
        
        # New key, check load factor
        current_load_factor = (self.count + 1) / self.capacity
        if current_load_factor > self.load_factor_threshold:
            self._resize()
        
        self.map.put(key, value)
        self.count += 1
    
    def _resize(self) -> None:
        old_map = self.map
        new_capacity = self.capacity * 2
        new_map = FixedSizeHashMap[K](new_capacity)
        
        # Rehash all entries
        for bucket in old_map.buckets:
            for key, value in bucket:
                new_map.put(key, value)
        
        self.map = new_map
        self.capacity = new_capacity
    
    def get(self, key: K) -> Optional[Any]:
        return self.map.get(key)
    
    def remove(self, key: K) -> bool:
        if self.map.remove(key):
            self.count -= 1
            return True
        return False
    
    def size(self) -> int:
        return self.count

""" 
if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000]
    trials = 5
    times = []
    times2 = []
    
    for size in sizes:
        fhm_times = []
        rhm_times = []
        
        for _ in range(trials):
            random.seed(42)  # Ensure the same random values for both hash maps
            
            # FixedSizeHashMap timing
            start = time.time()
            fhm = FixedSizeHashMap(size)
            for i in range(size):
                fhm.put(random.randint(0, size - 1), random.randint(0, size - 1))
            end = time.time()
            fhm_times.append(end - start)
            
            random.seed(42)  
            # ResizableHashMap timing
            start = time.time()
            rhm = ResizableHashMap()
            for i in range(size):
                rhm.put(random.randint(0, size - 1), random.randint(0, size - 1))
            end = time.time()
            rhm_times.append(end - start)
        
        times.append(sum(fhm_times) / trials)
        times2.append(sum(rhm_times) / trials)
    
    plt.plot(sizes, times2, marker='o', linestyle='-', label="Resizable Hash Map")
    plt.plot(sizes, times, marker='o', linestyle='-', label="Fixed Size Hash Map")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.xlabel("Size (n), Load Factor = 0.75")
    plt.ylabel("Total Time (s)")
    plt.legend()
    plt.show()
"""
"""
if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000]
    trials = 1
    load_factors = [0.1, 0.25, 0.5, 0.75, 0.9, 1.2, 1.5]
    times = {lf: [] for lf in load_factors}

    for size in sizes:
        rhm_times = {lf: [] for lf in load_factors}

        for _ in range(trials):
            for lf in load_factors:
                random.seed(42)  # Reset the seed for consistent values

                # ResizableHashMap timing
                start = time.time()
                rhm = ResizableHashMap(load_factor_threshold=lf)
                for i in range(size):
                    rhm.put(random.randint(0, size - 1), random.randint(0, size - 1))
                end = time.time()
                rhm_times[lf].append(end - start)

        for lf in load_factors:
            times[lf].append(sum(rhm_times[lf]) / trials)

    for lf in load_factors:
        plt.plot(sizes, times[lf], marker='o', linestyle='-', label=f"Resizable Hash Map (Load Factor = {lf})")
    
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.xlabel("Size (n)")
    plt.ylabel("Total Time (s)")
    plt.legend()
    plt.show()
"""
if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000]
    trials = 1
    initial_sizes = [0.5, 0.75, 1.0, 1.5]  # Multipliers for the initial size
    times = {isize: [] for isize in initial_sizes}

    for size in sizes:
        fhm_times = {isize: [] for isize in initial_sizes}

        for _ in range(trials):
            random.seed(42)  # Ensure the same random values for all hash maps

            for isize in initial_sizes:
                m = int(size * isize)
                start = time.time()
                fhm = FixedSizeHashMap(m)
                for i in range(size):
                    fhm.put(random.randint(0, size - 1), random.randint(0, size - 1))
                end = time.time()
                fhm_times[isize].append(end - start)

        for isize in initial_sizes:
            times[isize].append(sum(fhm_times[isize]) / trials)

    for isize in initial_sizes:
        plt.plot(sizes, times[isize], marker='o', linestyle='-', label=f"Fixed Size Hash Map (m = {isize} * size)")
    
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.xlabel("Size (n)")
    plt.ylabel("Total Time (s)")
    plt.legend()
    plt.show()
