# Priority Queue 

## 1. What is a Priority Queue?

A **Priority Queue** is an abstract data type where each element has an associated **priority**, and elements are served based on priority rather than insertion order.

- In a **Max Priority Queue** → the element with the **highest value** is dequeued first
- In a **Min Priority Queue** → the element with the **lowest value** is dequeued first

> A Priority Queue is **not a queue** in the traditional FIFO sense — it is ordered by priority, not by arrival time.

> **Key Use Cases:** CPU process scheduling, Dijkstra's shortest path, Prim's MST algorithm, Huffman encoding, Hospital emergency triage, Event-driven simulation

---

## 2. Regular Queue vs Priority Queue

### Regular Queue (FIFO)

Elements leave in the **same order** they entered — First In, First Out.

```
Enqueue: 5 → 3 → 8 → 1

Front → [ 5 | 3 | 8 | 1 ] ← Rear

Dequeue order: 5, 3, 8, 1     (insertion order)
```

### Priority Queue

Elements leave based on **priority**, regardless of insertion order.

```
Enqueue: 5, 3, 8, 1   (Max Priority Queue)

Internal Heap:      8
                   / \
                  5   3
                 /
                1

Dequeue order: 8, 5, 3, 1     (priority order — largest first)
```

### Comparison

| Feature              | Regular Queue          | Priority Queue                     |
|----------------------|------------------------|------------------------------------|
| Order of removal     | Insertion order (FIFO) | By priority (max or min)           |
| Underlying structure | Array / Linked List    | Heap (most efficient)              |
| Peek                 | Front element          | Highest/Lowest priority element    |
| Enqueue              | O(1)                   | O(log n)                           |
| Dequeue              | O(1)                   | O(log n)                           |

---

## 3. Priority Queue Implementation

A Priority Queue can be implemented using several data structures:

| Underlying Structure | Enqueue    | Dequeue    | Peek   | Notes                                      |
|----------------------|------------|------------|--------|--------------------------------------------|
| Unsorted Array       | O(1)       | O(n)       | O(n)   | Dequeue scans entire array for max/min     |
| Sorted Array         | O(n)       | O(1)       | O(1)   | Insertion keeps array sorted               |
| Unsorted Linked List | O(1)       | O(n)       | O(n)   | Same as unsorted array                     |
| Sorted Linked List   | O(n)       | O(1)       | O(1)   | Must find correct position on insert       |
| **Binary Heap**      | **O(log n)**| **O(log n)**| **O(1)** | **Best balance — used in practice**    |
| Fibonacci Heap       | O(1)       | O(log n)   | O(1)   | Theoretically optimal; complex to implement|

> **Binary Heap is the standard choice** — it gives O(log n) for both enqueue and dequeue, with O(1) peek, all in O(n) space.

---

## 4. Max Priority Queue vs Min Priority Queue

### Max Priority Queue

Uses a **Max Heap** internally. The largest element always sits at the root and is dequeued first.

```
Enqueue: [5, 9, 1, 8, 3, 6, 10, 4, 7, 2]

Internal Max Heap:

               10
             /    \
            9      6
           / \    / \
          8   3  5   1
         / \ /
        4  7 2

Dequeue order: 10 → 9 → 8 → 7 → 6 → 5 → 4 → 3 → 2 → 1
```

### Min Priority Queue

Uses a **Min Heap** internally. The smallest element always sits at the root and is dequeued first.

```
Enqueue: [5, 9, 1, 8, 3, 6, 10, 4, 7, 2]

Internal Min Heap:

               1
             /   \
            2     5
           / \   / \
          4   3 6  10
         / \ /
        8  7 9

Dequeue order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
```

### Comparison Table

| Feature                | Max Priority Queue         | Min Priority Queue          |
|------------------------|----------------------------|-----------------------------|
| Internal structure     | Max Heap                   | Min Heap                    |
| Heap property          | Parent ≥ Children          | Parent ≤ Children           |
| `peek()` returns       | Largest element            | Smallest element            |
| `dequeue()` returns    | Largest element            | Smallest element            |
| `sort()` returns       | Descending order           | Ascending order             |
| Common use case        | Job scheduling (high priority first) | Shortest path (smallest cost first) |

---

## 5. Implementation

### Algorithm

```
CLASS PriorityQueue:
    priority ← "max" or "min"    // determines which heap is used

    FUNCTION __init__(priority):
        IF priority == "max" → heap ← MaxHeap()
        IF priority == "min" → heap ← MinHeap()
        ELSE → RAISE ValueError

    // ── Core Operations ──────────────────────────────────────────
    FUNCTION enqueue(data):                             // O(log n)
        CALL heap.insert(data)

    FUNCTION dequeue():                                 // O(log n)
        IF priority == "max" → RETURN heap.extract_max()
        IF priority == "min" → RETURN heap.extract_min()

    FUNCTION peek():                                    // O(1)
        RETURN heap.peek()                // root of the internal heap

    // ── Queue Info ───────────────────────────────────────────────
    FUNCTION size():                                    // O(1)
        RETURN heap.heap_size()

    FUNCTION isEmpty():                                 // O(1)
        RETURN heap.isEmpty()

    // ── Search ───────────────────────────────────────────────────
    FUNCTION find(data):                                // O(n)
        RETURN heap.find(data)            // returns index or None

    FUNCTION contains(data):                            // O(n)
        RETURN heap.contains(data)        // returns True or False

    // ── Bulk Operations ──────────────────────────────────────────
    FUNCTION build_queue(elements):                     // O(n)
        CALL heap.build_heap(elements)    // Floyd's algorithm

    FUNCTION build_from_list(elements):                 // O(n log n)
        CALL heap.build_from_list(elements) // n individual inserts

    FUNCTION sort():                                    // O(n log n)
        RETURN heap.heap_sort()           // does NOT modify the queue

    // ── Utility ──────────────────────────────────────────────────
    FUNCTION display():                                 // O(n)
        CALL heap.display_list()
        CALL heap.display_tree()

    FUNCTION clear():                                   // O(1)
        CALL heap.clear()
```
---

## 7. Complexity of All Methods

### Time Complexity

| Method               | Time Complexity  | Explanation                                           |
|----------------------|------------------|-------------------------------------------------------|
| `enqueue(data)`      | **O(log n)**     | heap.insert() → heapify_up                            |
| `dequeue()`          | **O(log n)**     | heap.extract() → heapify_down                         |
| `peek()`             | **O(1)**         | Returns root — always at index 1                      |
| `size()`             | **O(1)**         | Returns `len(heap) - 1`                               |
| `isEmpty()`          | **O(1)**         | Checks if heap_size == 0                              |
| `find(data)`         | **O(n)**         | No ordering on siblings — must scan all nodes         |
| `contains(data)`     | **O(n)**         | Uses `find()` internally                              |
| `build_queue()`      | **O(n)**         | Floyd's algorithm — heapify_down from last non-leaf   |
| `build_from_list()`  | **O(n log n)**   | n individual enqueue calls                            |
| `sort()`             | **O(n log n)**   | n dequeue calls via heap_sort                         |
| `display()`          | **O(n)**         | Prints all n elements as list and tree                |
| `clear()`            | **O(1)**         | Resets internal heap to `[None]`                      |

### Space Complexity

| Method               | Space Complexity | Explanation                                           |
|----------------------|------------------|-------------------------------------------------------|
| Overall storage      | **O(n)**         | Internal heap array holds all n elements              |
| `enqueue()`          | **O(1)**         | No extra space beyond the new element                 |
| `dequeue()`          | **O(1)**         | In-place; one temp variable                           |
| `peek()`             | **O(1)**         | No allocation                                         |
| `find()`             | **O(1)**         | Single index variable                                 |
| `contains()`         | **O(1)**         | Delegates to find()                                   |
| `build_queue()`      | **O(1)**         | In-place Floyd's algorithm                            |
| `build_from_list()`  | **O(1)**         | Inserts one at a time; no extra buffer                |
| `sort()`             | **O(n)**         | Result list + temp copy of heap                       |
| `display()`          | **O(log n)**     | display_tree() uses recursive call stack              |
| `clear()`            | **O(1)**         | Resets to `[None]`                                    |

---

## 8. Extra — Important Notes & Real-World Context

### Why Heap is the Best Implementation for Priority Queue

| Property            | Explanation                                                       |
|---------------------|-------------------------------------------------------------------|
| O(log n) enqueue    | Heap insert is fast — just append and bubble up                  |
| O(log n) dequeue    | Heap extract is fast — replace root and bubble down              |
| O(1) peek           | Root is always the max or min — no searching needed              |
| O(n) build          | Floyd's algorithm builds a valid heap from any list in O(n)      |
| Memory efficient    | No pointers — stored as a flat array, cache-friendly             |

---

### Priority Queue vs Heap

| Aspect          | Heap                               | Priority Queue                         |
|-----------------|------------------------------------|----------------------------------------|
| What it is      | A concrete data structure          | An abstract data type (ADT)            |
| Defines         | How data is stored (array + rules) | What operations are available          |
| Operations      | insert, extract_max, heapify…      | enqueue, dequeue, peek                 |
| Relationship    | Heap **implements** Priority Queue | Priority Queue **uses** Heap           |

> A Priority Queue is the **interface**. A Heap is the **engine** underneath.

---

### Real-World Applications

| Application                   | Priority Type | Explanation                                          |
|-------------------------------|---------------|------------------------------------------------------|
| CPU Process Scheduling        | Max           | Highest-priority process gets CPU time first         |
| Dijkstra's Shortest Path      | Min           | Always process the node with the smallest known cost |
| Prim's MST Algorithm          | Min           | Always pick the edge with the smallest weight        |
| Huffman Encoding              | Min           | Merge two least-frequent characters first            |
| Hospital Emergency Triage     | Max           | Most critical patient treated first                  |
| Print Spooler                 | Max/Min       | Higher-priority documents print before others        |
| Event-Driven Simulation       | Min           | Always process the earliest scheduled event first    |

---

### Common Mistakes to Avoid

| Mistake                                      | Correct Approach                                              |
|----------------------------------------------|---------------------------------------------------------------|
| Passing priority other than "max" or "min"   | Constructor raises `ValueError` — validate before creating   |
| Assuming `sort()` modifies the queue         | `sort()` saves and restores the heap — queue is unchanged     |
| Using `find()` thinking it's O(log n)        | No ordering on siblings — PQ search is always O(n)           |
| Mixing up `build_queue` and `build_from_list`| `build_queue` is O(n); use it when all elements are known upfront |
| Calling `dequeue()` on an empty queue        | Always check `isEmpty()` first — raises Exception otherwise  |
| Assuming equal priorities maintain order     | Heap is not stable — equal values may not dequeue in FIFO order |

---

*The Priority Queue is only as efficient as its underlying heap. Always ensure the correct heap type (`MaxHeap` or `MinHeap`) is selected based on the problem requirement.*