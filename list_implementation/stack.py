from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, max_size: int = 100):
        self._max_size: int = max_size
        self._items: list[Optional[T]] = [None] * max_size
        self._top: int = -1
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        if self.is_full():
            raise OverflowError("Stack is full")
        
        self._top += 1
        self._items[self._top] = item
    
    def pop(self) -> Optional[T]:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        item = self._items[self._top]
        self._items[self._top] = None
        self._top -= 1
        return item
    
    def peek(self) -> Optional[T]:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self._items[self._top]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self._top == -1
    
    def is_full(self) -> bool:
        """Check if the stack is full."""
        return self._top == self._max_size - 1
    
    def size(self) -> int:
        """Return the current number of items in the stack."""
        return self._top + 1
    
    def clear(self) -> None:
        """Clear all items from the stack."""
        self._items = [None] * self._max_size
        self._top = -1
    
    def print_stack(self) -> None:
        """Print the stack elements from bottom to top."""
        if self.is_empty():
            print("Stack is empty")
            return
        
        elements = [str(self._items[i]) for i in range(self._top + 1)]
        print(f"Stack (bottom to top): [{', '.join(elements)}]")
