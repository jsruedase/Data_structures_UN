from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class CircularArrayList(Generic[T]):
    def __init__(self, size: int):
        self.size: int = size
        self.array: list[Optional[T]] = [None] * size
        self.front: int = 0
        self.rear: int = -1
        self.current_size: int = 0
    
    def push_back(self, elem: T) -> None:
        """Add an element to the end of the list."""
        if self.is_full():
            raise OverflowError("List is full")
        
        self.rear = (self.rear + 1) % self.size
        self.array[self.rear] = elem
        self.current_size += 1
    
    def push_front(self, elem: T) -> None:
        """Add an element to the front of the list."""
        if self.is_full():
            raise OverflowError("List is full")
        
        self.front = (self.front - 1 + self.size) % self.size
        self.array[self.front] = elem
        self.current_size += 1
    
    def pop_front(self) -> Optional[T]:
        """Remove and return the first element."""
        if self.is_empty():
            raise IndexError("List is empty")
        
        elem = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.size
        self.current_size -= 1
        return elem
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element."""
        if self.is_empty():
            raise IndexError("List is empty")
        
        elem = self.array[self.rear]
        self.array[self.rear] = None
        self.rear = (self.rear - 1 + self.size) % self.size
        self.current_size -= 1
        return elem
    
    def find(self, elem: T) -> int:
        """Find the index of an element."""
        for i in range(self.current_size):
            index = (self.front + i) % self.size
            if self.array[index] == elem:
                return i
        return -1
    
    def print_list(self) -> None:
        """Print the list elements."""
        elements = []
        for i in range(self.current_size):
            index = (self.front + i) % self.size
            elements.append(str(self.array[index]))
        print(f"List elements: [{', '.join(elements)}]")
    
    def is_empty(self)