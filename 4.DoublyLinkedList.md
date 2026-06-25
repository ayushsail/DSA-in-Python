# Doubly Linked List Algorithms

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