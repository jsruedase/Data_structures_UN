from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[Node[T]] = None

class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
    
    def push_back(self, elem: T) -> None:
        """Add an element to the end of the list."""
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def push_front(self, elem: T) -> None:
        """Add an element to the front of the list."""
        new_node = Node(elem)
        new_node.next = self.head
        self.head = new_node
    
    def pop_front(self) -> Optional[T]:
        """Remove and return the first element."""
        if not self.head:
            raise IndexError("List is empty")
        
        elem = self.head.data
        self.head = self.head.next
        return elem
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element."""
        if not self.head:
            raise IndexError("List is empty")
        
        if not self.head.next:
            elem = self.head.data
            self.head = None
            return elem
        
        current = self.head
        while current.next.next:
            current = current.next
        
        elem = current.next.data
        current.next = None
        return elem
    
    def find(self, elem: T) -> int:
        """Find the index of an element."""
        current = self.head
        index = 0
        while current:
            if current.data == elem:
                return index
            current = current.next
            index += 1
        return -1
    
    def erase(self, elem: T) -> None:
        """Remove first occurrence of an element."""
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == elem:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == elem:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError("Element not found")
    
    def print_list(self) -> None:
        """Print the list elements."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"List elements: [{', '.join(elements)}]")
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def clear(self) -> None:
        """Clear the list."""
        self.head = None
