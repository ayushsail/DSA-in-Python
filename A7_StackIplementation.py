# STACK ARRAY IMPLEMENTATION
print("STACK ARRAY IMPLEMENTATION\n")
class StackArr :
    def __init__ (self,size) :
        self.size = size
        self.arr = [None] * size
        self.TOP = -1
    
    def isFull(self) :
        if self.TOP == self.size -1 :
            return True
        else :
            return False
    
    def isEmpty(self) :
        if self.TOP == -1 :
            return True
        else :
            return False
        
    def push(self,data) :
        if self.isFull() :
            raise Exception ("Stack Overflow !")
        self.TOP += 1
        self.arr[self.TOP] = data
        return data
    
    def pop(self) :
        if self.isEmpty() :
            raise Exception ("Stack Underflow !")
        
        value = self.arr[self.TOP]
        self.arr[self.TOP] = None
        self.TOP -= 1
        return value
    
    def peek(self) :
        if self.isEmpty() :
            raise Exception ("Stack Underflow !")
        
        return self.arr[self.TOP]
    
    def get_size(self) :
        return self.TOP + 1
    
    def display(self) :
        if self.isEmpty() :
            print("Stack Underflow !")
            return
        
        for i in range(self.TOP,-1,-1) :
            print(self.arr[i])
    
    def clear(self) :
        self.arr = [None] * self.size
        self.TOP = -1

    


sa = StackArr(5)
print("Pushed :",sa.push(100))
print("Pushed :",sa.push(200))
print("Pushed :",sa.push(300))
print("Pushed :",sa.push(400))
print("Pushed :",sa.push(500))
print(sa.arr)

print("Popped :",sa.pop())
print("Popped :",sa.pop())
print("Popped :",sa.pop())
print(sa.arr)

print("Topmost element :",sa.peek())

print("No. of element :",sa.get_size())

print("Pushed :",sa.push(300))
print("Pushed :",sa.push(400))
print("Pushed :",sa.push(500))
sa.display()

sa.clear()
sa.display()




# STACK LL IMPLEMENTATION
print("\nSTACK LL IMPLEMENTATION\n")
class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None 

class StackLL :
    def __init__(self) :
        self.top = None       # which will be our head
        self.count = 0

    def isEmpty(self) :
        if self.top is None :
            return True
        else :
            return False
    
    def display(self) :
        if self.isEmpty() :
            print("Stack Underflow !\n")
            return
        itr = self.top
        while itr :
            print(itr.data)
            itr = itr.next
    
    def push(self,data) :
        node = Node(data)
        node.next = self.top
        self.top = node
        self.count += 1
        return data
    
    def pop(self) :
        if self.isEmpty() :
            raise Exception("Stack Underflow !")
        
        value = self.top.data
        self.top = self.top.next
        self.count -= 1
        return value
    
    def peek(self) :
        if self.isEmpty() :
            raise Exception("Stack Underflow !")

        return self.top.data
    
    def get_size(self) :
        return self.count

    def clear(self) :
        self.top = None
        self.count = 0

sl = StackLL()
print("Pushed :",sl.push(1))
print("Pushed :",sl.push(2))
print("Pushed :",sl.push(3))
print("Pushed :",sl.push(4))
print("Pushed :",sl.push(5))

sl.display()

print("Popped :",sl.pop())
print("Popped :",sl.pop())
print("Popped :",sl.pop())
sl.display()

print("Topmost element :", sl.peek())
print("No. of element :",sl.get_size())

sl.clear()
sl.display()




# STACK IMPLEMENTATION USING CLASS COLLECTION.DEQUE 
# this is the recommended way in python
# deques are generalization of stack & queues
# deques are implemented using doubly LL
print("\nSTACK DEQUE IMPLEMENTATION\n")
from collections import deque
stack = deque()
# print(dir(stack))   # this will show you all the methods

class Stack :
    def __init__(self) :
        self.container = deque()
    
    def push(self,data) :
        self.container.append(data)
        return data
    
    def pop(self) :
        return self.container.pop()
        
    def peek(self) :
         return self.container[-1]

    def isEmpty(self) :
        return len(self.container) == 0
    
    def size(self) :
        return len(self.container)
    
    def display(self) :
        print(self.container)
    

sq = Stack()
print("Pushed :",sq.push(100))
print("Pushed :",sq.push(200))
print("Pushed :",sq.push(300))  
print("Pushed :",sq.push(400))
print("Pushed :",sq.push(500))
sq.display()

print("Popped :",sq.pop())
print("Popped :",sq.pop())
sq.display()

print("Empty :",sq.isEmpty())
print("No. of element :",sq.size())

print("Popped :",sq.pop())
print("Popped :",sq.pop())
print("Popped :",sq.pop())
sq.display()

print("Empty :",sq.isEmpty())

