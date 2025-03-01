import typing
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Lista(Generic[T]):
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.last_element_index: int = -1
        self.array: list[Optional[T]] = [None] * size
    
    def push_back(self, elem: T) -> None:
        """Add an element to the back of the list."""
        if self.last_element_index >= self.size - 1:
            raise OverflowError("List is full. Cannot add element.")
        
        self.last_element_index += 1
        self.array[self.last_element_index] = elem
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element of the list."""
        if self.last_element_index == -1:
            raise IndexError("List is empty. Cannot remove element.")
        
        elem = self.array[self.last_element_index]
        self.array[self.last_element_index] = None
        self.last_element_index -= 1
        return elem
    
    def print_list(self) -> None:
        """Print the list elements."""
        elements = [str(self.array[i]) for i in range(self.last_element_index + 1)]
        print(f"List elements: [{', '.join(elements)}]")
    
    def push_front(self, elem: T) -> None:
        """Add an element to the front of the list."""
        if self.last_element_index >= self.size - 1:
            raise OverflowError("List is full. Cannot add element.")
        
        # Shift elements right
        for i in range(self.last_element_index, -1, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[0] = elem
        self.last_element_index += 1
    
    def pop_front(self) -> Optional[T]:
        """Remove and return the first element of the list."""
        if self.last_element_index == -1:
            raise IndexError("List is empty. Cannot remove element.")
        
        elem = self.array[0]
        # Shift elements left
        for i in range(self.last_element_index):
            self.array[i] = self.array[i + 1]
        
        self.array[self.last_element_index] = None
        self.last_element_index -= 1
        return elem
    
    def find(self, elem: T) -> int:
        """Find the index of an element in the list."""
        for i in range(self.last_element_index + 1):
            if self.array[i] == elem:
                return i
        return -1

    def erase(self, elem: T) -> None:
        """Remove the first occurrence of an element."""
        index = self.find(elem)
        if index == -1:
            raise ValueError("Element not found in list")
        
        # Shift elements left
        for i in range(index, self.last_element_index):
            self.array[i] = self.array[i + 1]
        
        self.array[self.last_element_index] = None
        self.last_element_index -= 1
    
    def add_before(self, ref_elem: T, insert_elem: T) -> None:
        """Insert an element before a reference element."""
        index = self.find(ref_elem)
        if index == -1:
            raise ValueError("Reference element not found")
        
        if self.last_element_index >= self.size - 1:
            raise OverflowError("List is full. Cannot add element.")
        
        # Shift elements right
        for i in range(self.last_element_index, index - 1, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[index] = insert_elem
        self.last_element_index += 1
    
    def add_after(self, ref_elem: T, insert_elem: T) -> None:
        """Insert an element after a reference element."""
        index = self.find(ref_elem)
        if index == -1:
            raise ValueError("Reference element not found")
        
        if self.last_element_index >= self.size - 1:
            raise OverflowError("List is full. Cannot add element.")
        
        # Shift elements right
        for i in range(self.last_element_index, index, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[index + 1] = insert_elem
        self.last_element_index += 1
    
    def clear(self) -> None:
        """Clear the list."""
        self.array = [None] * self.size
        self.last_element_index = -1
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.last_element_index == -1
    
    def is_full(self) -> bool:
        """Check if the list is full."""
        return self.last_element_index == self.size - 1
