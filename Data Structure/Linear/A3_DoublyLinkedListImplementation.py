# DOUBLY LINKED LIST IMPLEMENTAION
class Node :
    def __init__(self,prev=None, data=None, next=None) :
        self.prev = prev
        self.data = data
        self.next = next

# DEFINE METHODS TO PERFORM ON LL
class DoublyLinkedList :
    def __init__(self) :
        self.head = None
        self.count = 0

# ISEMPTY
    def isEmpty(self) :
        return self.count == 0

# DISPLAY
    def display(self) :
        if self.isEmpty() : return "DLL is Empty !"
        
        itr = self.head
        dllstr = ''
        while itr :
            dllstr += str(itr.data)

            if itr.next :
                dllstr += '<-->'

            itr = itr.next

        return dllstr


# INSERT AT BEGINING
    def insert_at_begining(self, data) :
        node = Node(None, data, self.head)
        if self.head is not None :
            self.head.prev = node

        self.head = node

        self.count += 1
        return data


# INSERT AT END
    def insert_at_end(self, data) :
        if self.isEmpty() :
            self.head = Node(None, data, None)
        
        else :
            itr = self.head
            while itr.next :
                itr = itr.next

            node = Node(itr, data, None)   
            itr.next = node

        self.count += 1
        return data


# INSERT AT INDEX
    def insert_at(self, index, data) :
        if index < 0 or  index > self.count : raise IndexError("Invalid Index")

        if index == 0 :     # case of insert_at_begining
            self.insert_at_begining(data)
        
        if index == self.count :     # case of insert_at_end
            self.insert_at_end(data)

        else :
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
            
            self.count += 1

        return data  


# INSERT AFTER A DATA
    def insert_after_data(self, data, data_to_insert) :
        if self.isEmpty() : raise Exception("DLL is Empty !")

        itr = self.head
        while itr :
            if itr.data == data :
                node = Node(itr, data_to_insert, itr.next)
                if itr.next :
                    itr.next.prev = node

                itr.next = node
                self.count += 1
                return data_to_insert
            
            itr = itr.next

        else : raise ValueError("Data Not Found !")


# INSERT A LIST
    def insert_a_list(self, data_list) :     # this method will erase the DLL and create a new DLL with this list
        self.head = None
        self.count = 0
        for data in data_list :
            self.insert_at_end(data)

        return data_list



# LENGHT OF DLL
    def len_of_dll(self) :        
        return self.count 


# REMOVE AT INDEX
    def remove_at(self, index) :
        if self.isEmpty() : raise Exception("DLL is Empty")

        if index < 0 or index >= self.len_of_dll() :
            raise Exception("Invalid Index")

        if index == 0 :
            value = self.head.data
            self.head = self.head.next
            if self.head :
                self.head.prev = None
        
        else :
            itr = self.head
            count = 0
            while itr :
                if count == index  :
                    value = itr.data
                    if itr.next :
                        itr.next.prev = itr.prev
                    if itr.prev :
                        itr.prev.next = itr.next
                    break
                count += 1
                itr = itr.next
        
        self.count -= 1
        return value



# REMOVE BY DATA
    def remove_by_data(self,data) :
        if self.isEmpty() : raise Exception("DLL is Empty !")

        if self.head.data is data :
            self.head = self.head.next
            if self.head :
                self.head.prev = None
        
        else :
            itr = self.head
            while itr :
                if itr.data is data :
                    if itr.next :
                        itr.next.prev = itr.prev
                    
                    if itr.prev :
                        itr.prev.next = itr.next
                    break
                itr = itr.next
            
            else :
                return "Data Not Found"
        
        self.count -= 1
        return data
        

# PRINT FORWARD 
    def print_forward(self) :       # same as display function
        if self.isEmpty() : return "DLL is Empty !"
        
        itr = self.head
        dllstr = ''
        while itr :
            dllstr += str(itr.data) 
            if itr.next :
                dllstr += '<-->'
            
            itr = itr.next
        
        return dllstr


# PRINT BACKWARD
    def print_backward(self) :
        if self.isEmpty() : return "DLL is Empty !"
        
        itr = self.head
        while itr.next :
            itr = itr.next
        
        dllstr = ''
        while itr :
            dllstr += str(itr.data) 

            if itr.prev :
                dllstr += '<-->'

            itr = itr.prev

        return dllstr

 
if __name__ == "__main__" :
    print("DOUBLY LL IMPLEMENTATION\n")
    dll = DoublyLinkedList()
    print("Inserted :", dll.insert_at_begining(10))
    print("Inserted :", dll.insert_at_begining(20))
    print("Inserted :", dll.insert_at_end(30))
    print("Inserted :", dll.insert_at_end(40))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())

    print("Inserted :", dll.insert_at(4,50))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())

    print("Inserted :", dll.insert_after_data(50,60))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())

    print("Inserted :", dll.insert_a_list(["banana","mango","grapes","orange"]))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())

    print("Deleted :", dll.remove_at(3))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())


    print("Deleted :", dll.remove_by_data("grapes"))
    print(dll.display())
    print("Lenght :",dll.len_of_dll())

    print("Inserted :", dll.insert_a_list([1,2,3,4,5,6,7,8,9]))
    print("Lenght :",dll.len_of_dll())

    print(dll.print_forward())
    print(dll.print_backward())






# CIRCULAR DOUBLY LINKED LIST IMPLEMENTATION
class Node : 
    def __init__(self,data) :
        self.prev = None
        self.data = data
        self.next = None

class CDLL :
    def __init__(self) :
        self.head = None
        self.count = 0

    def isEmpty(self) :
        return self.count == 0 
    
    def display(self) :
        if self.isEmpty() : return "CDLL is Empty !"

        itr = self.head
        cdllstr = 'head<-->'
        while True :
            cdllstr += str(itr.data) + '<-->'
            itr = itr.next

            if itr is self.head :
                break

        cdllstr += 'head'
        return cdllstr
    
    def insert_at_beginning(self,data) :
        node = Node(data)
        if self.isEmpty() :
            self.head = node
            node.next = self.head
            node.prev = self.head
        
        else :
            last = self.head.prev

            node.prev = last
            node.next = self.head

            last.next = node
            self.head.prev = node

            self.head = node

        
        self.count += 1
        return data
    
    def insert_at_end(self,data) :
        node = Node(data)
        if self.isEmpty() : 
            self.head = node
            node.next = self.head
            node.prev = self.head
        
        else :
            last = self.head.prev

            node.next = self.head
            node.prev = last

            last.next = node
            self.head.prev = node
        
        self.count += 1
        return data
    
    def insert_at(self,index,data) :
        if index < 0 or index > self.count : raise IndexError("Invalid Index !")

        if index == 0 :
            self.insert_at_beginning(data)
            return data
        
        if index == self.count :
            self.insert_at_end(data)
            return data
        

        node = Node(data)
        itr = self.head
        for _ in range(index) :
            itr = itr.next
        
        node.next = itr
        node.prev = itr.prev

        itr.prev.next = node
        itr.prev =node

        self.count += 1
        return data
    
    def insert_after_data(self,data,data_to_insert) :
        if self.isEmpty() : raise Exception("CDLL is Empty !")

        node = Node(data_to_insert)
        itr = self.head
        while True :
            if itr.data is data :
                node.next = itr.next
                node.prev = itr

                itr.next.prev = node
                itr.next = node
                self.count += 1
                return data_to_insert
            
            itr = itr.next

            if itr is self.head : break

        raise ValueError("Data Not Found !")
    
    def insert_a_list(self,data_list) :
        self.head = None
        self.count = 0
        for data in data_list :
            self.insert_at_end(data)

        return data_list
    
    def length(self) :
        return self.count
    
    def remove_at(self,index) :
        if self.isEmpty() : raise Exception("CDLL is Empty !")
        if index < 0 or index >= self.count : raise IndexError("Invalid Index !")

        if index == 0 :
            value = self.head.data
            if self.count == 1 :
                    self.head = None
            else :
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
        
        else :
            itr = self.head
            for _ in range(index) :
                itr = itr.next

            value = itr.data
            itr.prev.next = itr.next
            itr.next.prev = itr.prev
        
        self.count -= 1
        return value
    
    def remove_by_data(self,data) :
        if self.isEmpty() : raise Exception("CDLL is Empty !")
        if self.head.data is data :
            if self.count == 1 :
                self.head = None
            else :
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next

            self.count -= 1
            return data
        
        itr = self.head
        while True :
            if itr.data is data :
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                self.count -= 1
                return data
            
            itr = itr.next

            if itr is self.head : break

        raise ValueError("Data Not Found !")
    
    def print_forward(self) :
        if self.isEmpty() : return "CDLL is Empty !"

        itr = self.head
        cdllstr = 'head<-->'
        while True :
            cdllstr += str(itr.data) + '<-->'
            itr = itr.next

            if itr is self.head :
                break

        cdllstr += 'head'
        return cdllstr

    def print_backward(self) :
        if self.isEmpty() : return "CDLL is Empty !"
        
        cdllstr = 'head<-->'
        itr = self.head.prev
        while True :
            cdllstr += str(itr.data) + '<-->'
            itr = itr.prev
            
            if itr is self.head.prev :
                break
        
        cdllstr += 'head'
        return cdllstr
    
    def displayAI(self):
        if self.isEmpty():
            return "CDLL is Empty!"

        elements = []

        itr = self.head
        while True:
            elements.append(str(itr.data))
            itr = itr.next

            if itr is self.head:
                break

        line1 = "Head"
        line2 = " ↓"

        # Forward links
        line3 = " " + " ⇄ ".join(elements)

        n = len(line3)

        # Bottom loop
        line4 = "↑" + " " * (n - 2) + "|"
        line5 = "└" + "─" * (n - 2) + "┘"

        return "\n".join([line1, line2, line3, line4, line5])
    

if __name__ == "__main__" :
    print("\nCIRCULAR DOUBLY LL IMPLEMENTATION\n")

    cd = CDLL()
    print("Inserted :", cd.insert_at_beginning(30))
    print("Inserted :", cd.insert_at_beginning(20))
    print("Inserted :", cd.insert_at_beginning(10))
    print("Lenght :",cd.length())
    print(cd.display())

    print("Inserted :", cd.insert_at_end(40))
    print("Inserted :", cd.insert_at_end(50))
    print("Inserted :", cd.insert_at_end(60))
    print("Lenght :",cd.length())
    print(cd.display())

    print("Inserted :", cd.insert_after_data(60,70))
    print("Lenght :",cd.length())
    print(cd.display())

    print("inserted :", cd.insert_a_list(["banana","mango","grapes","orange","pineapple","guava","apple"]))
    print("Lenght :",cd.length())
    print(cd.display())

    print("Deleted :", cd.remove_at(0))
    print("Deleted :", cd.remove_at(5))
    print("Lenght :",cd.length())
    print(cd.display())

    print("Deleted :", cd.remove_by_data("mango"))
    print("Deleted :", cd.remove_by_data("guava"))
    print("Lenght :",cd.length())
    print(cd.display())

    print("inserted :", cd.insert_a_list([1,2,3,4,5,6,7,8,9]))
    print(cd.print_forward())
    print(cd.print_backward())

    
    print(cd.displayAI())
