class Node :
    def __init__(self,data,next) :
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self) :
        self.head = None

    def display(self) :
        if self.head is None :
            print("LL is Empty")
            return

        itr = self.head
        llstr = ''

        while itr :
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
    

    def insert_at_begining(self,data) :
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data) :
        if self.head is None :
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next :
            itr = itr.next
        
        itr.next = Node(data,itr.next)

    def insert_at(self,index,data) :
        if index < 0 or index >self.len_of_ll() :
            raise Exception("Invalid Index")
        
        if index == 0 :
            self.insert_at_begining(data)
        
        if index == self.len_of_ll() - 1 :
            self.insert_at_end(data)

        itr = self.head
        count = 0

        while itr :
            if count == index - 1 :
                itr.next = Node(data,itr.next)
                break

            count += 1
            itr = itr.next

    def insert_a_list(self,data_list) :
        self.head = None
        for data in data_list :
            self.insert_at_end(data)


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
    
    def remove_at(self,index) :
        if index < 0 or index > self.len_of_ll() :
            raise Exception("Invalid Index")
        
        if index == 0 :
            self.head = self.head.next
        
        itr = self.head
        count = 0
        while itr :
            if count == index - 1 :
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next


ll = LinkedList()
ll.insert_at_begining(1)
ll.insert_at_begining(2)
ll.insert_at_end(3)
ll.display()
print("Length of LL : ",ll.len_of_ll())
