# Linked List

# 1. What is a Linked List?

A **Linked List (LL)** is a linear data structure consisting of individual elements called **nodes**. Each node stores data and a reference (pointer) to the next node in the sequence.

Unlike arrays, linked list elements are **not stored in contiguous memory locations**.

### Visualization

```text
Head
 ↓
[10 | • ] → [20 | • ] → [30 | • ] → [40 | NULL]
```

Each node contains:

```text
[ Data | Next ]
```

* Data → Stores value
* Next → Stores address/reference of next node

---

# 2. Key Characteristics

###  1. Dynamic Size

* Linked Lists can grow and shrink during runtime.

### 2. Non-Contiguous Memory

* Nodes can exist anywhere in memory.

```text
Address      Node

1000         [10 | 5000]
5000         [20 | 9000]
9000         [30 | NULL]
```

### 3. Sequential Access

* To reach a node, we must traverse from the head.
* Cannot directly access Node3 like arrays.

```text
Head → Node1 → Node2 → Node3
```

### 4. Efficient Insertions & Deletions

* No shifting of elements required.
* Only pointers need updating.

### 5. Extra Memory Required

Each node stores an additional pointer.

```text
Node = Data + Next Pointer
```

---

# 3. How Elements are Stored in Linked List

Consider:

```text
10 → 20 → 30
```

Memory representation:

```text
Address      Node

1000         [10 | 5000]
5000         [20 | 8000]
8000         [30 | NULL]
```

Visualization:

```text
Head
 ↓
[10|•] ----→ [20|•] ----→ [30|NULL]
```

Unlike arrays:

```text
Array

1000   1004   1008

[10]   [20]   [30]
```

Linked List nodes can be scattered across memory.

---

# 4. Time Complexity of Linked List Operations

| Operation           | Time Complexity |
| ------------------- | --------------- |
| Access by Index     | O(n)            |
| Search              | O(n)            |
| Insert at Beginning | O(1)            |
| Insert at End       | O(n)            |
| Insert at Index     | O(n)            |
| Delete at Beginning | O(1)            |
| Delete at End       | O(n)            |
| Delete at Index     | O(n)            |
| Remove by Value     | O(n)            |
| Display             | O(n)            |
| Length Calculation  | O(n)            |
---



# Linked List Algorithms

## Node Structure

A node is the basic building block of a Linked List.

Each node contains:

```text
┌──────────┬──────────┐
│   Data   │   Next   │
└──────────┴──────────┘
```

* **Data** stores the actual value.
* **Next** stores the reference to the next node.

Example:

```text
Head
 ↓
[10|•] → [20|•] → [30|NULL]
```

---

# 1. Display Linked List

## Objective

Traverse the Linked List and print all elements.

## Algorithm

### Step 1

Check whether the Linked List is empty.

```text
IF head = NULL
    PRINT "LL is Empty"
    STOP
```

### Step 2

Create a temporary pointer.

```text
itr = head
```

### Step 3

Create an empty string.

```text
llstr = ""
```

### Step 4

Traverse until itr becomes NULL.

```text
WHILE itr != NULL
```

### Step 5

Append current node data.

```text
llstr += itr.data
```

### Step 6

If next node exists, add arrow.

```text
IF itr.next != NULL
    llstr += "-->"
```

### Step 7

Move iterator.

```text
itr = itr.next
```

### Step 8

Print final string.

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 2. Insert At Beginning

## Objective

Insert a new node before the current head.

## Algorithm

### Step 1

Create new node.

```text
new_node = Node(data)
```

### Step 2

Connect new node to current head.

```text
new_node.next = head
```

### Step 3

Move head to new node.

```text
head = new_node
```

### Visualization

Before:

```text
Head
 ↓
10 → 20 → 30
```

After inserting 5:

```text
Head
 ↓
5 → 10 → 20 → 30
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

### Case 1: Empty List

```text
IF head = NULL
    head = new_node
    STOP
```

### Case 2: Non-Empty List

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

Attach new node.

```text
itr.next = new_node
```

### Visualization

Before:

```text
10 → 20 → 30
```

After:

```text
10 → 20 → 30 → 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 4. Insert At Index

## Objective

Insert a node at a specific index.

## Algorithm

### Step 1

Validate index.

```text
IF index < 0
OR index > length
    THROW Exception
```

### Step 2

If index = 0

```text
Insert At Beginning
```

### Step 3

If insertion is at last position

```text
Insert At End
```

### Step 4

Traverse to node before target index.

```text
itr = head
count = 0

WHILE itr != NULL
```

### Step 5

Stop at:

```text
count = index - 1
```

### Step 6

Create new node.

```text
new_node = Node(data)
```

### Step 7

Connect new node.

```text
new_node.next = itr.next
itr.next = new_node
```

### Visualization

Before:

```text
10 → 20 → 30 → 40
```

Insert 25 at index 2

```text
10 → 20 → 25 → 30 → 40
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

Start traversal.

```text
itr = head
```

### Step 2

Search for target value.

```text
WHILE itr != NULL
```

### Step 3

If found:

```text
itr.data == target_data
```

### Step 4

Create new node.

```text
new_node = Node(data_to_insert)
```

### Step 5

Connect links.

```text
new_node.next = itr.next
itr.next = new_node
```

### Step 6

Stop traversal.

```text
BREAK
```

### Step 7

If value not found.

```text
PRINT "Data not found in LL"
```

### Visualization

Before:

```text
10 → 20 → 30
```

Insert 25 after 20

```text
10 → 20 → 25 → 30
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 6. Insert A List

## Objective

Replace current Linked List with a new list.

## Algorithm

### Step 1

Delete existing list.

```text
head = NULL
```

### Step 2

Loop through input list.

```text
FOR each data in data_list
```

### Step 3

Insert element at end.

```text
Insert At End(data)
```

### Example

Input:

```python
[10, 20, 30]
```

Output:

```text
10 → 20 → 30
```

### Complexity

```text
Time  : O(n²)
```

Reason:

```text
Each Insert At End requires traversal.
```

---

# 7. Length Of Linked List

## Objective

Count number of nodes.

## Algorithm

### Step 1

```text
count = 0
itr = head
```

### Step 2

Traverse list.

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

Traverse to node before target node.

```text
itr = head
count = 0
```

### Step 4

Stop at:

```text
count = index - 1
```

### Step 5

Bypass target node.

```text
itr.next = itr.next.next
```

### Visualization

Before:

```text
10 → 20 → 30 → 40
```

Remove index 2

```text
10 → 20 → 40
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# 9. Remove By Data

## Objective

Delete first occurrence of given value.

## Algorithm

### Case 1: Empty List

```text
IF head = NULL
    PRINT "LL is Empty"
```

### Case 2: Data Present At Head

```text
IF head.data = target
    head = head.next
```

### Case 3: Data Present Elsewhere

#### Step 1

Start traversal.

```text
itr = head
```

#### Step 2

Search next node.

```text
WHILE itr.next != NULL
```

#### Step 3

Check value.

```text
itr.next.data == target
```

#### Step 4

Skip target node.

```text
itr.next = itr.next.next
```

#### Step 5

Stop traversal.

```text
BREAK
```

### Step 6

If value not found.

```text
PRINT "Data not found in LL"
```

### Visualization

Before:

```text
10 → 20 → 30 → 40
```

Remove 30

```text
10 → 20 → 40
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
| Length Of LL        | O(n)            |
| Remove At Index     | O(n)            |
| Remove By Data      | O(n)            |

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

---
# Interview Definition

> A Linked List is a dynamic linear data structure consisting of nodes, where each node stores data and a reference to the next node. Nodes are connected through pointers and are not stored in contiguous memory locations.