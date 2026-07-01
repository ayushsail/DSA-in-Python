# QUEUE ARRAY IMPLEMENTATION
class QueueArr :
    def __init__ (self,size) :
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self) :
        return self.count == 0
    
    def isFull(self) :
        return self.count == self.size
    
    def enqueue(self,data) :
        if self.isFull() : raise Exception("Queue Overflow !")

        self.rear += 1
        self.arr[self.rear] = data
        self.count += 1
        return data
    
    def dequeue(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")

        self.front += 1
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.count -= 1
        return value
    
    def display(self) :
        if self.isEmpty() : return "Queue Underflow !"

        qstr = ''
        for i in range(self.front+1,self.rear+1) :
            qstr += str(self.arr[i]) + ' '
        
        return qstr

    def get_front(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.arr[self.front+1]
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.arr[self.rear]
    def get_size(self) :
        return self.count


if __name__ == "__main__" :
    print("QUEUE ARRAY IMPLEMENTATION\n")

    qa = QueueArr(5)

    print("Enqueued :",qa.enqueue(1))
    print("Enqueued :",qa.enqueue(2))
    print("Enqueued :",qa.enqueue(3))
    print("Enqueued :",qa.enqueue(4))
    print("Enqueued :",qa.enqueue(5))
    print(qa.display())
    print("front :", qa.get_front())
    print("rear :", qa.get_rear())
    print("no. of element :", qa.get_size())


    print("Dequeued :",qa.dequeue())
    print("Dequeued :",qa.dequeue())
    print(qa.display())
    print("front :", qa.get_front())
    print("rear :", qa.get_rear())
    print("no. of element :", qa.get_size())






# CIRCULAR QUEUE ARRAY IMPLEMENTATION
class CQueueArr :
    def __init__ (self,size) :
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self) :
        return self.count == 0
    
    def isFull(self) :
        return self.count == self.size
    
    def enqueue(self,data) :
        if self.isFull() : raise Exception("Queue Overflow !")

        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = data
        self.count += 1
        return data
    
    def dequeue(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")

        self.front = (self.front + 1) % self.size
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.count -= 1
        return value
    
    def display(self) :
        if self.isEmpty() : return "Queue Underflow !"

        qstr = ''
        current = (self.front + 1) % self.size
        for _ in range(self.count) :
            qstr += str(self.arr[current]) + ' '
            current = (current+1) % self.size
        
        return qstr

    def get_front(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.arr[(self.front+1) % self.size]
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.arr[self.rear]
    def get_size(self) :
        return self.count



if __name__ == "__main__" :
    print("\nCIRCULAR QUEUE ARRAY IMPLEMENTATION\n")

    cqa = CQueueArr(5)

    print("Enqueued :",cqa.enqueue(1))
    print("Enqueued :",cqa.enqueue(2))
    print("Enqueued :",cqa.enqueue(3))
    print("Enqueued :",cqa.enqueue(4))
    print("Enqueued :",cqa.enqueue(5))
    print(cqa.display())
    print(cqa.arr)

    print("Dequeued :",cqa.dequeue())
    print("Dequeued :",cqa.dequeue())
    print("Dequeued :",cqa.dequeue())
    print(cqa.display())
    print(cqa.arr)

    print("Enqueued :",cqa.enqueue(6))
    print("Enqueued :",cqa.enqueue(7))
    print("Enqueued :",cqa.enqueue(8))
    print(cqa.display())
    print(cqa.arr)

    print("Dequeued :",cqa.dequeue())
    print("Dequeued :",cqa.dequeue())
    print("Dequeued :",cqa.dequeue())
    print(cqa.display())
    print(cqa.arr)


    print("front :", cqa.get_front())
    print("rear :", cqa.get_rear())
    print("no. of element :", cqa.get_size())






# QUEUE LL IMPLEMENTATION
class Node :
    def __init__ (self,data) :
        self.data = data
        self.next = None

class QueueLL :
    def __init__(self) :
        self.count = 0
        self.front = None
        self.rear = None

    def isEmpty(self) :
        return self.count == 0
    
    def enqueue(self,data) :
        node = Node(data)
        if self.isEmpty() :
            self.front = self.rear = node

        else :
            self.rear.next = node
            self.rear = node

        self.count += 1
        return data

    def dequeue(self) :
        if self.isEmpty() : raise Exception("Queue Underflow")

        value = self.front.data
        self.front = self.front.next
        self.count -= 1

        if self.front == None :
            self.rear = None
        return value
    
    def display(self) :
        if self.isEmpty() : return "Queue Underflow"

        qstr = ''
        itr = self.front
        while itr :
            qstr += str(itr.data) + ' '
            itr = itr.next

        return qstr
    
    def get_front(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.front.data
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.rear.data
    def get_size(self) :
        return self.count
    

if __name__ == "__main__" :
    print("\nQUEUE LL IMPLEMENTATION\n")

    ql = QueueLL()
    print("Enqueued :", ql.enqueue(1))
    print("Enqueued :", ql.enqueue(2))
    print("Enqueued :", ql.enqueue(3))
    print("Enqueued :", ql.enqueue(4))
    print("Enqueued :", ql.enqueue(5))
    print(ql.display())
    print("front :", ql.get_front())
    print("rear :", ql.get_rear())
    print("no. of element :", ql.get_size())

    print("Dequeued :", ql.dequeue())
    print("Dequeued :", ql.dequeue())
    print(ql.display())
    print("front :", ql.get_front())
    print("rear :", ql.get_rear())
    print("no. of element :", ql.get_size())
            





# CIRCULAR QUEUE LL IMPLEMENTATION
class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class CQueueLL :
    def __init__(self) :
        self.front = None
        self.rear = None
        self.count = 0


    def isEmpty(self) :
        return self.count == 0
    

    def enqueue(self,data) :
        node = Node(data)
        if self.isEmpty() :
            self.front = node
            self.rear = node
            self.rear.next = self.front
        
        else :
            node.next = self.front
            self.rear.next = node
            self.rear = node
        
        self.count += 1
        return data
    

    def dequeue(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")

        value = self.front.data

        if self.count == 1 :
            self.front = None
            self.rear = None

        else :
            self.rear.next = self.front.next
            self.front = self.front.next

        self.count -= 1
        return value


    def display(self) :
        if self.isEmpty() : return "Queue Underflow !"

        itr = self.front
        cqstr = ''
        for _ in range(self.count) :
            cqstr += str(itr.data) + ' '
            itr = itr.next
        
        return cqstr
    
    def get_front(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.front.data
    def get_rear(self) :
        if self.isEmpty() : raise Exception("Queue Underflow !")
        return self.rear.data
    def get_size(self) :
        return self.count
        
if __name__ == "__main__" :
    print("\nCIRCULAR QUEUE LL IMPLEMENTATION\n")
    cql = CQueueLL() 
    print("Enqueued :", cql.enqueue(1))
    print("Enqueued :", cql.enqueue(2))
    print("Enqueued :", cql.enqueue(3))
    print("Enqueued :", cql.enqueue(4))
    print("Enqueued :", cql.enqueue(5))
    print(cql.display())
    print("front :", cql.get_front())
    print("rear :", cql.get_rear())
    print("no. of element :", cql.get_size())
        

    print("Dequeued :", cql.dequeue())
    print("Dequeued :", cql.dequeue())
    print("Dequeued :", cql.dequeue())
    print(cql.display())
    print("front :", cql.get_front())
    print("rear :", cql.get_rear())
    print("no. of element :", cql.get_size())






# QUEUE IMPLEMENTATION USING CLASS COLLECTION.DEQUE 
# this is the recommended way in python
# deques are generalization of stack & queues   
# deques are implemented using doubly LL
from collections import deque

class Queue :

    def __init__(self) :
        self.buffer = deque()

    def enqueue(self,data) :
        self.buffer.appendleft(data)

    def dequeue(self) :
        return self.buffer.pop()
    
    def display(self) :
        return self.buffer
    
    def isEmpty(self) :
        return len(self.buffer) == 0
    
    def size(self) :
        return len(self.buffer)

if __name__ == "__main__" :
    print("\nQUEUE USING COLLECTION.DEQUE\n")

    q = Queue()

    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.04 AM',
        'price': 136
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.05 AM',
        'price': 131
    })

    print(q.display())
    print("No. of elements :", q.size())

    print("Dequeued :", q.dequeue())
    print("Dequeued :", q.dequeue())
    print(q.display())
    print("No. of elements :", q.size())



    # print(dir(q.buffer))       # this will show you all the methods
 