from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self, max_size: int = 100):
        self._max_size: int = max_size
        self._items: list[Optional[T]] = [None] * max_size
        self._front: int = 0
        self._rear: int = -1
        self._current_size: int = 0
    
    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        # Circular increment of rear
        self._rear = (self._rear + 1) % self._max_size
        self._items[self._rear] = item
        self._current_size += 1
    
    def dequeue(self) -> Optional[T]:
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self._items[self._front]
        self._items[self._front] = None
        # Circular increment of front
        self._front = (self._front + 1) % self._max_size
        self._current_size -= 1
        return item
    
    def peek(self) -> Optional[T]:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._items[self._front]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._current_size == 0
    
    def is_full(self) -> bool:
        """Check if the queue is full."""
        return self._current_size == self._max_size
    
    def size(self) -> int:
        """Return the current number of items in the queue."""
        return self._current_size
    
    def clear(self) -> None:
        """Clear all items from the queue."""
        self._items = [None] * self._max_size
        self._front = 0
        self._rear = -1
        self._current_size = 0
    
    def print_queue(self) -> None:
        """Print the queue elements from front to rear."""
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        for i in range(self._current_size):
            index = (self._front + i) % self._max_size
            elements.append(str(self._items[index]))
        
        print(f"Queue (front to rear): [{', '.join(elements)}]")
