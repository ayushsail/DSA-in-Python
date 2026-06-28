# STACK ARRAY IMPLEMENTATION
from A1_ArrayImplementation import DynamicArray

print("STACK ARRAY IMPLEMENTATION\n")
class Stack :
    def __init__ (self,size) :
        self.size = size
        self.arr = DynamicArray(size)
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
        return self.arr[self.TOP]
    
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

    


s = Stack(5)
print("Pushed :",s.push(100))
print("Pushed :",s.push(200))
print("Pushed :",s.push(300))
print("Pushed :",s.push(400))
print("Pushed :",s.push(500))
print(s.arr)

print("Popped :",s.pop())
print("Popped :",s.pop())
print("Popped :",s.pop())
print(s.arr)

print("Topmost element :",s.peek())

print("No. of element :",s.get_size())

print("Pushed :",s.push(300))
print("Pushed :",s.push(400))
print("Pushed :",s.push(500))
s.display()

s.clear()
s.display()


# STACK LL IMPLEMENTATION
print("STACK LL IMPLEMENTATION\n")