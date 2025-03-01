from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None

class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
    
    def push_back(self, elem: T) -> None:
        """Add an element to the end of the list."""
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def push_front(self, elem: T) -> None:
        """Add an element to the front of the list."""
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def pop_front(self) -> Optional[T]:
        """Remove and return the first element."""
        if not self.head:
            raise IndexError("List is empty")
        
        elem = self.head.data
        self.head = self.head.next
        
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        
        return elem
    
    def pop_back(self) -> Optional[T]:
        """Remove and return the last element."""
        if not self.tail:
            raise IndexError("List is empty")
        
        elem = self.tail.data
        self.tail = self.tail.prev
        
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        
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
        current = self.head
        while current:
            if current.data == elem:
                # Adjust head or tail if needed
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    # Link previous and next nodes
                    current.prev.next = current.next
                    current.next.prev = current.prev
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
        self.tail = None
