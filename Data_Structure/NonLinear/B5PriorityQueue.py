from B5MaxHeap import MaxHeap              # for priority = "max"
from B5MinHeap import MinHeap              # for priority = "min"


class PriorityQueue :
    def __init__ (self, priority = "max") :
        self.priority = priority.lower()            # store it in lower case character

        if self.priority == "max" :
            self.heap = MaxHeap()

        elif self.priority == "min" :
            self.heap = MinHeap()

        else : raise ValueError("Priority must be 'max' or 'min'")

    def __str__(self):
        return str(self.heap)

    __repr__ = __str__


    def enqueue(self,data) :
        self.heap.insert(data)

    def dequeue(self) :
        if self.priority == "max" : return self.heap.extract_max()
        else : return self.heap.extract_min()

    def peek(self) : return self.heap.peek()

    def display(self) :
        self.heap.display_list()
        self.heap.display_tree()

    def size(self) : return self.heap.heap_size()

    def isEmpty(self) : return self.heap.isEmpty()

    def find(self,data) : return self.heap.find(data)

    def contains(self,data) : return self.heap.contains(data)

    def sort(self) : return self.heap.heap_sort()

    def build_queue(self,elements) : return self.heap.build_heap(elements)

    def build_from_list(self,elements) : return self.heap.build_from_list(elements)

    def clear(self) : self.heap.clear()


if __name__ == "__main__":

    print("=" * 60)
    print("MAX PRIORITY QUEUE")
    print("=" * 60)

    max_pq = PriorityQueue("max")
    max_pq.build_queue([5, 9, 1, 8, 3, 6, 10, 4, 7, 2])

    print("\nDisplay Queue")
    max_pq.display()

    print("\nPeek :", max_pq.peek())

    print("Size :", max_pq.size())

    print("Is Empty :", max_pq.isEmpty())

    print("Find 7 :", max_pq.find(7))

    print("Contains 15 :", max_pq.contains(15))

    print("\nEnqueue 15")
    max_pq.enqueue(15)
    max_pq.display()

    print("\nDequeue :", max_pq.dequeue())
    max_pq.display()

    print("\nSorted Queue :", max_pq.sort())

    print("\nQueue after sorting (should remain unchanged)")
    max_pq.display()

    print("\nClearing Queue...")
    max_pq.clear()

    print("Is Empty :", max_pq.isEmpty())






    print("\n\n" + "=" * 60)
    print("MIN PRIORITY QUEUE")
    print("=" * 60)

    min_pq = PriorityQueue("min")
    min_pq.build_queue([5, 9, 1, 8, 3, 6, 10, 4, 7, 2])

    print("\nDisplay Queue")
    min_pq.display()

    print("\nPeek :", min_pq.peek())

    print("Size :", min_pq.size())

    print("Is Empty :", min_pq.isEmpty())

    print("Find 7 :", min_pq.find(7))

    print("Contains 15 :", min_pq.contains(15))

    print("\nEnqueue 0")
    min_pq.enqueue(0)
    min_pq.display()

    print("\nDequeue :", min_pq.dequeue())
    min_pq.display()

    print("\nSorted Queue :", min_pq.sort())

    print("\nQueue after sorting (should remain unchanged)")
    min_pq.display()

    print("\nClearing Queue...")
    min_pq.clear()

    print("Is Empty :", min_pq.isEmpty())