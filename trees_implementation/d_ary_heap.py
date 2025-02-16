from abc import ABC, abstractmethod
import time
import matplotlib.pyplot as plt
import random
from typing import TypeVar, Generic, Optional, List, Any

T = TypeVar('T')

class DAryHeapInterface(Generic[T], ABC):
    @abstractmethod
    def insert(self, elem: T) -> None:
        pass
    
    @abstractmethod
    def extract_max(self) -> Optional[T]:
        pass
    
    @abstractmethod
    def get_max(self) -> Optional[T]:
        pass

class DAryHeap(DAryHeapInterface[T]):
    def __init__(self, max_size: int, d: int) -> None:
        if d < 2:
            raise ValueError("d must be at least 2")
        self.max_size: int = max_size
        self.d: int = d  
        self.last_index: int = -1
        self.array: List[Optional[T]] = [None] * max_size
    
    def _parent(self, index: int) -> int:
        """Get the parent index of a given index."""
        return (index - 1) // self.d
    
    def _first_child(self, index: int) -> int:
        """Get the first child index of a given index."""
        return self.d * index + 1
    
    def _sift_up(self, index: int) -> None:
        if index == 0:
            return
            
        parent = self._parent(index)
        if self.array[parent] < self.array[index]: 
            self.array[parent], self.array[index] = self.array[index], self.array[parent]
            self._sift_up(parent)
        
    def _sift_down(self, index: int) -> None:
        largest = index
        first_child = self._first_child(index)
        
        # Check all d children
        for child in range(first_child, min(first_child + self.d, self.last_index + 1)):
            if self.array[child] > self.array[largest]: 
                largest = child
            
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self._sift_down(largest)
    
    def insert(self, elem: T) -> None:
        """Insert a new element into the heap."""
        if self.last_index + 1 >= self.max_size:
            raise Exception("Heap is full")
            
        self.last_index += 1
        self.array[self.last_index] = elem
        self._sift_up(self.last_index)
        
    def extract_max(self) -> Optional[T]:
        """Remove and return the maximum element."""
        if self.last_index == -1:
            return None
            
        max_val = self.array[0]
        self.array[0] = self.array[self.last_index]
        self.array[self.last_index] = None
        self.last_index -= 1
        
        if self.last_index > 0:
            self._sift_down(0)
            
        return max_val
    
    def get_max(self) -> Optional[T]:
        """Return the maximum element without removing it."""
        if self.last_index == -1:
            return None
        return self.array[0]
    
    def decrease_key(self, index: int, new_value: T) -> None:
        """Decrease the key at the given index."""
        if index < 0 or index > self.last_index:
            raise IndexError("Index out of bounds")
        if self.array[index] < new_value:  # type: ignore
            raise ValueError("New value is larger than current value")
            
        self.array[index] = new_value
        self._sift_down(index)
    
    def increase_key(self, index: int, new_value: T) -> None:
        """Increase the key at the given index."""
        if index < 0 or index > self.last_index:
            raise IndexError("Index out of bounds")
        if self.array[index] > new_value:  # type: ignore
            raise ValueError("New value is smaller than current value")
            
        self.array[index] = new_value
        self._sift_up(index)
    
    def height(self) -> int:
        """Calculate the height of the heap."""
        if self.last_index == -1:
            return 0
        return max(1, (self.last_index + 1).bit_length() // self.d.bit_length())
    
    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return self.last_index == -1
    
    def is_full(self) -> bool:
        """Check if the heap is full."""
        return self.last_index + 1 == self.max_size
    
    def clear(self) -> None:
        """Remove all elements from the heap."""
        self.array = [None] * self.max_size
        self.last_index = -1
    
    def print(self) -> None:
        """Print the heap array up to the last valid index."""
        print([x for x in self.array[:self.last_index + 1]])
    
if __name__ == "__main__":
    sizes = [10**3, 10**4, 10**5, 10**6]
    heaps = []
    for i in range(30,31):
        d_ary_heap_insert_times = []
        d_ary_heap_extract_times = []
        
        for size in sizes:
            h = DAryHeap[int](size, i)
            start = time.time()
            for _ in range(size):
                h.insert(random.randint(0, size))
            end = time.time()
            print(f"Insertion time with d={i} and size={size}: {end-start}")
            d_ary_heap_insert_times.append(end-start)
            
            start = time.time()
            for _ in range(size):
                h.extract_max()
            end = time.time()
            print(f"Extraction time with d={i} and size={size}: {end-start}")
            d_ary_heap_extract_times.append(end-start)
            print()
    
        heaps.append((d_ary_heap_insert_times, d_ary_heap_extract_times))
    

    plt.figure(figsize=(10, 5))

    for i, (insert_times, extract_times) in enumerate(heaps):
        d = i + 2  

        plt.plot(sizes, insert_times, marker="o", linestyle="-", label=f"d={d}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Heap size (n)")
    plt.ylabel("Insertion Time (s)")
    plt.title("Insertion Time vs Heap Size for Different d")
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()


    plt.figure(figsize=(10, 5))

    for i, (insert_times, extract_times) in enumerate(heaps):
        d = i + 2  

        plt.plot(sizes, extract_times, marker="o", linestyle="-", label=f"d={d}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Heap size (n)")
    plt.ylabel("Extraction Time (s)")
    plt.title("Extraction Time vs Heap Size for Different d")
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()
    
    