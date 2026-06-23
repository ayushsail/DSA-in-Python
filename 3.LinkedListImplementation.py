# DEFINE A NODE WITH DATA AND NEXT
class Node :
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

# DEFINE METHODS TO PERFORM ON LL
class LinkedList :
    def __init__(self) :
        self.head = None
    

# DISPLAY   
    def display(self) :
        if self.head is None :
            print("LL is Empty")
            return
        
        itr = self.head
        llstr = ''

        while itr :
            llstr += str(itr.data)

            if itr.next :
                llstr += '-->'
            itr = itr.next
        
        print(llstr)


# INSERT AT BEGINING
    def insert_at_begining(self, data) :
        node = Node(data, self.head)
        self.head = node


# INSERT AT END
    def insert_at_end(self, data) :
        if self.head is None :
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next :
            itr = itr.next
        
        node = Node(data, None)
        itr.next = node


# INSERT AT INDEX
    def insert_at(self, index, data) :
        if index < 0 or index > self.len_of_ll() :
            raise Exception("Invalid Index")

        if index == 0 :     # case of insert_at_begining
            self.insert_at_begining(data)
            return

        if index == self.len_of_ll() - 1 :      # case of insert_at_end
            self.insert_at_end(data) 
            return

        itr = self.head
        count = 0

        while itr :
            if count == index - 1 :
                node = Node(data, itr.next)
                itr.next = node
                break

            count += 1
            itr = itr.next


# INSERT AFTER A DATA
    def insert_after_data(self, data,data_to_insert) :
        itr = self.head
        while itr :
            if itr.data == data :
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next 

        else :
            print("Data not found in LL")


# INSERT A LIST
    def insert_a_list(self, data_list) :    # this method will erase the LL and create a new LL with this list
        self.head = None
        for data in data_list :
            self.insert_at_end(data)
        

# LENGHT OF LL
    def len_of_ll(self) :
        if self.head is None :
            print("LL is Empty")
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
        
        if index < 0 or index >=self.len_of_ll() :
            raise Exception("Invalid Index")
        
        if index == 0 :
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr :
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            count += 1
            itr = itr.next


# REMOVE BY DATA
    def remove_by_data(self, data) :
        if self.head is None :
            print("DLL is Empty")
            return
        
        if self.head.data == data :
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next :
            if itr.next.data == data :
                itr.next = itr.next.next
                break

            itr = itr.next
        
        else :
            print("Data not found in LL")




ll = LinkedList()
ll.insert_at_begining(100)
ll.insert_at_begining(101)
ll.insert_at_end(99)
ll.display()
ll.insert_at(1,200)
ll.display()
print("Lenght :",ll.len_of_ll())

ll.remove_at(4)
ll.display()

ll.insert_a_list(["banana","mango","grapes","orange"])
ll.insert_after_data("mango","apple") # insert apple after mango
ll.display()
ll.remove_by_data("orange") # remove orange from linked list
ll.display()
ll.remove_by_data("figs")
ll.display()
print("Lenght :",ll.len_of_ll())
ll.remove_by_data("banana")
ll.remove_by_data("mango")
ll.remove_by_data("apple")
ll.remove_by_data("grapes")

ll.display()