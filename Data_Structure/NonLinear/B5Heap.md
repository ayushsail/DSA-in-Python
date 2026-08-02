# Heap Data Structure — Complete Guide

---

## 1. What is a Heap?

A **Heap** is a specialized **complete binary tree** that satisfies the **heap property**:

- In a **Max Heap** → every parent node is **greater than or equal to** its children
- In a **Min Heap** → every parent node is **less than or equal to** its children

Heaps are **not fully sorted** — they only guarantee the root is the max (or min). The rest of the tree is partially ordered.

> **Key Use Cases:** Priority Queues, Heap Sort, Dijkstra's Shortest Path, Task Scheduling, Median Finding

---

## 2. Prerequisite — Binary Tree Concepts

### Full Binary Tree

A binary tree where every node has either **0 or 2 children** — never just 1.

```
        1
       / \
      2   3
     / \
    4   5
```
✅ Full Binary Tree

```
        1
       /
      2
     /
    4
```
❌ Not Full (node 2 has only 1 child)

---

### Complete Binary Tree

A binary tree where:
1. **All levels are fully filled** except possibly the last
2. The last level has all nodes **as far left as possible**

```
          1
        /   \
       2     3
      / \   /
     4   5 6
```
✅ Complete Binary Tree — last level fills left to right

```
          1
        /   \
       2     3
      / \     \
     4   5     6
```
❌ Not Complete — node 6 is on the right without a left sibling

> **Why it matters:** A heap is always a complete binary tree. This property allows it to be stored efficiently in an **array** without any pointers.

---

### Array Representation of a Complete Binary Tree

For a node at index `i` (1-based indexing):

| Relation       | Formula        |
|----------------|----------------|
| Parent         | `i // 2`       |
| Left Child     | `i * 2`        |
| Right Child    | `i * 2 + 1`    |
| Root           | index `1`      |

```
Tree:          10
              /  \
             9    8
            / \  /
           7  6 5

Array: [None, 10, 9, 8, 7, 6, 5]
Index:    0    1  2  3  4  5  6
```

`None` at index 0 is a placeholder so that the parent/child formulas work cleanly with 1-based indexing.

---

## 3. Max Heap vs Min Heap

### Max Heap

Every parent node is **greater than or equal to** its children.
The **maximum element is always at the root** (index 1).

```
          10
        /    \
       9      8
      / \    / \
     7   6  5   4
```

**Max Heap Property:** `heap[parent] >= heap[child]` for all nodes

---

### Min Heap

Every parent node is **less than or equal to** its children.
The **minimum element is always at the root** (index 1).

```
          1
        /   \
       3     2
      / \   / \
     7   5 8   4
```

**Min Heap Property:** `heap[parent] <= heap[child]` for all nodes

---

### Comparison Table

| Feature                   | Max Heap                              | Min Heap                               |
|---------------------------|---------------------------------------|----------------------------------------|
| Root element              | Maximum value                         | Minimum value                          |
| Heap property             | Parent ≥ Children                     | Parent ≤ Children                      |
| `peek()` returns          | Largest element                       | Smallest element                       |
| Common use case           | Heap sort (descending)                | Priority queue (lowest priority first) |
| Python built-in (`heapq`) | Not directly (negate values)          | ✅ Default behavior                    |

---

## 4. Implementation

### Max Heap — Algorithm

```
CLASS MaxHeap:
    heap ← [None]       // 1-based indexing; index 0 unused

    // ── Helper Methods ──────────────────────────────────────
    FUNCTION parent(index):
        RETURN index // 2

    FUNCTION left_child(index):
        RETURN index * 2

    FUNCTION right_child(index):
        RETURN index * 2 + 1

    FUNCTION has_parent(index):
        RETURN index > 1

    FUNCTION has_left(index):
        RETURN left_child(index) <= heap_size()

    FUNCTION has_right(index):
        RETURN right_child(index) <= heap_size()

    FUNCTION heap_size():
        RETURN length(heap) - 1

    FUNCTION isEmpty():
        RETURN heap_size() == 0

    FUNCTION swap(i, j):
        heap[i], heap[j] ← heap[j], heap[i]

    // ── Peek ────────────────────────────────────────────────
    FUNCTION peek():                                    // O(1)
        IF isEmpty() → RAISE Exception
        RETURN heap[1]

    // ── Insert ──────────────────────────────────────────────
    FUNCTION insert(data):                              // O(log n)
        APPEND data to heap
        CALL heapify_up(heap_size())

    // ── Extract Max ─────────────────────────────────────────
    FUNCTION extract_max():                             // O(log n)
        IF isEmpty() → RAISE Exception
        max_val ← heap[1]
        IF heap_size() == 1:
            REMOVE last element
            RETURN max_val
        heap[1] ← REMOVE last element of heap
        CALL heapify_down(1)
        RETURN max_val

    // ── Heapify Up ──────────────────────────────────────────
    FUNCTION heapify_up(index):                         // O(log n)
        WHILE has_parent(index):
            p ← parent(index)
            IF heap[index] > heap[p]:
                CALL swap(index, p)
                index ← p
            ELSE:
                BREAK

    // ── Heapify Down ────────────────────────────────────────
    FUNCTION heapify_down(index):                       // O(log n)
        WHILE has_left(index):
            largest ← index
            left ← left_child(index)
            IF heap[left] > heap[largest]:
                largest ← left
            IF has_right(index):
                right ← right_child(index)
                IF heap[right] > heap[largest]:
                    largest ← right
            IF index == largest:
                BREAK
            CALL swap(index, largest)
            index ← largest

    // ── Utility ─────────────────────────────────────────────
    FUNCTION find(data):                                // O(n)
        FOR i FROM 1 TO heap_size():
            IF heap[i] == data → RETURN i
        RETURN None

    FUNCTION contains(data):                            // O(n)
        RETURN find(data) IS NOT None

    FUNCTION clear():                                   // O(1)
        heap ← [None]
```

---

### Min Heap — Algorithm

The Min Heap is structurally identical to Max Heap. The **only difference** is in the comparison inside `heapify_up` and `heapify_down` — reversed to always keep the smallest element at the root.

```
CLASS MinHeap:
    heap ← [None]       // 1-based indexing; index 0 unused

    // ── Helper Methods ──────────────────────────────────────
    // (same as MaxHeap — parent, left_child, right_child,
    //  has_parent, has_left, has_right, heap_size, isEmpty, swap)

    // ── Peek ────────────────────────────────────────────────
    FUNCTION peek():                                    // O(1)
        IF isEmpty() → RAISE Exception
        RETURN heap[1]                // returns MINIMUM element

    // ── Insert ──────────────────────────────────────────────
    FUNCTION insert(data):                              // O(log n)
        APPEND data to heap
        CALL heapify_up(heap_size())

    // ── Extract Min ─────────────────────────────────────────
    FUNCTION extract_min():                             // O(log n)
        IF isEmpty() → RAISE Exception
        min_val ← heap[1]
        IF heap_size() == 1:
            REMOVE last element
            RETURN min_val
        heap[1] ← REMOVE last element of heap
        CALL heapify_down(1)
        RETURN min_val

    // ── Heapify Up (comparison FLIPPED vs MaxHeap) ──────────
    FUNCTION heapify_up(index):                         // O(log n)
        WHILE has_parent(index):
            p ← parent(index)
            IF heap[index] < heap[p]:       // ← LESS THAN (flipped)
                CALL swap(index, p)
                index ← p
            ELSE:
                BREAK

    // ── Heapify Down (comparison FLIPPED vs MaxHeap) ────────
    FUNCTION heapify_down(index):                       // O(log n)
        WHILE has_left(index):
            smallest ← index               // ← track SMALLEST (flipped)
            left ← left_child(index)
            IF heap[left] < heap[smallest]:
                smallest ← left
            IF has_right(index):
                right ← right_child(index)
                IF heap[right] < heap[smallest]:
                    smallest ← right
            IF index == smallest:
                BREAK
            CALL swap(index, smallest)
            index ← smallest

    // ── Utility ─────────────────────────────────────────────
    // (same as MaxHeap — find, contains, clear)
```

> **Summary of differences:**
> | Method         | Max Heap          | Min Heap          |
> |----------------|-------------------|-------------------|
> | `heapify_up`   | `child > parent`  | `child < parent`  |
> | `heapify_down` | track `largest`   | track `smallest`  |
> | `extract`      | returns maximum   | returns minimum   |

---

## 5. Heapify Up & Heapify Down — In Depth

These are the two core operations that maintain the heap property after every insertion or deletion.

---

### Heapify Up (Bubble Up / Sift Up)

**When used:** After **inserting** a new element (added at the last position).

**Goal:** Move the newly inserted element **upward** until the heap property is restored.

**Steps:**
1. Add the new element at the end of the heap array
2. Compare it with its parent
3. If it violates the heap property → **swap** with parent
4. Repeat from the new position until the root or no violation

**Max Heap Example — Insert `15`:**

```
Before insert:          After append 15:        After heapify up:
       10                     10                       15
      /  \                   /  \                     /  \
     9    8       →         9    8         →         10    8
    / \                    / \ /                    / \ /
   7   6                  7  6 15                  7  6 9
```

```
Step 1: 15 added at end (index 6)
Step 2: parent(6) = 3 → heap[3] = 8,  15 > 8  → SWAP
Step 3: now at index 3, parent(3) = 1 → heap[1] = 10, 15 > 10 → SWAP
Step 4: now at index 1 (root) → STOP
```

```python
def heapify_up(self, index):
    while self.has_parent(index):
        p = self.parent(index)
        if self.heap[index] > self.heap[p]:   # Max Heap condition
            self.swap(index, p)
            index = p
        else:
            break
```

**Time Complexity:** O(log n) — at most travels the height of the tree

---

### Heapify Down (Bubble Down / Sift Down)

**When used:** After **extracting** the root (the root is replaced by the last element).

**Goal:** Move the misplaced root element **downward** until the heap property is restored.

**Steps:**
1. Replace root with the last element, remove the last element
2. Compare root with both children
3. Swap with the **largest** child (Max Heap) if it's larger than the current node
4. Repeat from the swapped position until a leaf or no violation

**Max Heap Example — Extract max (`10`), replace with `6`:**

```
Before extract:         After replace root:     After heapify down:
       10                     6                        9
      /  \                   / \                      / \
     9    8       →         9   8          →         6   8
    / \                    / \                      /
   7   6                  7   (removed)            7
```

```
Step 1: root = 6, children are 9 and 8
Step 2: largest child = 9 (index 2), 9 > 6 → SWAP
Step 3: now at index 2, left child = 7 (index 4), no right child
Step 4: 7 > 6 → SWAP
Step 5: now at index 4, no children → STOP
```

```python
def heapify_down(self, index):
    while self.has_left(index):
        largest = index
        left = self.left_child(index)
        if self.heap[left] > self.heap[largest]:
            largest = left
        if self.has_right(index):
            right = self.right_child(index)
            if self.heap[right] > self.heap[largest]:
                largest = right
        if index == largest:    # already in correct position
            break
        self.swap(index, largest)
        index = largest
```

**Time Complexity:** O(log n) — at most travels the height of the tree

---

### Heapify Up vs Heapify Down

| Aspect               | Heapify Up                     | Heapify Down                       |
|----------------------|--------------------------------|------------------------------------|
| Triggered by         | `insert()`                     | `extract_max()` / `extract_min()`  |
| Direction            | Child → Root                   | Root → Leaf                        |
| Comparisons per step | 1 (with parent only)           | 2 (with both children)             |
| Time Complexity      | O(log n)                       | O(log n)                           |
| Path length          | Height of tree                 | Height of tree                     |

---

## 6. Build Heap — O(n) Explained

A naive approach of inserting `n` elements one by one costs **O(n log n)**.

`build_heap()` is smarter — it starts from the **last non-leaf node** and heapifies down each node, achieving **O(n)** overall.

### Algorithm

```
FUNCTION build_heap(elements):                          // O(n)
    heap ← [None] + elements
    start ← heap_size() // 2      // last non-leaf node index
    FOR i FROM start DOWN TO 1:
        CALL heapify_down(i)
```

**Why start from `heap_size // 2`?**
All nodes after index `heap_size // 2` are **leaf nodes** — they trivially satisfy the heap property on their own. We only need to heapify internal nodes.

### Code

```python
def build_heap(self, elements):
    self.heap = [None] + elements
    # Last non-leaf is at index: heap_size // 2
    for i in range(self.heap_size() // 2, 0, -1):
        self.heapify_down(i)
```

**Why O(n)?**
- Most nodes are near the bottom — they travel very few levels down
- Mathematically: the sum of all downward paths across all nodes = O(n), not O(n log n)

```
Input: [5, 9, 1, 8, 3, 6, 10, 4, 7, 2]

Array:  [None, 5, 9, 1, 8, 3, 6, 10, 4, 7, 2]
Start heapifying from index 5 (heap_size // 2) down to index 1

Final Max Heap: [None, 10, 9, 6, 8, 3, 5, 1, 4, 7, 2]
```

---

## 7. Heap Sort — Algorithm

Heap Sort uses a Max Heap to sort an array in **ascending order** in two phases.

### Phase 1 — Build a Max Heap

Convert the input array into a valid Max Heap using Floyd's algorithm.

### Phase 2 — Extract Max Repeatedly

Swap the root (maximum) with the last element, shrink the heap by 1, then heapify down the new root. Repeating this places elements in sorted order from right to left.

### Algorithm

```
FUNCTION heap_sort(arr):                                // O(n log n)

    // Phase 1: Build Max Heap from input array
    n ← length(arr)
    FOR i FROM (n // 2 - 1) DOWN TO 0:                 // O(n)
        CALL heapify_down(arr, n, i)

    // Phase 2: Extract max element one by one
    FOR i FROM (n - 1) DOWN TO 1:                      // O(n log n)
        SWAP arr[0] WITH arr[i]           // move current max to end
        CALL heapify_down(arr, i, 0)     // heapify the reduced heap (size = i)

    RETURN arr                            // sorted in ascending order


FUNCTION heapify_down(arr, heap_size, index):           // O(log n)
    largest ← index
    left    ← 2 * index + 1              // 0-based indexing
    right   ← 2 * index + 2

    IF left < heap_size AND arr[left] > arr[largest]:
        largest ← left

    IF right < heap_size AND arr[right] > arr[largest]:
        largest ← right

    IF largest ≠ index:
        SWAP arr[index] WITH arr[largest]
        CALL heapify_down(arr, heap_size, largest)
```

### Step-by-step Trace

```
Input:  [4, 10, 3, 5, 1]

Phase 1 — Build Max Heap:
  → [10, 5, 3, 4, 1]

Phase 2 — Extract max repeatedly:
  Step 1: Swap 10 ↔ 1  → [1, 5, 3, 4, | 10]  → heapify → [5, 4, 3, 1, | 10]
  Step 2: Swap 5  ↔ 1  → [1, 4, 3, | 5, 10]  → heapify → [4, 1, 3, | 5, 10]
  Step 3: Swap 4  ↔ 3  → [3, 1, | 4, 5, 10]  → heapify → [3, 1, | 4, 5, 10]
  Step 4: Swap 3  ↔ 1  → [1, | 3, 4, 5, 10]  → done

Output: [1, 3, 4, 5, 10]   ✅ Sorted ascending
```

### Properties

| Property        | Value                                              |
|-----------------|----------------------------------------------------|
| Time Complexity | O(n log n) — guaranteed; no worst-case like Quick Sort |
| Space Complexity| O(1) — fully in-place                              |
| Stable?         | ❌ Not stable — equal elements may reorder          |
| Cache-friendly? | ❌ No — jumps around in the array                  |

---

## 8. Complexity of All Methods

### Time Complexity

| Method              | Time Complexity | Explanation                                              |
|---------------------|-----------------|----------------------------------------------------------|
| `peek()`            | **O(1)**        | Root is always at index 1                                |
| `insert(data)`      | **O(log n)**    | Append O(1) + heapify_up O(log n)                        |
| `extract_max/min()` | **O(log n)**    | Remove root O(1) + heapify_down O(log n)                 |
| `heapify_up()`      | **O(log n)**    | Travels at most the height of the tree                   |
| `heapify_down()`    | **O(log n)**    | Travels at most the height of the tree                   |
| `build_heap()`      | **O(n)**        | Floyd's algorithm — smarter than n insertions            |
| `build_from_list()` | **O(n log n)**  | n individual inserts, each O(log n)                      |
| `heap_sort()`       | **O(n log n)**  | n extract_max calls, each O(log n)                       |
| `find(data)`        | **O(n)**        | No ordering guarantee — must scan all elements           |
| `contains(data)`    | **O(n)**        | Uses `find()` internally                                 |
| `heap_size()`       | **O(1)**        | Returns `len(self.heap) - 1`                             |
| `isEmpty()`         | **O(1)**        | Checks heap size                                         |
| `clear()`           | **O(1)**        | Resets heap to `[None]`                                  |
| `swap(i, j)`        | **O(1)**        | Python tuple unpacking                                   |

### Space Complexity

| Method              | Space Complexity | Explanation                                             |
|---------------------|------------------|---------------------------------------------------------|
| Overall storage     | **O(n)**         | Array stores all n elements                             |
| `insert()`          | **O(1)**         | No extra space beyond the element added                 |
| `extract_max/min()` | **O(1)**         | In-place; only one temp variable                        |
| `heapify_up()`      | **O(1)**         | Iterative — no recursion stack                          |
| `heapify_down()`    | **O(1)**         | Iterative — no recursion stack                          |
| `build_heap()`      | **O(1)**         | In-place heapify (input array reused)                   |
| `heap_sort()`       | **O(1)**         | Fully in-place if done directly on input array          |
| `find()`            | **O(1)**         | Single index variable                                   |
| `display_tree()`    | **O(log n)**     | Recursive call stack depth = tree height                |

---

## 9. Extra — Important Notes & Interview Tips

### Why is a Heap stored as an Array (not a Tree with Nodes)?

1. **No pointer overhead** — saves memory (no `left`, `right`, `parent` pointers)
2. **Cache-friendly** — contiguous memory = faster access
3. **Index math is O(1)** — parent/child navigation is just arithmetic
4. **Possible only because heaps are complete binary trees** — no gaps in the array

---

### Heap vs BST

| Feature                | Heap                               | Binary Search Tree (BST)           |
|------------------------|------------------------------------|-------------------------------------|
| Ordering               | Partial (only parent > children)   | Full (left < root < right)          |
| Find min/max           | O(1)                               | O(log n) for balanced BST           |
| Search any element     | O(n)                               | O(log n) for balanced BST           |
| Insert                 | O(log n)                           | O(log n) for balanced BST           |
| Structure guarantee    | Always complete binary tree        | Can become unbalanced → O(n)        |
| Use case               | Priority Queue, sorting            | Searching, ordered traversal        |

---

### Priority Queue using Heap — Algorithm

A **Priority Queue** is the most common real-world application of a heap. Each element has an associated **priority**, and the element with the highest (or lowest) priority is always served first.

```
CLASS PriorityQueue:
    heap ← []     // stores (priority, data) pairs as a Min Heap
                  // lower priority number = higher urgency

    FUNCTION enqueue(priority, data):               // O(log n)
        item ← (priority, data)
        APPEND item to heap
        CALL heapify_up(last index)

    FUNCTION dequeue():                             // O(log n)
        IF isEmpty() → RAISE Exception
        top ← heap[0]                   // highest priority item
        heap[0] ← REMOVE last item of heap
        CALL heapify_down(0)
        RETURN top

    FUNCTION peek():                                // O(1)
        IF isEmpty() → RAISE Exception
        RETURN heap[0]                  // return without removing

    FUNCTION isEmpty():                             // O(1)
        RETURN length(heap) == 0


// ── Example Trace ──────────────────────────────────────────────
enqueue(3, "Low priority task")    → heap: [(3, "Low...")]
enqueue(1, "Urgent task")         → heap: [(1, "Urgent"), (3, "Low...")]
enqueue(2, "Medium task")         → heap: [(1, "Urgent"), (3, "Low..."), (2, "Medium")]

dequeue() → returns (1, "Urgent task")
dequeue() → returns (2, "Medium task")
dequeue() → returns (3, "Low priority task")
```

**Key Insight:**
- Use a **Min Heap** when lower number = higher priority (most common)
- Use a **Max Heap** when higher number = higher priority
- Python's `heapq` is a Min Heap by default — negate values for Max Heap behaviour

**Real-world uses of Priority Queue:**
- OS process scheduling (CPU assigns time to highest-priority process)
- Dijkstra's shortest path (always process the closest unvisited node)
- Hospital emergency triage (most critical patient first)
- Event simulation (process earliest event first)

---

### Common Mistakes to Avoid

| Mistake                                   | Correct Approach                                          |
|-------------------------------------------|-----------------------------------------------------------|
| Using 0-based indexing without adjusting  | Use 1-based indexing OR adjust parent/child formulas      |
| Forgetting `[None]` placeholder           | Always initialize heap as `[None]` for 1-based indexing  |
| Calling `heapify_up` after build_heap     | `build_heap` uses `heapify_down` only — that's correct    |
| Assuming heap is fully sorted             | Heap only guarantees root is max/min                      |
| Using `find()` thinking it's O(log n)`    | Heap search is always O(n) — no ordering on siblings      |
| Forgetting to restore heap after sort     | Save `temp = self.heap.copy()` before extracting          |

---

### Quick Summary

```
Heap
 ├── Complete Binary Tree stored as Array
 ├── Max Heap → root is maximum   (parent >= children)
 ├── Min Heap → root is minimum   (parent <= children)
 │
 ├── Core Operations
 │    ├── insert()       → append + heapify_up    → O(log n)
 │    ├── extract()      → swap root with last
 │    │                     + pop last
 │    │                     + heapify_down         → O(log n)
 │    └── peek()         → return heap[1]          → O(1)
 │
 ├── Build Heap          → Floyd's algorithm       → O(n)
 ├── Heap Sort           → n × extract             → O(n log n)
 ├── Priority Queue      → enqueue/dequeue via heap → O(log n)
 └── Search              → linear scan             → O(n)
```

---

*For Python code implementation of Max Heap, refer to your `MaxHeap` class. The algorithms above map directly to those methods.*