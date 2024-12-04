class CircularArray():
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1
 
    def pushBack(self, data):

        if ((self.rear + 1) % self.size == self.front): 
            print("Error: Lista llena. No se puede agregar el elemento.")
             
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = data
    
    def pushFront(self, data):
        if ((self.rear + 1) % self.size == self.front): 
            print("Error: Lista llena. No se puede agregar el elemento.")
             
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.front = (self.front - 1) % self.size
            #self.rear = (self.rear + 1) % self.size 
            self.queue[self.front] = data
    
    def popBack(self):
        if (self.front == -1):
            print ("Error: Lista vacia. No se puede eliminar el elemento.")

        elif (self.front == self.rear): 
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            #return temp
        
        else:
            temp = self.queue[self.rear]
            self.rear = (self.rear - 1) % self.size
            #return temp
    
    def popFront(self):
        if (self.front == -1):
            print ("Error: Lista vacia. No se puede eliminar el elemento.")

        elif (self.front == self.rear): 
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            #return temp
        
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            #return temp
 
    def printf(self):
        if self.front == -1:
            print("Elementos en el arreglo: []")

        elif (self.rear >= self.front):
            print("Elementos en el arreglo: [", 
                                              end = "")
            for i in range(self.front, self.rear + 1):
                if i != self.rear and self.front != -1:
                    print(self.queue[i], end = " ")
                else:
                    print(self.queue[i], end = "")
            print ("]")
 
        else:
            print("Elementos en el arreglo: [", 
                                           end = "")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                if i != self.rear and self.front != -1:
                    print(self.queue[i], end = " ")
                else:
                    print(self.queue[i], end = "")
            print ("]")
    
size = int(input())
lst = CircularArray(size)
running = True      
while running:
    try:
        inp = input()
        inp = inp.split()
        if inp[0] == "1":
            lst.printf()
        elif inp[0] == "2":
            lst.pushBack(inp[1])
        elif inp[0] == "3":
            lst.popBack()
        elif inp[0] == "4":
            lst.pushFront(inp[1])
        elif inp[0] == "5":
            lst.popFront()
    except:
        running = False

