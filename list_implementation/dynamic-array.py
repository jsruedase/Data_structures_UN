from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class DynamicArray(Generic[T]):
    def __init__(self, initial_capacity: int = 10):
        self._capacity: int = initial_capacity
        self._size: int = 0
        self._array: list[Optional[T]] = [None] * initial_capacity
    
    def _resize(self, new_capacity: int) -> None:
        """Resize the internal array to a new capacity."""
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
    
    def push_back(self, elem: T) -> None:
        """Add an element to the end of the array."""
        if self._size == self._capacity:
            # Double the capacity when full
            self._resize(self._capacity * 2)
        
        self._array[self._size] = elem
        self._size += 1
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element."""
        if self._size == 0:
            raise IndexError("Array is empty")
        
        self._size -= 1
        elem = self._array[self._size]
        self._array[self._size] = None
        
        # Shrink if size is less than 1/4 of capacity
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return elem
    
    def __getitem__(self, index: int) -> T:
        """Get element at a specific index."""
        if 0 <= index < self._size:
            return self._array[index]
        raise IndexError("Index out of bounds")
    
    def __setitem__(self, index: int, value: T) -> None:
        """Set element at a specific index."""
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of bounds")
    
    def insert(self, index: int, elem: T) -> None:
        """Insert an element at a specific index."""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        
        # Resize if full
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i-1]
        
        self._array[index] = elem
        self._size += 1
    
    def remove(self, index: int) -> Optional[T]:
        """Remove element at a specific index."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        
        elem = self._array[index]
        
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i+1]
        
        self._size -= 1
        self._array[self._size] = None
        
        # Shrink if size is less than 1/4 of capacity
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return elem
    
    def clear(self) -> None:
        """Clear the array."""
        self._array = [None] * self._capacity
        self._size = 0
    
    def is_empty(self) -> bool:
        """Check if the array is empty."""
        return self._size == 0
    
    def size(self) -> int:
        """Get the current size of the array."""
        return self._size
    
    def capacity(self) -> int:
        """Get the current capacity of the array."""
        return self._capacity
    
    def print_array(self) -> None:
        """Print the array elements."""
        elements = [str(self._array[i]) for i in range(self._size)]
        print(f"Array elements: [{', '.join(elements)}]")
