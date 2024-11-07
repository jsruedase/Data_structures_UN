class Lista:
    def __init__(self, size) -> None:
        self.size = size
        self.last_element_index = -1
        self.array = [None for i in range(0,size)]
    
    def addLast(self, elem):
        if self.last_element_index == self.size - 1:
            print("Error: Lista llena. No se puede agregar el elemento.")
        else: 
            self.array[self.last_element_index + 1] = elem
            self.last_element_index += 1
    
    def removeLast(self):
        if self.last_element_index == -1:
            print("Error: Lista vacia. No se puede eliminar el elemento.")
        else:
            self.array[self.last_element_index] = 0
            self.last_element_index -= 1
    
    def printf(self):
        print(f"Elementos en el arreglo: [", end= "")
        for i in range(0, self.last_element_index + 1):
            if i != self.last_element_index:
                print(self.array[i], end=" ")
            else:
                print(self.array[i], end="")
        print("]")
    
    def addFirst(self, elem):
        if self.last_element_index == self.size - 1:
            print("Error: Lista llena. No se puede agregar el elemento.")
        else:
            for i in range(0, self.last_element_index + 1):
                self.array[self.last_element_index + 1 - i] = self.array[self.last_element_index - i]
            self.array[0] = elem
            self.last_element_index += 1
            
    def removeFirst(self):
        if self.last_element_index == -1:
            print("Error: Lista vacia. No se puede eliminar el elemento.")
        else:
            for i in range(0, self.last_element_index + 1):
                try:
                    self.array[i] = self.array[i+1]
                except:
                    pass
            self.last_element_index -= 1
        

size = int(input())
lst = Lista(size)
running = True      
while running:
    try:
        inp = input()
        inp = inp.split()
        if inp[0] == "1":
            lst.printf()
        elif inp[0] == "2":
            lst.addLast(inp[1])
        elif inp[0] == "3":
            lst.removeLast()
        elif inp[0] == "4":
            lst.addFirst(inp[1])
        elif inp[0] == "5":
            lst.removeFirst()
    except:
        running = False
    
