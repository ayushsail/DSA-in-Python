# DEFINE A NODE WITH PREV, DATA AND NEXT
class Node :
    def __init__(self,prev=None, data=None, next=None) :
        self.prev = prev
        self.data = data
        self.next = next

# DEFINE METHODS TO PERFORM ON LL
class DoublyLinkedList :
    def __init__(self) :
        self.head = None


# DISPLAY
    def display(self) :
        if self.head is None :
            print("DLL is Empty")
            return
        
        itr = self.head
        dllstr = ''
        while itr :
            dllstr += str(itr.data)

            if itr.next :
                dllstr += '<-->'

            itr = itr.next

        print(dllstr)


# INSERT AT BEGINING
    def insert_at_begining(self, data) :
        node = Node(None, data, self.head)
        if self.head is not None :
            self.head.prev = node

        self.head = node


# INSERT AT END
    def insert_at_end(self, data) :
        if self.head is None :
            self.head = Node(None, data, None)
            return
        
        itr = self.head
        while itr.next :
             itr = itr.next

        node = Node(itr, data, None)   
        itr.next = node


# INSERT AT INDEX
    def insert_at(self, index, data) :
        if index < 0 or  index > self.len_of_dll() :
            raise Exception("Invalid Index")

        if index == 0 :     # case of insert_at_begining
            self.insert_at_begining(data)
            return
        
        if index == self.len_of_dll() - 1 :     # case of insert_at_end
            self.insert_at_end(data)
            return

        itr = self.head
        count = 0
        while itr :
            if count == index - 1 :
                node = Node(itr, data, itr.next)
                itr.next.prev = node
                itr.next = node
                break

            count += 1
            itr = itr.next


# INSERT AFTER A DATA
    def insert_after_data(self, data, data_to_insert) :
        itr = self.head
        while itr :
            if itr.data == data :
                node = Node(itr, data_to_insert, itr.next)
                if itr.next :
                    itr.next.prev = node

                itr.next = node
                break
            
            itr = itr.next

        else :
            print("Data not found in DLL")


# INSERT A LIST
    def insert_a_list(self, data_list) :     # this method will erase the DLL and create a new DLL with this list
        self.head = None
        for data in data_list :
            self.insert_at_end(data)



# LENGHT OF DLL
    def len_of_dll(self) :
        if self.head is None :
            print("DLL is Empty")
            return
        
        itr = self.head
        count = 0
        while itr :
            count += 1
            itr = itr.next
        
        return count


# REMOVE AT INDEX
    def remove_at(self, index) :
        if self.head is None :
            print("DLL is Empty")
            return

        if index < 0 or index >= self.len_of_dll() :
            raise Exception("Invalid Index")

        if index == 0 :
            self.head = self.head.next
            if self.head :
                self.head.prev = None
            return
        
        itr = self.head
        count = 0
        while itr :
            if count == index  :
                if itr.next :
                    itr.next.prev = itr.prev
                if itr.prev :
                    itr.prev.next = itr.next
                break
            count += 1
            itr = itr.next


# REMOVE BY DATA
    def remove_by_data(self,data) :
        if self.head is None :
            print("DLL is Empty")
            return

        if self.head.data == data :
            self.head = self.head.next
            if self.head :
                self.head.prev = None
            return
        
        itr = self.head
        while itr :
            if itr.data == data :
                if itr.next :
                    itr.next.prev = itr.prev
                
                if itr.prev :
                    itr.prev.next = itr.next
                break
            itr = itr.next
        
        else :
            print("Data Not Found")
        

# PRINT FORWARD 
    def print_forward(self) :       # same as print
        if self.head is None :
            print("DLL is Empty")
            return
        
        itr = self.head
        dllstr = ''
        while itr :
            dllstr += str(itr.data) 
            if itr.next :
                dllstr += '<-->'
            
            itr = itr.next
        
        print(dllstr)


# PRINT BACKWARD
    def print_backward(self) :
        if self.head is None :
            print("DLL is Empty")
            return
        
        itr = self.head
        while itr.next :
            itr = itr.next
        
        dllstr = ''
        while itr :
            dllstr += str(itr.data) 

            if itr.prev :
                dllstr += '<-->'

            itr = itr.prev

        print(dllstr)



dll = DoublyLinkedList()
dll.insert_at_begining(10)
dll.insert_at_begining(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.display()
print("Lenght :",dll.len_of_dll())

dll.insert_at(3,50)
dll.display()
print("Lenght :",dll.len_of_dll())

dll.insert_after_data(50,60)
dll.display()
print("Lenght :",dll.len_of_dll())

dll.insert_a_list(["banana","mango","grapes","orange"])
dll.display()
print("Lenght :",dll.len_of_dll())

dll.remove_at(3)
dll.display()

dll.remove_by_data("grapes")
dll.display()

dll.insert_a_list([1,2,3,4,5,6,7,8,9])

dll.print_forward()
dll.print_backward()