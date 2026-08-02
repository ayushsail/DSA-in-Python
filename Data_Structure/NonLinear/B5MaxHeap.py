class MaxHeap :
    def __init__(self) :
        self.heap = [None]

    def __str__(self):
        return str(self.heap)

    __repr__ = __str__


# DISPLAY LIST
    def display_list(self) :
        if self.isEmpty() : raise Exception("Heap is Empty !")
        print("Heap list : ",self.heap[1:])


# DISPLAY TREE
    def display_tree(self, index=1,  level=0) :
        if self.isEmpty() : raise Exception("Heap is Empty !")

        if self.has_right(index) : self.display_tree(self.right_child(index),level+1)

        space = '     ' * level
        print(space + str(self.heap[index]))

        if self.has_left(index) : self.display_tree(self.left_child(index),level+1)



# HELPER METHODS
    def parent(self,index) :
        return index // 2

    def left_child(self,index) :
        return index * 2

    def right_child(self,index) :
        return index * 2 + 1

    def has_parent(self,index) :
        return index > 1

    def has_left(self,index) :
        return self.left_child(index) <= self.heap_size()

    def has_right(self,index) :
        return self.right_child(index) <= self.heap_size()

    def heap_size(self) :
        return len(self.heap) - 1

    def isEmpty(self) :
        return self.heap_size() == 0 

    def peek(self) :
        if self.isEmpty() : raise Exception("Heap is Empty !")
        return self.heap[1]
    
    def swap(self,i,j) :
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        # # it is same like this : 
        # # value = self.heap[i]
        # # self.heap[i] = self.heap[j]
        # # self.heap[j] = value


# HEAPIFY UP
    def heapify_up(self,index) :
        while self.has_parent(index) :
            parent_index = self.parent(index)
            
            if self.heap[index] > self.heap[parent_index]  :
                self.swap(index,parent_index)
                index = parent_index
            else :
                break


# HEAPIFY DOWN
    def heapify_down(self,index) :
        while self.has_left(index) :
            largest = index

            left_index = self.left_child(index)
            if self.heap[left_index] > self.heap[largest] : largest = left_index

            if self.has_right(index) : 
                right_index = self.right_child(index)
                if self.heap[right_index] > self.heap[largest] : largest = right_index

            if index == largest :           # duplicates are allowed in heap
                break
            else :
                self.swap(index,largest)
                index = largest


# INSERT
    def insert(self,data) :
        self.heap.append(data)
        self.heapify_up(self.heap_size())


# EXTRACT MAX - DELETE ROOT
    def extract_max(self) :
        if self.isEmpty() : raise Exception("Heap is Empty !!")

        max_val = self.heap[1]

        if self.heap_size() == 1 :
            self.heap.pop()
            return max_val

        last = self.heap.pop()
        self.heap[1] = last

        self.heapify_down(1)

        return max_val

    
# BUILD HEAP
    def build_heap(self,elements) :
        self.heap = [None] + elements
        for i in range(self.heap_size()//2,0,-1) :
            self.heapify_down(i)


# BUILD FROM LIST
    def build_from_list(self,elements) :
        self.heap = [None]
        for element in elements :
            self.insert(element)


# HEAP SORT
    def heap_sort(self) :
        temp_heap = self.heap.copy()
        result = []

        while not self.isEmpty() :
            val = self.extract_max()
            result.append(val)

        self.heap = temp_heap

        result.reverse()
        return result


# UTILITY METHODS
    def find(self,data) :
        for i in range(1,self.heap_size()+1) :
            if self.heap[i] == data :
                return i
        return None

    def contains(self,data) :
        return self.find(data) is not None

    def clear(self) :
        self.heap = [None]




if __name__ == "__main__" :
    h = MaxHeap()
    h.build_heap([5, 9, 1, 8, 3, 6, 10, 4, 7, 2])
    h.display_list()
    h.display_tree()
    print("\nSorted Heap : ", h.heap_sort())

    print("\nExtracted element : ", h.extract_max())
    h.display_list()
    h.display_tree()
    print("\nSorted Heap : ", h.heap_sort())

    print("\nExtracted element : ", h.extract_max())
    h.display_list()
    h.display_tree()

    print("\nSorted Heap : ", h.heap_sort())
