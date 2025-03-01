from abc import ABC, abstractmethod
import time
import matplotlib.pyplot as plt
import random
from typing import TypeVar, Generic, Optional, List, Any

T = TypeVar('T') 

class DisjointSetsInterface(Generic[T], ABC):
    @abstractmethod
    def find(self, i: T) -> T:
        pass
    
    @abstractmethod
    def union(self, i: T, j: T) -> None:
        pass

class DisjointSets(Generic[T], DisjointSetsInterface[T]):
    def __init__(self, num: int):
        #makeset
        self.parents = [i for i in range(0, num)]
        self.rank = [0 for _ in range(0, num)]
    
    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i
    
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1

class DisjointSets2():
    def __init__(self, num: int):
        #makeset
        self.parents = [i for i in range(0, num)]
    
    def find(self, i):
        # Path compression remains the same
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        
        self.parents[i_id] = j_id

if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000]
    times = []
    times2 = []
    for size in sizes:
        start = time.time()
        ds = DisjointSets(size)
        for i in range(0, size - 1):
            ds.union(random.randint(0, size - 1), random.randint(0, size - 1))
        end = time.time()
        times.append(end - start)

        start = time.time()
        ds2 = DisjointSets2(size)
        for i in range(0, size - 1):
            ds2.union(random.randint(0, size - 1), random.randint(0, size - 1))
        end = time.time()
        times2.append(end - start)
    
    plt.plot(sizes, times2, marker='o', linestyle='-', label="Union-Find with Path Compression")
    plt.plot(sizes, times, marker='o', linestyle='-', label="Union-Find with Rank")
    plt.xscale("log")
    plt.yscale("log") 
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.xlabel("Size (n)")
    plt.ylabel("Total Time (s)")
    plt.legend()
    plt.show()
    