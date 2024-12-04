import time
import matplotlib.pyplot as plt
from typing import TypeVar, Generic

T = TypeVar('T')  # Define type variable "T"

class Lista(Generic[T]):
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.last_element_index: int = -1
        self.array: list[T] = [None for i in range(0,size)]
    
    def pushBack(self, elem: T) -> None:
        if self.last_element_index == self.size - 1:
            print("Error: Lista llena. No se puede agregar el elemento.")
        else: 
            self.array[self.last_element_index + 1] = elem
            self.last_element_index += 1
    
    def popBack(self) -> None:
        if self.last_element_index == -1:
            print("Error: Lista vacia. No se puede eliminar el elemento.")
        else:
            self.array[self.last_element_index] = 0
            self.last_element_index -= 1
    
    def printf(self) -> None:
        print(f"Elementos en el arreglo: [", end= "")
        for i in range(0, self.last_element_index + 1):
            if i != self.last_element_index:
                print(self.array[i], end=" ")
            else:
                print(self.array[i], end="")
        print("]")
    
    def pushFront(self, elem: T) -> None:
        if self.last_element_index == self.size - 1:
            print("Error: Lista llena. No se puede agregar el elemento.")
        else:
            for i in range(0, self.last_element_index + 1):
                self.array[self.last_element_index + 1 - i] = self.array[self.last_element_index - i]
            self.array[0] = elem
            self.last_element_index += 1
            
    def popFront(self) -> None:
        if self.last_element_index == -1:
            print("Error: Lista vacia. No se puede eliminar el elemento.")
        else:
            for i in range(0, self.last_element_index + 1):
                try:
                    self.array[i] = self.array[i+1]
                except:
                    pass
            self.last_element_index -= 1
    
    def find(self, elem: T) -> T:
        for i in range(0, self.last_element_index+1):
            if self.array[i] == elem:
                return i
        return -1

    def erase(self, elem: T) -> None:
        indx: int = self.find(elem)
        if indx != -1:
            if self.last_element_index == -1:
                print("Error: Lista vacia. No se puede eliminar el elemento.")
            else:
                for i in range(indx, self.last_element_index + 1):
                    try:
                        self.array[i] = self.array[i+1]
                    except:
                        pass
                self.last_element_index -= 1
        else:
            print("Element not in list")

    def addBefore(self, elem: T, insert :T) -> None:
        indx: int = self.find(elem)
        if indx != -1:
            if self.last_element_index == self.size - 1:
                print("Error: Lista llena. No se puede agregar el elemento.")
            else:
                for i in range(indx-1, self.last_element_index + 1):
                    self.array[self.last_element_index + 1 - i] = self.array[self.last_element_index - i]
                self.array[indx-1] = insert
                self.last_element_index += 1
        else:
            print("Element not in list")
    
    def addAfter(self, elem: T, insert :T) -> None:
        indx: int = self.find(elem)
        if indx != -1:
            if self.last_element_index == self.size - 1:
                print("Error: Lista llena. No se puede agregar el elemento.")
            else:
                for i in range(indx+1, self.last_element_index + 1):
                    self.array[self.last_element_index + 1 - i] = self.array[self.last_element_index - i]
                self.array[indx+1] = insert
                self.last_element_index += 1
        else:
            print("Element not in list")
    
    def empty(self) -> None: 
        self.last_element_index = -1
        

# Hackerrank code
# size = int(input())
# lst = Lista[int](size)
# running = True      
# while not running:
#     try:
#         inp = input()
#         inp = inp.split()
#         if inp[0] == "1":
#             lst.printf()
#         elif inp[0] == "2":
#             lst.addLast(inp[1])
#         elif inp[0] == "3":
#             lst.removeLast()
#         elif inp[0] == "4":
#             lst.addFirst(inp[1])
#         elif inp[0] == "5":
#             lst.removeFirst()
#     except:
#         running = False

#Time-tests
# sizes = [100, 1000, 10000, 100000, 1000000, 10000000] 
# insertion_time = []
# remove_time = []

# for size in sizes:
#     start = time.time()
#     lst = Lista[int](size)
#     for i in range(0, lst.size):
#         lst.pushBack(i)
#     end = time.time()
#     time_measure = (end - start)/size
#     insertion_time.append(time_measure)
    
#     start = time.time()
#     for i in range(0, lst.size):
#         lst.popFront()
#     end = time.time()
#     time_measure = (end - start)/size
#     remove_time.append(time_measure)

# removeLast =  [0.0, 0.0, 0.0, 1.6487598419189454e-07, 1.0928702354431152e-07, 1.1763114929199219e-07]
# removeFirst = [1.768594086754930e-05, 5.09876545678913e-05, 0.000365743902, 0.003546328, 0.00895487365, 0.026463829]

# plt.plot(sizes, removeLast, label="removeLast()")
# plt.show()  # O(1)
# plt.plot(sizes, removeFirst, label="removeFirst()")
# plt.show() # O(n)


