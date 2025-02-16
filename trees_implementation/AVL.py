from abc import ABC, abstractmethod
import time
import matplotlib.pyplot as plt
import random
from typing import TypeVar, Generic, Optional, List, Any

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue: List[T] = []
    
    def enqueue(self, value: T) -> None:
        self.queue.append(value)
    
    def dequeue(self) -> T:
        return self.queue.pop(0)
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0

class TreeNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None
        self.parent: Optional[TreeNode[T]] = None
        self.height: int = 0

class BinarySearchTreeInterface(Generic[T], ABC):
    @abstractmethod
    def height(self, start: Optional[TreeNode[T]]) -> int:
        pass
    
    @abstractmethod
    def size(self, start: Optional[TreeNode[T]]) -> int:
        pass
    
    @abstractmethod
    def inorder(self, start: Optional[TreeNode[T]]) -> None:
        pass
    
    @abstractmethod
    def postorder(self, start: Optional[TreeNode[T]]) -> None:
        pass
    
    @abstractmethod
    def preorder(self, start: Optional[TreeNode[T]]) -> None:
        pass
    
    @abstractmethod
    def leveltraversal(self) -> None:
        pass
    
    @abstractmethod
    def find(self, key: T, start: TreeNode[T]) -> TreeNode[T]:
        pass
    
    @abstractmethod
    def insert(self, value: T) -> None:
        pass
    
    @abstractmethod
    def delete(self, value: T) -> None:
        pass

class AVL(BinarySearchTreeInterface[T]):
    def __init__(self) -> None:
        self.root: Optional[TreeNode[T]] = None
    
    def size(self, start: Optional[TreeNode[T]]) -> int:
        if start is None:
            return 0
        else:
            return 1 + self.size(start.left) + self.size(start.right)
    
    def inorder(self, start: Optional[TreeNode[T]]) -> None:
        if start is None:
            return
        self.inorder(start.left)
        print(start.value, end=" ") 
        self.inorder(start.right)
    
    def postorder(self, start: Optional[TreeNode[T]]) -> None:
        if start is None:
            return
        self.postorder(start.left)
        self.postorder(start.right)
        print(start.value, end=" ")
    
    def preorder(self, start: Optional[TreeNode[T]]) -> None:    
        if start is None:
            return
        print(start.value, end=" ")
        self.preorder(start.left)
        self.preorder(start.right)
    
    def leveltraversal(self) -> None:
        if self.root is None:
            return
        q: Queue[TreeNode[T]] = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            print(node.value)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
    
    def leftdescendant(self, start: TreeNode[T]) -> TreeNode[T]:
        if start.left is None:
            return start
        return self.leftdescendant(start.left)
    
    def rightancestor(self, start: TreeNode[T]) -> Optional[TreeNode[T]]:
        if start.parent is None:
            return None
        if start.value < start.parent.value:
            return start.parent
        return self.rightancestor(start.parent)
    
    def next(self, start: TreeNode[T]) -> Optional[TreeNode[T]]:
        if start.right is not None:
            return self.leftdescendant(start.right)
        return self.rightancestor(start)
    
    def rangesearch(self, x: T, y: T, start: TreeNode[T]) -> List[T]:
        L: List[T] = []
        N = self.find(x, start)
        while N is not None and N.value <= y: 
            if N.value >= x: 
                L.append(N.value)
            N = self.next(N)
        return L
    
    def height(self, start: Optional[TreeNode[T]]) -> int:
        if start is None:
            return 0
        elif start.left is None and start.right is None:
            return 1
        else:
            return start.height
    
    def update_height(self, node: Optional[TreeNode[T]]) -> None:
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def balance_factor(self, node: Optional[TreeNode[T]]) -> int:
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: TreeNode[T]) -> TreeNode[T]:
        if y.left is None:
            return y
            
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update parent pointers
        x.parent = y.parent
        y.parent = x
        if T2 is not None:
            T2.parent = y
            
        # Update root if necessary
        if x.parent is None:
            self.root = x
        else:
            if x.parent.left == y:
                x.parent.left = x
            else:
                x.parent.right = x
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def rotate_left(self, x: TreeNode[T]) -> TreeNode[T]:
        if x.right is None:
            return x
            
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update parent pointers
        y.parent = x.parent
        x.parent = y
        if T2 is not None:
            T2.parent = x
            
        # Update root if necessary
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def rebalance(self, node: Optional[TreeNode[T]]) -> Optional[TreeNode[T]]:
        if node is None:
            return None
            
        self.update_height(node)
        balance = self.balance_factor(node)
        
        # Left Heavy
        if balance > 1 and node.left is not None:
            # Left-Right Case
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
            
        # Right Heavy
        if balance < -1 and node.right is not None:
            # Right-Left Case
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
            
        return node
    
    def find(self, key: T, start: Optional[TreeNode[T]]) -> Optional[TreeNode[T]]:
        if start is None:
            return None
        if start.value == key:
            return start
        elif key < start.value:  # type: ignore
            if start.left is not None:
                return self.find(key, start.left)
            return start
        else:
            if start.right is not None:
                return self.find(key, start.right)
            return start
    
    def insert(self, value: T) -> None:
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
            
        parent = self.find(value, self.root)
        if parent is None:
            self.root = new_node
            return
            
        new_node.parent = parent
        
        if value < parent.value:  # type: ignore
            parent.left = new_node
        else:
            parent.right = new_node
            
        # Rebalance from the new node up to the root
        current = parent
        while current is not None:
            current = self.rebalance(current)
            current = current.parent if current else None
    
    def delete(self, value: T) -> None:
        node = self.find(value, self.root)
        if node is None or node.value != value:
            return
        
        parent_to_rebalance = node.parent
        
        # Case 3: Node has two children
        if node.left is not None and node.right is not None:
            # Find the next node (smallest value in right subtree)
            successor = node.right
            while successor.left is not None:
                successor = successor.left
                
            node.value = successor.value
            # Move to delete the successor instead
            node = successor
            parent_to_rebalance = node.parent
            
        # At this point, node has at most one child
        
        # Case 1: Node is a leaf
        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
            else:
                if node.parent is not None:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                    
        # Case 2: Node has one child
        else:
            child = node.left if node.left else node.right
            if node == self.root:
                self.root = child
                if child is not None:
                    child.parent = None
            else:
                if node.parent is not None and child is not None:
                    if node.parent.left == node:
                        node.parent.left = child
                    else:
                        node.parent.right = child
                    child.parent = node.parent
        
        # Rebalance from the parent of the deleted node up to the root
        current = parent_to_rebalance
        while current is not None:
            current = self.rebalance(current)
            current = current.parent if current else None
            

if __name__ == "__main__":
    def test_delete(tree, size, num_searches=10000):
        # Insert `size` random elements
        values = random.sample(range(10 * size), size)
        for v in values:
            tree.insert(v)

        # Pick random search keys from the inserted values
        num_searches = min(num_searches, size)
        search_keys = random.sample(values, num_searches)

        # Measure search time
        start_time = time.time()
        for key in search_keys:
            tree.delete(key)
        end_time = time.time()

        avg_time = (end_time - start_time) / num_searches
        return avg_time

    # Run tests
    sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    bst_find_times = []

    for size in sizes:
        bst_tree = AVL()
        bst_time = test_delete(bst_tree, size)
        bst_find_times.append(bst_time)

        print(f"Size {size}: AVL avg remove time = {bst_time:.6e}")


    plt.figure(figsize=(10, 5))
    plt.plot(sizes, bst_find_times, marker='o', label="AVL Remove Time")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tree size (n)")
    plt.ylabel("Avg Find Time (s)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.show()