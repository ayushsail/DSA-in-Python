# LL IMPLEMENTATION

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


# ISEMPTY CONDITION
    def isEmpty(self):
        return self.count == 0


# DISPLAY
    def display(self):
        if self.isEmpty():
            return "LL is Empty !"

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data)

            if itr.next:
                llstr += "-->"

            itr = itr.next

        return llstr


# INSERT AT BEGINNING
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        self.count += 1
        return data


# INSERT AT END
    def insert_at_end(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = node

        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = node

        self.count += 1
        return data


# INSERT AT INDEX
    def insert_at(self, index, data):
        if index < 0 or index > self.count: raise IndexError("Invalid Index !")

        if index == 0:
            self.insert_at_beginning(data)
            return data

        if index == self.count:
            self.insert_at_end(data)
            return data

        itr = self.head

        for _ in range(index - 1):
            itr = itr.next

        node = Node(data)
        node.next = itr.next
        itr.next = node

        self.count += 1
        return data


# INSERT AFTER DATA
    def insert_after_data(self, data, data_to_insert):
        if self.isEmpty():
            raise Exception("LL is Empty !")

        itr = self.head

        while itr:
            if itr.data == data:
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node

                self.count += 1
                return data_to_insert

            itr = itr.next

        raise ValueError("Data Not Found !")


# INSERT A LIST
    def insert_a_list(self, data_list):
        self.head = None
        self.count = 0

        for data in data_list:
            self.insert_at_end(data)

        return data_list


# LENGTH
    def length(self):
        return self.count


# REMOVE AT INDEX
    def remove_at(self, index):
        if self.isEmpty():
            raise Exception("LL is Empty !")

        if index < 0 or index >= self.count:
            raise IndexError("Invalid Index !")

        if index == 0:
            value = self.head.data
            self.head = self.head.next

        else:
            itr = self.head

            for _ in range(index - 1):
                itr = itr.next

            value = itr.next.data
            itr.next = itr.next.next

        self.count -= 1
        return value


# REMOVE BY DATA
    def remove_by_data(self, data):
        if self.isEmpty():
            raise Exception("LL is Empty !")

        if self.head.data == data:
            value = self.head.data
            self.head = self.head.next

            self.count -= 1
            return value

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                value = itr.next.data
                itr.next = itr.next.next

                self.count -= 1
                return value

            itr = itr.next

        raise ValueError("Data Not Found !")


if __name__ == "__main__":
    print("\nLL IMPLEMENTATION\n")

    ll = LinkedList()

    print("Inserted :", ll.insert_at_beginning(3))
    print("Inserted :", ll.insert_at_beginning(2))
    print("Inserted :", ll.insert_at_beginning(1))
    print("Length :", ll.length())
    print(ll.display())

    print("Inserted :", ll.insert_at_end(4))
    print("Inserted :", ll.insert_at_end(5))
    print("Length :", ll.length())
    print(ll.display())

    print("Inserted :", ll.insert_at(0, 100))
    print("Inserted :", ll.insert_after_data(3, 300))
    print("Inserted :", ll.insert_after_data(100, 400))
    print("Length :", ll.length())
    print(ll.display())

    print("Inserted :", ll.insert_a_list(["banana", "mango", "grapes", "orange", "pineapple", "guava", "apple"]))
    print("Length :", ll.length())
    print(ll.display())

    print("Deleted :", ll.remove_at(0))
    print("Deleted :", ll.remove_at(5))
    print("Length :", ll.length())
    print(ll.display())

    print("Deleted :", ll.remove_by_data("mango"))
    print("Deleted :", ll.remove_by_data("guava"))
    print("Length :", ll.length())
    print(ll.display())






# CIRCULAR LL IMPLEMENTATION
class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class CLL() :
    def __init__(self) :
        self.head = None
        self.count = 0   


# ISEMPTY CONDITION
    def isEmpty(self) :
        return self.count == 0
    
# GET LAST NODE
    def _get_last_node(self):
        last = self.head

        while last.next is not self.head:
            last = last.next

        return last
    

# DISPLAY
    def display(self) :
        if self.isEmpty() : return "CLL is Empty !"

        itr = self.head
        cllstr = 'head -->'
        while True :
            cllstr += str(itr.data) + '-->'
            itr = itr.next

            if itr is self.head :
                break

        cllstr += 'head'
        return cllstr 
        

# INSERT AT BEGINNING
    def insert_at_beginning(self,data) :
        node = Node(data)

        if self.isEmpty() :
            self.head = node
            node.next = self.head      # the node points to itself
        
        else :
            last = self._get_last_node()

            node.next = self.head
            last.next = node
            self.head = node

        self.count += 1
        return data
    

# INSERT AT END
    def insert_at_end(self,data) :
        node = Node(data)

        if self.isEmpty() :
            self.head = node
            node.next = self.head

        else :
            last = self._get_last_node()

            node.next = self.head
            last.next = node

        self.count += 1
        return data
    

# INSERT AT INDEX
    def insert_at(self,index,data) :
        if index < 0 or index > self.count : raise IndexError("Invalid Index !")
        
        if index == 0 : 
            self.insert_at_beginning(data)
            return data

        if index == self.count : 
            self.insert_at_end(data)
            return data
        
        itr = self.head

        for _ in range(index - 1):
            itr = itr.next

        node = Node(data)
        node.next = itr.next
        itr.next = node

        self.count += 1
        return data
    

# INSERT AFTER DATA
    def insert_after_data(self,data,data_to_insert) :
        if self.isEmpty() : raise Exception("CLL is Empty !")
        
        itr = self.head
        while True :
            if itr.data == data :
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node
                self.count += 1
                return data_to_insert

            itr = itr.next

            if itr is self.head : break

        raise ValueError("Data Not Found !")


# INSERT A LIST 
    def insert_a_list(self,data_list) :     # this function will erase the DLL and create a new DLL with this list
        self.head = None
        self.count = 0
        for data in data_list :
            self.insert_at_end(data)
        return data_list


# LENGHT
    def length(self) :
        return self.count
    

# REMOVE AT INDEX
    def remove_at(self,index) :
        if self.isEmpty() : raise Exception("CLL is Empty !")
        if index < 0 or index >= self.count : raise IndexError("Invalid Index !")

        if index == 0 :
            value = self.head.data
            if self.count == 1:
                self.head = None
            
            else :
                last = self._get_last_node()

                last.next = self.head.next
                self.head = self.head.next

        else :
            itr = self.head 
            for _ in range(index-1) :
                itr = itr.next

            value = itr.next.data
            itr.next = itr.next.next
            

        self.count -= 1
        return value
    

# REMOVE BY DATA
    def remove_by_data(self,data) :
        if self.isEmpty() : raise Exception("CLL is Empty !")
        if self.head.data == data :
            if self.count == 1 :
                self.head = None
            else :
                last = self._get_last_node()
                
                last.next = self.head.next
                self.head = self.head.next

            self.count -= 1
            return data
        
        itr = self.head
        while True :
            if itr.next.data == data :
                itr.next = itr.next.next
                self.count -= 1
                return data
            itr = itr.next

            if itr == self.head :
                break
         
        raise ValueError("Data Not Found !")
    
    def displayAI(self):
        if self.isEmpty():
            return "CLL is Empty!"

        elements = []

        itr = self.head
        while True:
            elements.append(str(itr.data))
            itr = itr.next

            if itr is self.head:
                break

        line1 = "Head"
        line2 = " ↓"
        line3 = " " + " → ".join(elements)

        # Length of the third line
        n = len(line3)

        # Bottom loop
        line4 = "↑" + " " * (n - 2) + "|"
        line5 = "└" + "─" * (n - 2) + "┘"

        return "\n".join([line1, line2, line3, line4, line5])
        

    
if __name__ == "__main__" :
    print("\nCICRULAR LL IMPLEMENTATION\n")
    cl = CLL() 
    print("inserted :", cl.insert_at_beginning(3))
    print("inserted :", cl.insert_at_beginning(2))
    print("inserted :", cl.insert_at_beginning(1))
    print("Lenght :",cl.length())
    print(cl.display())

    print("inserted :", cl.insert_at_end(4))
    print("inserted :", cl.insert_at_end(5))
    print("Lenght :",cl.length())
    print(cl.display())

    print("inserted :", cl.insert_at(0,100))
    print("inserted :", cl.insert_after_data(3,300))
    print("inserted :", cl.insert_after_data(100,400))
    print("Lenght :",cl.length())
    print(cl.display())

    print("inserted :", cl.insert_a_list(["banana","mango","grapes","orange","pineapple","guava","apple"]))
    print("Lenght :",cl.length())
    print(cl.display())

            
    print("Deleted :",cl.remove_at(0))
    print("Deleted :",cl.remove_at(5))
    print("Lenght :",cl.length())
    print(cl.display())

    print("Deleted :",cl.remove_by_data("mango"))
    print("Deleted :",cl.remove_by_data("guava"))
    print("Lenght :",cl.length())
    print(cl.display())


    print("inserted :", cl.insert_a_list(["banana","mango","grapes","orange","pineapple","guava","apple"]))
    print("Lenght :",cl.length())
    print(cl.displayAI())