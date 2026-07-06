# DEQUE USING CIRCULAR ARRAY

class DequeArr :
    def __init__(self,size) :
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self) :
        return self.count == 0 
    def isFull(self) :
        return self.count == self.size
    
    def insert_front(self,data) :
        if self.isFull() : raise Exception("Deque Overflow !")

        if self.isEmpty() :
            self.front = self.rear = 0
            # empty case - need to update both front & rear and then insert
        
        else :
            self.front = (self.front - 1 + self.size) % self.size
            # front goes backward before insertion

        self.arr[self.front] = data
        self.count += 1
        return data

    def insert_rear(self,data) :
        if self.isFull() : raise Exception("Deque Overflow !")
        
        if self.isEmpty() :
            self.front = self.rear = 0
            # empty case - need to update both front & rear and then insert
        
        else :
            self.rear = (self.rear + 1) % self.size
            # rear goes forward before insertion

        self.arr[self.rear] = data
        self.count += 1
        return data
    
    def delete_front(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")

        value = self.arr[self.front]
        self.arr[self.front] = None

        if self.count == 1 :
            self.front = self.rear = -1
            # going-to-be-empty case - need to update both front & rear after deletion of last present element
        
        else :
            self.front = (self.front + 1) % self.size
            # rear goes forward after deletion

        self.count -= 1
        return value
    
    def delete_rear(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")

        value = self.arr[self.rear]
        self.arr[self.rear] = None

        if self.count == 1 :
            self.front = self.rear = -1
            # going-to-be-empty case - need to update both front & rear after deletion of last present element

        else :
            self.rear = (self.rear - 1 + self.size) % self.size
            # rear goes backward after deletion
        
        self.count -= 1
        return value
    

    def display(self) :
        if self.isEmpty() : return "Deque Underflow !"

        dstr = 'front --> ' 
        current = self.front
        for _ in range(self.count) :
            dstr += str(self.arr[current]) + ' '
            current = (current + 1) % self.size
        
        dstr += '<-- rear'
        return dstr
    
    def get_front(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")
        return self.arr[self.front] 
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")
        return self.arr[self.rear]
    def get_size(self) :
        return self.count


if __name__ == "__main__" :
    print("DEQUE USING CIRCULAR ARRAY\n")

    da = DequeArr(10)
    print("Inserted :", da.insert_rear(1))
    print("Inserted :", da.insert_rear(2))
    print("Inserted :", da.insert_rear(3))
    print("Inserted :", da.insert_rear(4))
    print("Inserted :", da.insert_rear(5))
    print(da.arr)
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Inserted :", da.insert_front(6))
    print("Inserted :", da.insert_front(7))
    print("Inserted :", da.insert_front(8))
    print("Inserted :", da.insert_front(9))
    print("Inserted :", da.insert_front(10))
    print(da.arr)
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Deleted :", da.delete_front())
    print("Deleted :", da.delete_front())
    print(da.arr)
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Deleted :", da.delete_rear())
    print("Deleted :", da.delete_rear())
    print(da.arr)
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())






# DEQUE USING CIRCULAR DOUBLY LINKED LIST

class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        self.prev = None

class DequeCDLL :
    def __init__(self) :
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self) :
        return self.count == 0
    
    def insert_front(self,data) :
        node = Node(data)
        if self.isEmpty() :
            self.front = self.rear = node
            # empty case - need to update both front & rear
            node.next = self.front
            node.prev = self.front
        
        else :
            # first - node insertion
            node.prev = self.rear
            node.next = self.front

            # second - updating front & rear pointer
            self.rear.next = node
            self.front.prev = node

            # third - assigning front to the node
            self.front = node
        
        self.count += 1
        return data
    
    def insert_rear(self,data) :
        node = Node(data)
        if self.isEmpty() :
            self.rear = self.front = node
            # empty case - need to update both front & rear
            node.next = self.rear
            node.prev = self.rear

        else :
            # first - node insertion
            node.next = self.front
            node.prev = self.rear

            # second - updating front & rear pointer
            self.rear.next = node
            self.front.prev = node

            # third - assigning rear to the node
            self.rear = node
        
        self.count += 1
        return  data

    def delete_front(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")

        # first - store value
        value = self.front.data

        if self.count == 1 :
            self.front = self.rear = None
            # going-to-be-empty case - need to update both front & rear to "None"
        
        else :
            # else - update pointers of front & rear
            self.rear.next = self.front.next
            self.front.next.prev = self.rear

            # assigning front to node
            self.front = self.front.next
        
        self.count -= 1
        return value
    
    def delete_rear(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")

        # first - store value
        value = self.rear.data

        if self.count == 1 :
            self.rear = self.front = None
            # going-to-be-empty case - need to update both front & rear to "None"
        
        else :
            # else - update pointers of front & rear
            self.rear.prev.next = self.front
            self.front.prev = self.rear.prev

            # assigning rear to node
            self.rear = self.rear.prev
        
        self.count -= 1
        return value
    
    def display(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")

        itr = self.front
        dstr = 'front --> '
        while True :
            dstr += str(itr.data) + ' '
            itr = itr.next

            if itr == self.front : break

        dstr += '<-- rear'
        return dstr
    

    def get_front(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")
        return self.front.data
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Deque Underflow !")
        return self.rear.data
    def get_size(self) :
        return self.count


if __name__ == "__main__" :
    print("\nDEQUE USING CIRCULAR DOUBLY LINKED LIST\n")

    da = DequeCDLL()
    print("Inserted :", da.insert_rear(1))
    print("Inserted :", da.insert_rear(2))
    print("Inserted :", da.insert_rear(3))
    print("Inserted :", da.insert_rear(4))
    print("Inserted :", da.insert_rear(5))
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Inserted :", da.insert_front(6))
    print("Inserted :", da.insert_front(7))
    print("Inserted :", da.insert_front(8))
    print("Inserted :", da.insert_front(9))
    print("Inserted :", da.insert_front(10))
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Deleted :", da.delete_front())
    print("Deleted :", da.delete_front())
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())

    print("Deleted :", da.delete_rear())
    print("Deleted :", da.delete_rear())
    print(da.display())
    print("front :", da.get_front())
    print("rear :", da.get_rear())
    print("No. of elements :", da.get_size())
