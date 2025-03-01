from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class CircularDynamicArray(Generic[T]):
    def __init__(self, initial_capacity: int = 10):
        self._capacity: int = initial_capacity
        self._size: int = 0
        self._front: int = 0
        self._array: list[Optional[T]] = [None] * initial_capacity
    
    def _resize(self, new_capacity: int) -> None:
        """Resize the internal array to a new capacity."""
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[(self._front + i) % self._capacity]
        
        self._array = new_array
        self._front = 0
        self._capacity = new_capacity
    
    def push_back(self, elem: T) -> None:
        """Add an element to the end of the array."""
        if self._size == self._capacity:
            # Double the capacity when full
            self._resize(self._capacity * 2)
        
        # Calculate the index to insert
        insert_index = (self._front + self._size) % self._capacity
        self._array[insert_index] = elem
        self._size += 1
    
    def push_front(self, elem: T) -> None:
        """Add an element to the front of the array."""
        if self._size == self._capacity:
            # Double the capacity when full
            self._resize(self._capacity * 2)
        
        # Move front index back (wrapping around)
        self._front = (self._front - 1 + self._capacity) % self._capacity
        self._array[self._front] = elem
        self._size += 1
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element."""
        if self._size == 0:
            raise IndexError("Array is empty")
        
        # Calculate the last element's index
        last_index = (self._front + self._size - 1) % self._capacity
        elem = self._array[last_index]
        self._array[last_index] = None
        self._size -= 1
        
        # Shrink if size is less than 1/4 of capacity
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return elem
    
    def pop_front(self) -> Optional[T]:
        """Remove and return the first element."""
        if self._size == 0:
            raise IndexError("Array is empty")
        
        elem = self._array[self._front]
        self._array[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        # Shrink if size is less than 1/4 of capacity
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return elem
    
    def __getitem__(self, index: int) -> T:
        """Get element at a specific index."""
        if 0 <= index < self._size:
            return self._array[(self._front + index) % self._capacity]
        raise IndexError("Index out of bounds")
    
    def print_array(self) -> None:
        """Print the array elements."""
        elements = []
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            elements.append(str(self._array[index]))
        print(f"Array elements: [{', '.join(elements)}]")
    
    def size(self) -> int:
        """Get the current size of the array."""
        return self._size
    
    def is_empty(self) -> bool:
        """Check if the array is empty."""
        return self._size == 0
