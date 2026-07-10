# Doubly Linked List

## What is DLL?

A Doubly Linked List is a Linked List where every node stores:
1. Previous Node Address
2. Data
3. Next Node Address

## Visualization
NULL ←→ 10 ←→ 20 ←→ 30 ←→ NULL


## Advantages of DLL
* Traverse forward and backward
* Easier deletion
* Easier insertion before a node

## Disadvantages
* Extra memory for previous pointer
* More pointer updates


### Visualization

```text
NULL ←→ 10 ←→ 20 ←→ 30 ←→ NULL
```

---

# Doubly Linked List Algorithms

## Node Structure

A Doubly Linked List node contains three parts:

```text
┌────────┬────────┬────────┐
│  Prev  │  Data  │  Next  │
└────────┴────────┴────────┘
```

* **Prev** → Reference to previous node
* **Data** → Stores actual value
* **Next** → Reference to next node



# 1. Display Doubly Linked List

## Objective

Print all nodes from left to right.

## Algorithm

### Step 1

Check if DLL is empty.

```text
IF head = NULL
    PRINT "DLL is Empty"
    STOP
```

### Step 2

Initialize iterator.

```text
itr = head
```

### Step 3

Traverse until NULL.

```text
WHILE itr != NULL
```

### Step 4

Print current node data.

```text
PRINT itr.data
```

### Step 5

Move to next node.

```text
itr = itr.next
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 2. Insert At Beginning

## Objective

Insert a node before the current head.

## Algorithm

### Step 1

Create new node.

```text
new_node = Node(NULL, data, head)
```

### Step 2

If DLL is not empty.

```text
IF head != NULL
```

Update old head.

```text
head.prev = new_node
```

### Step 3

Move head.

```text
head = new_node
```

### Visualization

Before

```text
10 ←→ 20 ←→ 30
```

After inserting 5

```text
5 ←→ 10 ←→ 20 ←→ 30
```

### Complexity

```text
Time  : O(1)
Space : O(1)
```

---

# 3. Insert At End

## Objective

Insert a node at the last position.

## Algorithm

### Case 1 : Empty DLL

```text
head = Node(NULL, data, NULL)
```

### Case 2 : DLL Exists

#### Step 1

```text
itr = head
```

#### Step 2

Traverse to last node.

```text
WHILE itr.next != NULL
    itr = itr.next
```

#### Step 3

Create new node.

```text
new_node = Node(itr, data, NULL)
```

#### Step 4

Connect last node.

```text
itr.next = new_node
```

### Visualization

Before

```text
10 ←→ 20 ←→ 30
```

After

```text
10 ←→ 20 ←→ 30 ←→ 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 4. Insert At Index

## Objective

Insert node at a specific index.

## Algorithm

### Step 1

Validate index.

```text
IF index < 0 OR index > length
    THROW Exception
```

### Step 2

If index = 0

```text
Insert At Beginning
```

### Step 3

If index = length

```text
Insert At End
```

### Step 4

Traverse until index - 1.

```text
itr = head
count = 0
```

### Step 5

Create node.

```text
new_node = Node(itr, data, itr.next)
```

### Step 6

Update next node.

```text
itr.next.prev = new_node
```

### Step 7

Update current node.

```text
itr.next = new_node
```

### Visualization

Before

```text
10 ←→ 20 ←→ 30 ←→ 40
```

Insert 25 at index 2

```text
10 ←→ 20 ←→ 25 ←→ 30 ←→ 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 5. Insert After Data

## Objective

Insert a node after a specific value.

## Algorithm

### Step 1

Traverse DLL.

```text
itr = head
```

### Step 2

Search target data.

```text
WHILE itr != NULL
```

### Step 3

If found.

```text
itr.data == target_data
```

### Step 4

Create node.

```text
new_node = Node(itr, data_to_insert, itr.next)
```

### Step 5

If next node exists.

```text
itr.next.prev = new_node
```

### Step 6

Connect current node.

```text
itr.next = new_node
```

### Step 7

Stop traversal.

```text
BREAK
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 6. Insert A List

## Objective

Replace existing DLL with a new list.

## Algorithm

### Step 1

Delete current DLL.

```text
head = NULL
```

### Step 2

Traverse input list.

```text
FOR each item in data_list
```

### Step 3

Insert each item at end.

```text
Insert At End(item)
```

### Example

Input

```python
[10, 20, 30]
```

Output

```text
10 ←→ 20 ←→ 30
```

### Complexity

```text
Time : O(n²)
```

---

# 7. Length Of DLL

## Objective

Count total nodes.

## Algorithm

### Step 1

```text
count = 0
itr = head
```

### Step 2

Traverse DLL.

```text
WHILE itr != NULL
```

### Step 3

Increment count.

```text
count += 1
```

### Step 4

Move iterator.

```text
itr = itr.next
```

### Step 5

Return count.

```text
RETURN count
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 8. Remove At Index

## Objective

Delete node at a specific index.

## Algorithm

### Step 1

Validate index.

```text
IF index invalid
    THROW Exception
```

### Step 2

If removing head.

```text
head = head.next
```

### Step 3

Update new head.

```text
IF head != NULL
    head.prev = NULL
```

### Step 4

Traverse to target index.

```text
itr = head
count = 0
```

### Step 5

Reconnect next node.

```text
itr.next.prev = itr.prev
```

### Step 6

Reconnect previous node.

```text
itr.prev.next = itr.next
```

### Visualization

Before

```text
10 ←→ 20 ←→ 30 ←→ 40
```

Remove index 2

```text
10 ←→ 20 ←→ 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 9. Remove By Data

## Objective

Delete first occurrence of a value.

## Algorithm

### Case 1 : Empty DLL

```text
IF head = NULL
    PRINT "DLL is Empty"
```

### Case 2 : Data Found At Head

```text
IF head.data == target
```

Move head.

```text
head = head.next
```

Update prev pointer.

```text
head.prev = NULL
```

### Case 3 : Data Found Elsewhere

#### Step 1

Traverse DLL.

```text
itr = head
```

#### Step 2

Search target.

```text
WHILE itr != NULL
```

#### Step 3

Reconnect next node.

```text
itr.next.prev = itr.prev
```

#### Step 4

Reconnect previous node.

```text
itr.prev.next = itr.next
```

#### Step 5

Stop traversal.

```text
BREAK
```

### Visualization

Before

```text
10 ←→ 20 ←→ 30 ←→ 40
```

Remove 30

```text
10 ←→ 20 ←→ 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 10. Print Forward

## Objective

Print DLL from Head → Tail.

## Algorithm

### Step 1

Start from head.

```text
itr = head
```

### Step 2

Traverse using next pointer.

```text
WHILE itr != NULL
```

### Step 3

Print data.

```text
PRINT itr.data
```

### Step 4

Move forward.

```text
itr = itr.next
```

### Example

```text
10 ←→ 20 ←→ 30 ←→ 40
```

Output

```text
10 ←→ 20 ←→ 30 ←→ 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 11. Print Backward

## Objective

Print DLL from Tail → Head.

## Algorithm

### Step 1

Move to last node.

```text
itr = head

WHILE itr.next != NULL
    itr = itr.next
```

### Step 2

Traverse backwards.

```text
WHILE itr != NULL
```

### Step 3

Print data.

```text
PRINT itr.data
```

### Step 4

Move backward.

```text
itr = itr.prev
```

### Example

DLL

```text
10 ←→ 20 ←→ 30 ←→ 40
```

Output

```text
40 ←→ 30 ←→ 20 ←→ 10
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# Complete Complexity Table

| Operation           | Time Complexity |
| ------------------- | --------------- |
| Display             | O(n)            |
| Insert At Beginning | O(1)            |
| Insert At End       | O(n)            |
| Insert At Index     | O(n)            |
| Insert After Data   | O(n)            |
| Insert A List       | O(n²)           |
| Length Of DLL       | O(n)            |
| Remove At Index     | O(n)            |
| Remove By Data      | O(n)            |
| Print Forward       | O(n)            |
| Print Backward      | O(n)            |

---

---

# Circular Doubly Linked List (CDLL)

## What is a Circular Doubly Linked List?

A **Circular Doubly Linked List (CDLL)** is a Doubly Linked List in which:

- The **last node's `next` points to the head**.
- The **head node's `prev` points to the last node**.

Thus, there is **no NULL pointer** at either end of the list.

---

# Visualization

```text
            Head
             ↓
10 ←→ 20 ←→ 30 ←→ 40
↑                 ↓
└─────────────────┘
```

Both forward and backward traversal are circular.

---

# Features of Circular Doubly Linked List

- Each node stores **Prev, Data and Next**.
- Last node connects back to Head.
- Head's previous pointer points to the last node.
- Traversal is possible in both directions.
- No NULL pointer exists.
- Insertions and deletions require updating both `prev` and `next` pointers.

---

# Node Structure

```text
┌────────┬────────┬────────┐
│  Prev  │  Data  │  Next  │
└────────┴────────┴────────┘
```

Unlike DLL,

```text
Head.prev = Last
Last.next = Head
```

instead of

```text
Head.prev = NULL
Last.next = NULL
```

---

# Algorithms

## 1. Display

### Objective

Display the CDLL from Head to Last.

### Algorithm

1. Check whether the list is empty.
2. Start from Head.
3. Print current node.
4. Move to next node.
5. Stop when Head is reached again.

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

## 3. Insert At Beginning

### Algorithm

### Case 1 : Empty List

```text
Create node
head = node
node.next = head
node.prev = head
```

### Case 2 : Non-empty List

1. New node's `next = head`
2. New node's `prev = head.prev`
3. Last node's `next = new node`
4. Head's `prev = new node`
5. Move head to new node

### Visualization

Before

```text
10 ←→ 20 ←→ 30
↑             ↓
└─────────────┘
```

After inserting 5

```text
5 ←→ 10 ←→ 20 ←→ 30
↑                 ↓
└─────────────────┘
```

### Complexity

```text
Time  : O(1)
Space : O(1)
```

---

## 4. Insert At End

### Algorithm

### Case 1

If list is empty

```text
Create node
head = node
node.next = head
node.prev = head
```

### Case 2

1. New node's `next = head`
2. New node's `prev = head.prev`
3. Last node's `next = new node`
4. Head's `prev = new node`

### Complexity

```text
Time  : O(1)
Space : O(1)
```

---

## 5. Insert At Index

### Algorithm

1. Validate index.
2. If index = 0

```text
Insert At Beginning
```

3. If index = length

```text
Insert At End
```

4. Traverse to the required position.
5. Insert node between previous and current node.

```text
new.prev = itr.prev
new.next = itr

itr.prev.next = new
itr.prev = new
```

### Complexity

```text
Time : O(n)
```

---

## 6. Insert After Data

### Algorithm

1. Traverse the CDLL.
2. Search target data.
3. Insert node after it.

```text
new.next = itr.next
new.prev = itr

itr.next.prev = new
itr.next = new
```

4. Stop when Head is reached again.

### Complexity

```text
Time : O(n)
```

---

## 7. Insert A List

### Algorithm

1. Delete existing CDLL.
2. Reset count.
3. Insert each element using Insert At End.

### Complexity

```text
Time : O(n²)
```

---

## 8. Length

Return maintained node count.

```text
RETURN count
```

### Complexity

```text
Time : O(1)
```

---

## 9. Remove At Index

### Algorithm

### Case 1 : Removing Head

If only one node exists

```text
head = NULL
```

Otherwise

```text
head.prev.next = head.next
head.next.prev = head.prev
head = head.next
```

### Case 2 : Other Index

Traverse to target node.

Reconnect surrounding nodes.

```text
itr.prev.next = itr.next
itr.next.prev = itr.prev
```

### Complexity

```text
Time : O(n)
```

---

## 10. Remove By Data

### Algorithm

### Case 1

Data found at Head.

If only one node exists

```text
head = NULL
```

Else

```text
head.prev.next = head.next
head.next.prev = head.prev
head = head.next
```

### Case 2

Traverse until target data is found.

Reconnect neighbors.

```text
itr.prev.next = itr.next
itr.next.prev = itr.prev
```

Stop when Head is reached again.

### Complexity

```text
Time : O(n)
```

---
## 2. Print Backward

### Objective

Display the CDLL from Last to Head.

### Algorithm

1. Check whether the list is empty.
2. Start from `head.prev`.
3. Print current node.
4. Move using `prev`.
5. Stop when the last node is reached again.

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# Time Complexity

| Operation | Time |
|-----------|------|
| Display | O(n) |
| Print Backward | O(n) |
| Insert At Beginning | O(1) |
| Insert At End | O(1) |
| Insert At Index | O(n) |
| Insert After Data | O(n) |
| Insert A List | O(n²) |
| Length | O(1) |
| Remove At Index | O(n) |
| Remove By Data | O(n) |

---

# Applications of Circular Doubly Linked List

- Browser history (Forward and Backward navigation)
- Music playlist with Previous and Next buttons
- Image viewers
- Undo / Redo operations
- Round Robin scheduling
- Circular deques
- Operating System process scheduling

---

# Singly LL vs Doubly LL

| Feature            | Singly LL | Doubly LL    |
| ------------------ | --------- | ------------ |
| Pointers per Node  | 1         | 2            |
| Memory Usage       | Less      | More         |
| Forward Traversal  | Yes       | Yes          |
| Backward Traversal | No        | Yes          |
| Deletion           | Harder    | Easier       |
| Implementation     | Simpler   | More Complex |

---


# Key Interview Points

1. Linked Lists use non-contiguous memory.
2. Each node contains data and next pointer.
3. Random access is not possible.
4. Insert At Beginning is O(1).
5. Searching requires traversal.
6. Linked Lists are dynamic in size.
7. Insertion and deletion are easier than arrays.
8. Access by index is O(n).
9. Extra memory is required for storing pointers.
10. Each node stores **Prev + Data + Next**.
11. DLL supports traversal in both directions.
12. Deletion is easier because previous node is directly accessible.
13. DLL requires extra memory for the prev pointer.
14. Insertion and deletion at known positions require only pointer updates.
15. Access by index is still O(n).
16. Print backward is a major advantage of DLL over Singly LL.
17. DLL is commonly used in browser history, undo/redo systems, and music playlists.
18. Every node stores Prev, Data and Next.
19. Last node points to Head.
20. Head's Prev points to the Last node.
21. No NULL pointer exists.
22. Traversal can be performed in both directions.
23. Insertion at beginning and end is O(1) when using `head.prev`.
24. Deletion requires updating both `prev` and `next` pointers.
25. A single-node CDLL points to itself through both `next` and `prev`.
26. `head.prev` always represents the last node.
27. CDLL combines the advantages of both Circular Linked Lists and Doubly Linked Lists.

---

# Interview Definition

> A Doubly Linked List (DLL) is a linear data structure in which each node contains three parts: a pointer to the previous node, the data, and a pointer to the next node. Unlike a Singly Linked List, it allows traversal in both forward and backward directions, making insertion and deletion operations more efficient when the target node is known.

> A Circular Doubly Linked List (CDLL) is a doubly linked list in which the last node's `next` points to the head and the head's `prev` points to the last node, forming a closed circular structure. It supports efficient traversal in both forward and backward directions without using NULL pointers.