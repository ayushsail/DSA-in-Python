# FIXED ARRAY IMPLEMENTATION
class FixedArray :
    def __init__ (self,size) :
        self.size = size
        self.count = 0
        self.arr = [None] * size

    def isEmpty(self) :
        if self.count == 0 :
            return True
        else :
            return False
        
    def isFull(self) :
        if self.count == self.size :
            return True
        else :
            return False
    
    def insert_at_begining(self,data) :
        if self.isFull() :
            raise Exception("Array Overflow")

        else :
            for i in range(self.count-1,-1,-1) :
                self.arr[i+1] = self.arr[i]
            
            self.arr[0] = data
            self.count += 1

    def insert_at_end(self,data) :
        if self.isFull() :
            raise Exception("Array Overflow")
        
        self.arr[self.count]  = data
        self.count += 1
    
    def insert_at(self,index,data) :
        if self.isFull() :
            raise Exception("Array Overflow")
        if index < 0 or index > self.count :
            raise IndexError("Invalid Index")
        for i in range(self.count-1,index-1,-1) :
            self.arr[i+1] = self.arr[i]
        self.arr[index] = data
        self.count += 1
    
    def display(self) :
        if self.isEmpty() :
            print("Array Underflow")
            return
        arrstr = ''
        for i in range(self.count)  :
            arrstr += str(self.arr[i]) + ' '
        print(arrstr)

    def delete_at(self,index) :
        if self.isEmpty() :
            print("Array Underflow")
            return
        if index < 0 or index >= self.count :
            raise IndexError("Invalid Index")
        value = self.arr[index]
        for i in range(index,self.count-1) :
            self.arr[i] = self.arr[i+1]
        
        self.count -= 1
        self.arr[self.count] = None
        return value


if __name__ == "__main__"  :       
    print("FIXED ARRAY\n")
    a = FixedArray(5)
    # print(a.count)
    # a.display()
    a.insert_at_begining(1)
    a.insert_at_begining(2)
    a.insert_at_end(3)
    a.insert_at_end(4)
    a.insert_at(2,100)
    print(a.delete_at(3))
    print(a.delete_at(3))
    print(a.delete_at(0))
    a.display()
    print(a.arr)


 
# DYNAMIC ARRAY IMPLEMENTATION
# two new function called resize() and shrink() which make it dynamic
# except this two function, it is same as fixed array
class DynamicArray :
    def __init__ (self,size) :
        self.size = size
        self.initial_size = size
        self.count = 0
        self.arr = [None] * size
    
    def resize(self) :
        new_size = self.size*2     # new size
        new_arr = [None] * new_size
        for i in range(self.count) :
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr
        self.size = new_size
    
    def shrink(self) :
        if self.size > self.initial_size and self.count <= self.size // 4 :
            new_size = self.size // 2
            new_arr = [None] * new_size
            for i in range(self.count) :
                new_arr[i] = self.arr[i]

            self.arr = new_arr
            self.size = new_size


    def isEmpty(self) :
        if self.count == 0 :
            return True
        else :
            return False
        
    def isFull(self) :
        if self.count == self.size :
            return True
        else :
            return False
    
    def insert_at_begining(self,data) :
        if self.isFull() :
            self.resize()

        for i in range(self.count-1,-1,-1) :
            self.arr[i+1] = self.arr[i]
            
        self.arr[0] = data
        self.count += 1

    def insert_at_end(self,data) :
        if self.isFull() :
            self.resize()
        
        self.arr[self.count]  = data
        self.count += 1
    
    def insert_at(self,index,data) :
        if self.isFull() :
            self.resize()
            
        if index < 0 or index > self.count :
            raise IndexError("Invalid Index")
        for i in range(self.count-1,index-1,-1) :
            self.arr[i+1] = self.arr[i]
        self.arr[index] = data
        self.count += 1
    
    def display(self) :
        if self.isEmpty() :
            print("Array Underflow")
            return
        arrstr = ''
        for i in range(self.count)  :
            arrstr += str(self.arr[i]) + ' '
        print(arrstr)

    def delete_at(self,index) :
        if self.isEmpty() :
            print("Array Underflow")
            return
        if index < 0 or index >= self.count :
            raise IndexError("Invalid Index")
        value = self.arr[index]
        for i in range(index,self.count-1) :
            self.arr[i] = self.arr[i+1]
        
        self.count -= 1
        self.arr[self.count] = None

        self.shrink()           # new addition in delete_at method to make it dynamic

        return value



if __name__ == "__main__" :
    print("\nDYNAMIC ARRAY\n")  
    a = DynamicArray(5)

    print(a.arr)        # size = 5

    a.insert_at_end(1)
    a.insert_at_end(2)
    a.insert_at_end(3)
    a.insert_at_end(4)
    a.insert_at_end(5)
    a.insert_at_end(6)

    print(a.arr)        # size = 10

    a.insert_at_end(7)
    a.insert_at_end(8)
    a.insert_at_end(9)
    a.insert_at_end(10) 
    a.insert_at_end(11)
    a.insert_at_end(12)

    print(a.arr)        # size = 20

    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)

    print(a.arr)        # size = 10

    a.delete_at(0)
    a.delete_at(0)
    a.delete_at(0)

    print(a.arr)        # size = 5

    a.delete_at(0)
    a.delete_at(0)

    print(a.arr)        # now it doesn't shrink further