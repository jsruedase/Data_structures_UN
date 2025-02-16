from typing import TypeVar, Generic, Optional, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class HeapInterface(Generic[T], ABC):
    @abstractmethod
    def insert(self, elem: T) -> None:
        pass
    
    @abstractmethod
    def extract_max(self) -> Optional[T]:
        pass

class Heap(HeapInterface[T]):
    def __init__(self, max_size: int) -> None:
        self.max_size: int = max_size
        self.last_index: int = -1
        self.array: List[Optional[T]] = [None] * max_size
    
    def _sift_up(self, index: int) -> None:
        if index == 0:
            return
            
        parent: int = (index - 1) // 2
        if self.array[parent] < self.array[index]: 
            self.array[parent], self.array[index] = self.array[index], self.array[parent]
            self._sift_up(parent)
        
    def _sift_down(self, index: int) -> None:
        largest: int = index
        left: int = 2 * index + 1
        right: int = 2 * index + 2
        
        if left <= self.last_index and self.array[left] > self.array[largest]:  
            largest = left
            
        if right <= self.last_index and self.array[right] > self.array[largest]: 
            largest = right
            
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self._sift_down(largest)
            
    def insert(self, elem: T) -> None:
        if self.last_index + 1 >= self.max_size:
            raise Exception("Heap is full")
            
        self.last_index += 1
        self.array[self.last_index] = elem
        self._sift_up(self.last_index)
        
    def extract_max(self) -> Optional[T]:
        if self.last_index == -1:
            return None
            
        max_val = self.array[0]
        self.array[0] = self.array[self.last_index]
        self.array[self.last_index] = None
        self.last_index -= 1
        
        if self.last_index > 0:
            self._sift_down(0)
            
        return max_val
    
    def heap_sort(self, arr: List[T]) -> List[T]:
        def sift_down(index: int, size: int) -> None:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            # Check if left child exists and is larger than root
            if left < size and arr[left] > arr[largest]:  # type: ignore
                largest = left
                
            # Check if right child exists and is larger than largest so far
            if right < size and arr[right] > arr[largest]:  # type: ignore
                largest = right
                
            # If largest is not root
            if largest != index:
                arr[index], arr[largest] = arr[largest], arr[index]
                sift_down(largest, size)
        
        # Heapify: build max heap
        n = len(arr)
        first_parent = (n - 1) // 2
        for i in range(first_parent, -1, -1):
            sift_down(i, n)
        
        # Sorting phase
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            sift_down(0, i) 
        
        return arr
    
    def print(self) -> None:
        print([x for x in self.array[:self.last_index + 1]])

if __name__ == "__main__":
    h = Heap[int](10)
    for x in [4, 8, 2, 9, 1, 7]:
        h.insert(x)
    h.print()  # Should print in max-heap order
    while h.last_index >= 0:
        print(h.extract_max())  # Should print in descending order