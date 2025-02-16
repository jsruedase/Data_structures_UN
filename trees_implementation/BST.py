from abc import ABC, abstractmethod
import time
import matplotlib.pyplot as plt
import random
from typing import TypeVar, Generic, Optional, List, Any

T = TypeVar('T')  # Define type variable for comparable types

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

class BST(BinarySearchTreeInterface[T]):
    def __init__(self) -> None:
        self.root: Optional[TreeNode[T]] = None
    
    def height(self, start: Optional[TreeNode[T]]) -> int:
        if start is None:
            return 0
        elif start.left is None and start.right is None:
            return 1
        else:
            return 1 + max(self.height(start.left), self.height(start.right))
        
    def height2(self, start: Optional[TreeNode[T]]) -> int:
        if start is None:
            return 0
        else:
            return 1 + max(self.height(start.left), self.height(start.right))
    
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
    
    def find(self, key: T, start: TreeNode[T]) -> TreeNode[T]:
        if start.value == key:
            return start
        elif key < start.value:  
            if start.left is not None:
                return self.find(key, start.left)
            return start
        else:
            if start.right is not None:
                return self.find(key, start.right)
            return start
    
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
    
    def insert(self, value: T) -> None:
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            parent = self.find(value, self.root)
            new_node.parent = parent
            if value < parent.value:  
                parent.left = new_node
            else:
                parent.right = new_node

    def delete(self, value: T) -> None:
        if self.root is None:
            print("Tree is empty")
            return
            
        node = self.find(value, self.root)
        if node is None or node.value != value:
            print("Node not found")
            return
            
        def delete_node(node: TreeNode[T]) -> None:
            # Case 1: Leaf
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                else:
                    parent = node.parent
                    if parent is not None:
                        if parent.left == node:
                            parent.left = None
                        else:
                            parent.right = None
                        
            # Case 2: 1 child
            elif node.left is None or node.right is None:
                child = node.left if node.left else node.right
                if node == self.root:
                    self.root = child
                    if child is not None:
                        child.parent = None
                else:
                    parent = node.parent
                    if parent is not None and child is not None:
                        if parent.left == node:
                            parent.left = child
                        else:
                            parent.right = child
                        child.parent = parent
                    
            # Case 3: 2 children
            else:
                next_node = self.next(node)
                if next_node is not None:
                    node.value = next_node.value
                    delete_node(next_node)
        
        delete_node(node)
        
if __name__ == "__main__":
    h1 = []
    h2 = []
    for i in range(0, 10):
        tr = BST()
        for i in range(0, 1000000):
            tr.insert(random.randint(0, 1000000))
        start = time.time()
        r = tr.height(tr.root)
        end = time.time()
        h1.append(end - start)
        
        start = time.time()
        r = tr.height2(tr.root)
        end = time.time()
        h2.append(end - start)
    print("Average height1 time: ", sum(h1) / len(h1))
    print("Average height2 time: ", sum(h2) / len(h2))

    
