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

    


s = StackArr(5)
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
        return self.top.data
    
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