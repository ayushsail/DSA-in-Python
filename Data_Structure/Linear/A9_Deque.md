# Deque (Double Ended Queue)

## What is a Deque?

A **Deque (Double Ended Queue)** is a linear data structure that allows **insertion and deletion from both the front and the rear**. It combines the functionality of both a **Stack** and a **Queue**.

Unlike a normal queue where insertion happens only at the rear and deletion only at the front, a deque provides full flexibility by allowing operations at both ends.

Because of this property, a deque can behave as:

- A Queue (FIFO)
- A Stack (LIFO)

Deque is widely used in scheduling algorithms, browser history, sliding window problems, palindrome checking, and caching mechanisms.

---

# Features of Deque

- Allows insertion from both front and rear.
- Allows deletion from both front and rear.
- Can work as both Queue and Stack.
- Fast insertion and deletion from both ends.
- Circular implementation utilizes memory efficiently.
- Supports O(1) insertion and deletion.
- Can be implemented using:
  - Circular Array
  - Circular Doubly Linked List

---

# Deque Operations

- Insert Front
- Insert Rear
- Delete Front
- Delete Rear
- Get Front
- Get Rear
- Check Empty
- Check Full (Array Implementation)
- Get Size
- Display

---

# Deque Using Circular Array

## Algorithm

### Initialization

- Create an array of fixed size.
- Initialize:
  - `front = -1`
  - `rear = -1`
  - `count = 0`

---

## Insert Front

- Check if deque is full.
- If deque is empty:
  - Set
    - `front = rear = 0`
- Otherwise:
  - Move front one position backward using circular indexing.

```
front = (front - 1 + size) % size
```

- Insert the element at `front`.
- Increase `count`.

---

## Insert Rear

- Check if deque is full.
- If deque is empty:
  - Set

```
front = rear = 0
```

- Otherwise:
  - Move rear one position forward.

```
rear = (rear + 1) % size
```

- Insert element at `rear`.
- Increase `count`.

---

## Delete Front

- Check if deque is empty.
- Store the front value.
- Remove the element.

If only one element exists:

```
front = rear = -1
```

Otherwise:

Move front forward.

```
front = (front + 1) % size
```

- Decrease `count`.
- Return deleted value.

---

## Delete Rear

- Check if deque is empty.
- Store rear value.
- Remove the element.

If only one element exists:

```
front = rear = -1
```

Otherwise:

Move rear backward.

```
rear = (rear - 1 + size) % size
```

- Decrease `count`.
- Return deleted value.

---

## Display

- Start from `front`.
- Traverse exactly `count` elements.
- Move forward using

```
current = (current + 1) % size
```

- Print every element.

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert Front | O(1) |
| Insert Rear | O(1) |
| Delete Front | O(1) |
| Delete Rear | O(1) |
| Get Front | O(1) |
| Get Rear | O(1) |
| Display | O(n) |

---

# Important Circular Array Expressions

### Move Front Backward

```
front = (front - 1 + size) % size
```

---

### Move Front Forward

```
front = (front + 1) % size
```

---

### Move Rear Forward

```
rear = (rear + 1) % size
```

---

### Move Rear Backward

```
rear = (rear - 1 + size) % size
```

---

### Empty Deque

```
front = rear = -1
```

---

### First Insertion

```
front = rear = 0
```

---

# Deque Using Circular Doubly Linked List

A Circular Doubly Linked List (CDLL) is ideal for implementing a deque because every node maintains both `next` and `prev` pointers while the last node points back to the first node.

Only two pointers are maintained:

- `front`
- `rear`

Every insertion and deletion updates only a few pointers, making every operation **O(1)**.

---

## Algorithm

### Insert Front

- Create a new node.

If deque is empty:

- Assign

```
front = rear = node
```

- Make the node circular.

```
node.next = front
node.prev = front
```

Otherwise:

- Connect new node.

```
node.prev = rear
node.next = front
```

- Update surrounding nodes.

```
rear.next = node
front.prev = node
```

- Move front.

```
front = node
```

- Increase count.

---

## Insert Rear

- Create new node.

If deque is empty:

```
front = rear = node
node.next = rear
node.prev = rear
```

Otherwise:

Connect node.

```
node.next = front
node.prev = rear
```

Update existing nodes.

```
rear.next = node
front.prev = node
```

Move rear.

```
rear = node
```

Increase count.

---

## Delete Front

- Check empty.
- Store front value.

If only one node exists:

```
front = rear = None
```

Otherwise:

Connect rear with second node.

```
rear.next = front.next
front.next.prev = rear
```

Move front.

```
front = front.next
```

Decrease count.

Return deleted value.

---

## Delete Rear

- Check empty.
- Store rear value.

If only one node exists:

```
front = rear = None
```

Otherwise:

Connect second last node with front.

```
rear.prev.next = front
front.prev = rear.prev
```

Move rear.

```
rear = rear.prev
```

Decrease count.

Return deleted value.

---

## Display

- Start from `front`.
- Traverse until front is reached again.
- Print every node.

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert Front | O(1) |
| Insert Rear | O(1) |
| Delete Front | O(1) |
| Delete Rear | O(1) |
| Get Front | O(1) |
| Get Rear | O(1) |
| Display | O(n) |

---

# Important Pointer Assignments (CDLL)

## First Node

```
front = rear = node

node.next = front
node.prev = front
```

---

## Insert Front

```
node.prev = rear
node.next = front

rear.next = node
front.prev = node

front = node
```

---

## Insert Rear

```
node.next = front
node.prev = rear

rear.next = node
front.prev = node

rear = node
```

---

## Delete Front

```
rear.next = front.next
front.next.prev = rear

front = front.next
```

---

## Delete Rear

```
rear.prev.next = front
front.prev = rear.prev

rear = rear.prev
```

---

## Delete Last Node

```
front = rear = None
```

---

# Advantages of Deque

- Supports both FIFO and LIFO operations.
- Very efficient for sliding window problems.
- Constant-time insertion and deletion.
- Flexible than Stack and Queue.
- Circular implementations eliminate unnecessary shifting.
- CDLL implementation requires no fixed size.

---

# Applications of Deque

- Browser Back and Forward navigation
- Undo and Redo operations
- Sliding Window Maximum/Minimum
- Palindrome checking
- CPU Scheduling
- Job Scheduling
- Cache implementation
- Task scheduling systems
- BFS (Bidirectional Search)
- Expression evaluation
- LRU Cache

---

# Difference Between Queue and Deque

| Queue | Deque |
|--------|-------|
| Insert only at rear | Insert at both ends |
| Delete only from front | Delete from both ends |
| Follows FIFO | Can work as FIFO and LIFO |
| Less flexible | More flexible |
| Simpler implementation | More versatile |

---

# Summary

A **Deque (Double Ended Queue)** is an extension of the Queue data structure that supports insertion and deletion from both the front and the rear. It combines the characteristics of both Stack and Queue, making it suitable for a wide variety of applications.

In this project, the deque has been implemented using:

- **Circular Array**, which provides efficient memory utilization with fixed size.
- **Circular Doubly Linked List**, which offers dynamic memory allocation without size limitations.

Both implementations achieve **O(1)** time complexity for insertion and deletion operations, making the deque one of the most efficient linear data structures for double-ended operations.