# Queue

## What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle. This means the element inserted first is removed first, just like people standing in a queue at a ticket counter.

Only two basic operations are allowed:

- **Enqueue** – Insert an element at the rear of the queue.
- **Dequeue** – Remove an element from the front of the queue.

Unlike a Stack, where insertion and deletion occur from the same end, a Queue performs insertion at one end and deletion at the other.

---

## Working of a Queue

```
Initially

Front                     Rear
  ↓                         ↓
Empty Queue


Enqueue(10)

Front Rear
  ↓     ↓
+----+
| 10 |
+----+


Enqueue(20)

Front         Rear
  ↓             ↓
+----+----+
| 10 | 20 |
+----+----+


Enqueue(30)

Front              Rear
  ↓                  ↓
+----+----+----+
| 10 | 20 | 30 |
+----+----+----+


Dequeue()

Front         Rear
  ↓             ↓
+----+----+
| 20 | 30 |
+----+----+
```

The first inserted element (**10**) is also the first element removed.

---

# Features of Queue

- Follows **FIFO (First In, First Out)** principle.
- Insertion takes place only at the **rear**.
- Deletion takes place only at the **front**.
- Can be implemented using **Arrays** or **Linked Lists**.
- Supports constant time insertion and deletion in efficient implementations.
- Widely used in scheduling, buffering, and traversal algorithms.

---

# Basic Queue Operations

| Operation | Description |
|-----------|-------------|
| Enqueue | Insert an element at the rear |
| Dequeue | Remove the front element |
| Front | Returns the first element |
| Rear | Returns the last element |
| isEmpty | Checks whether the queue is empty |
| isFull | Checks whether the queue is full (Array Implementation) |
| Size | Returns the number of elements |

---

# Queue Implementations

There are four common implementations of Queue:

1. Queue using Array
2. Circular Queue using Array
3. Queue using Linked List
4. Circular Queue using Linked List

---

# 1. Queue using Array

## Idea

A fixed-size array is used to store queue elements.

Two indices are maintained:

- **front** → points before the first element
- **rear** → points to the last inserted element

Insertion increments the rear index, while deletion increments the front index.

### Algorithm

### Enqueue

```
If queue is full
    Queue Overflow

Increment rear

Insert data at rear

Increase count
```

### Dequeue

```
If queue is empty
    Queue Underflow

Increment front

Store front element

Decrease count

Return removed element
```

### Advantages

- Easy to implement.
- O(1) insertion and deletion.
- Simple indexing.

### Disadvantages

- Fixed size.
- Wastes memory after multiple dequeue operations because freed positions cannot be reused.

---

# 2. Circular Queue using Array

## Idea

A Circular Queue connects the last array index back to the first index.

Instead of moving only forward, the indices wrap around using the modulo (`%`) operator.

```
rear = (rear + 1) % size
front = (front + 1) % size
```

This efficiently reuses empty spaces created after dequeuing.

### Algorithm

### Enqueue

```
If queue is full
    Queue Overflow

rear = (rear + 1) mod size

Insert data

Increase count
```

### Dequeue

```
If queue is empty
    Queue Underflow

front = (front + 1) mod size

Remove element

Decrease count
```

### Advantages

- Reuses empty positions.
- Prevents memory wastage.
- O(1) insertion and deletion.

### Disadvantages

- Fixed capacity.
- Slightly more complex than a normal queue.

---

# 3. Queue using Linked List

## Idea

Instead of an array, nodes are connected using pointers.

Two pointers are maintained:

- **front**
- **rear**

The queue grows dynamically, so there is no fixed capacity.

### Algorithm

### Enqueue

```
Create a new node

If queue is empty

    front = rear = new node

Else

    rear.next = new node

    rear = new node

Increase count
```

### Dequeue

```
If queue is empty

    Queue Underflow

Store front data

Move front to next node

If queue becomes empty

    rear = None

Decrease count

Return removed data
```

### Advantages

- Dynamic size.
- No memory wastage.
- No fixed capacity.

### Disadvantages

- Extra memory required for pointers.
- Slightly slower than arrays due to pointer traversal.

---

# 4. Circular Queue using Linked List

## Idea

The last node points back to the first node, creating a circular structure.

```
rear.next = front
```

This allows continuous traversal without reaching a `None` pointer.

### Algorithm

### Enqueue

```
Create new node

If queue is empty

    front = rear = node

    rear.next = front

Else

    node.next = front

    rear.next = node

    rear = node

Increase count
```

### Dequeue

```
If queue is empty

    Queue Underflow

Store front data

If only one node exists

    front = rear = None

Else

    rear.next = front.next

    front = front.next

Decrease count

Return removed data
```

### Advantages

- Dynamic size.
- Efficient O(1) insertion and deletion.
- No memory wastage.
- Continuous circular traversal.

### Disadvantages

- More complex implementation.
- Extra pointer maintenance required.

---

# Time Complexity

| Operation | Queue Array | Circular Queue Array | Queue LL | Circular Queue LL |
|-----------|-------------|----------------------|----------|-------------------|
| Enqueue | O(1) | O(1) | O(1) | O(1) |
| Dequeue | O(1) | O(1) | O(1) | O(1) |
| Front | O(1) | O(1) | O(1) | O(1) |
| Rear | O(1) | O(1) | O(1) | O(1) |
| Display | O(n) | O(n) | O(n) | O(n) |
| Size | O(1) | O(1) | O(1) | O(1) |

---

# Applications of Queue

Queues are widely used in computer science and real-world systems.

- CPU Scheduling
- Printer Queue Management
- Keyboard Input Buffer
- Network Packet Processing
- Breadth First Search (BFS)
- Level Order Traversal of Trees
- Web Server Request Handling
- Call Center Systems
- Message Queues
- Task Scheduling

---

# Queue vs Stack

| Feature | Queue | Stack |
|---------|-------|-------|
| Principle | FIFO | LIFO |
| Insertion | Rear | Top |
| Deletion | Front | Top |
| Main Operations | Enqueue / Dequeue | Push / Pop |
| Applications | Scheduling, BFS | Undo, Recursion, Expression Evaluation |

---

# Summary

A Queue is one of the most fundamental linear data structures. It processes elements in the order they are inserted (FIFO). While a simple array-based queue is easy to implement, it suffers from memory wastage after deletions. A Circular Queue overcomes this limitation by reusing empty spaces. Linked List implementations provide dynamic memory allocation, and a Circular Queue using a Linked List combines dynamic sizing with efficient circular traversal.

Understanding all four implementations provides a strong foundation for more advanced data structures such as **Deque**, **Priority Queue**, and **Graphs**.