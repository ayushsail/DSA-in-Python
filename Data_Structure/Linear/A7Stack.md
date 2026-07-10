# Stack

## What is a Stack?

A **Stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle.

This means the **last element inserted into the stack is the first one to be removed**.

Think of a stack of books.

```
Push(10)
Push(20)
Push(30)

        TOP
         │
         ▼
     ┌──────┐
     │  30  │
     ├──────┤
     │  20  │
     ├──────┤
     │  10  │
     └──────┘
```

Now perform

```
Pop()
```

```
        TOP
         │
         ▼
     ┌──────┐
     │  20  │
     ├──────┤
     │  10  │
     └──────┘
```

The last inserted element (`30`) is removed first.

---

# How Stack Works

A stack allows insertion and deletion **only from one end**, called the **TOP**.

```
           TOP
            │
            ▼
     ┌─────────────┐
     │ Push / Pop  │
     └─────────────┘
           ▲
           │
     All operations
     happen here
```

No operation is performed from the bottom or middle.

---

# Basic Operations

| Operation | Description |
|-----------|-------------|
| Push | Insert an element at the top |
| Pop | Remove the top element |
| Peek | View the top element without removing it |
| isEmpty | Check whether the stack is empty |
| get_size | Return the number of elements |
| Display | Print all elements from top to bottom |
| Clear | Remove all elements (Array implementation) |

---

# Applications of Stack

Stacks are widely used in computer science.

Some common applications are:

- Function Call Stack
- Recursion
- Undo / Redo Operations
- Browser Back Button
- Parentheses Matching
- Expression Evaluation
- Depth First Search (DFS)
- Backtracking Algorithms

---

# Stack Representation

## Array Implementation

```
TOP = 3

Index

0      1      2      3
────────────────────────────
10     20     30     40
                     ▲
                    TOP
```

---

## Linked List Implementation

```
TOP (Head)
   │
   ▼

┌─────┐
│ 40  │
└──┬──┘
   │
┌──▼──┐
│ 30  │
└──┬──┘
   │
┌──▼──┐
│ 20  │
└──┬──┘
   │
┌──▼──┐
│ 10  │
└─────┘
```

The head node itself acts as the **TOP** of the stack.

---

# Array Implementation

In this implementation, a fixed-size array is used.

A variable named `TOP` stores the index of the current top element.

```
Initially

TOP = -1

Array

[ None None None None None ]
```

When an element is pushed,

```
TOP++

↓

Insert element
```

When an element is popped,

```
Remove element

↓

TOP--
```

---

# Array Implementation Algorithms

## Constructor

### Purpose

Initialize a fixed-size stack.

### Algorithm

1. Receive stack size.
2. Create an array of given size.
3. Initialize every element with `None`.
4. Set

```
TOP = -1
```

---

## isFull()

### Algorithm

1. Compare

```
TOP == size - 1
```

2. If true

Return `True`

3. Otherwise

Return `False`

Time Complexity

```
O(1)
```

---

## isEmpty()

### Algorithm

1. Compare

```
TOP == -1
```

2. Return the result.

Time Complexity

```
O(1)
```

---

## push(data)

### Algorithm

1. Check whether stack is full.
2. If full

```
Raise Stack Overflow
```

3. Increment `TOP`.
4. Store data at

```
arr[TOP]
```

5. Return inserted value.

Time Complexity

```
O(1)
```

---

## pop()

### Algorithm

1. Check whether stack is empty.
2. If empty

```
Raise Stack Underflow
```

3. Store the top element.
4. Replace top position with `None`.
5. Decrement `TOP`.
6. Return removed value.

Time Complexity

```
O(1)
```

---

## peek()

### Algorithm

1. Check whether stack is empty.
2. Return

```
arr[TOP]
```

Time Complexity

```
O(1)
```

---

## get_size()

### Algorithm

Return

```
TOP + 1
```

Time Complexity

```
O(1)
```

---

## display()

### Algorithm

1. Check whether stack is empty.
2. Traverse from

```
TOP → 0
```

3. Print every element.

Time Complexity

```
O(n)
```

---

## clear()

### Algorithm

1. Create a new array filled with `None`.
2. Assign it to the stack.
3. Reset

```
TOP = -1
```

Time Complexity

```
O(n)
```

---

# Linked List Implementation

In this implementation, a **Singly Linked List** is used.

The **head node acts as the TOP**.

Every push and pop operation is performed at the beginning of the linked list.

```
TOP

↓

40 → 30 → 20 → 10
```

No traversal is required.

---

# Linked List Implementation Algorithms

## Constructor

### Algorithm

1. Set

```
top = None
```

2. Initialize

```
count = 0
```

---

## isEmpty()

### Algorithm

1. Check whether

```
top is None
```

2. Return result.

Time Complexity

```
O(1)
```

---

## push(data)

### Algorithm

1. Create a new node.
2. Point its `next` to current `top`.
3. Update

```
top = new node
```

4. Increment `count`.
5. Return inserted value.

Time Complexity

```
O(1)
```

---

## pop()

### Algorithm

1. Check whether stack is empty.
2. Store data of top node.
3. Move

```
top = top.next
```

4. Decrement `count`.
5. Return removed value.

Time Complexity

```
O(1)
```

---

## peek()

### Algorithm

1. Check whether stack is empty.
2. Return

```
top.data
```

Time Complexity

```
O(1)
```

---

## get_size()

### Algorithm

Return

```
count
```

Time Complexity

```
O(1)
```

---

## display()

### Algorithm

1. Start from `top`.
2. Traverse until `None`.
3. Print every node.

Time Complexity

```
O(n)
```

---

# Time Complexity Comparison

| Operation | Array Stack | Linked List Stack |
|-----------|-------------|-------------------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| get_size | O(1) | O(1) |
| Display | O(n) | O(n) |
| Clear | O(n) | Not Implemented |

---

# Array vs Linked List Implementation

| Feature | Array Stack | Linked List Stack |
|----------|-------------|-------------------|
| Memory Allocation | Contiguous | Dynamic |
| Stack Size | Fixed | Dynamic |
| Overflow | Possible | Only when memory is exhausted |
| Extra Memory | No | One pointer per node |
| Cache Performance | Better | Slightly Lower |
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |

---

# Advantages

- Simple implementation.
- All primary operations run in **O(1)** time.
- Ideal for LIFO-based problems.
- Used internally by programming languages for function calls and recursion.

---

# Disadvantages

- Only the top element is directly accessible.
- Array implementation has a fixed capacity.
- Linked List implementation requires additional memory for pointers.

---

# Source Code

The complete implementation is available in:

```
A7_StackImplementation.py
```

The file contains:

- Stack using Fixed Array
- Stack using Singly Linked List
- Push
- Pop
- Peek
- isEmpty
- get_size
- Display
- Clear (Array implementation)
- Sample test cases for both implementations

---

# Key Takeaways

- A Stack follows the **LIFO (Last In, First Out)** principle.
- All insertions and deletions occur only at the **TOP**.
- Array implementation is simple and cache-friendly but has a fixed size.
- Linked List implementation grows dynamically and avoids overflow caused by fixed capacity.
- `push()`, `pop()`, and `peek()` all execute in **O(1)** time, making the stack one of the most efficient linear data structures for LIFO operations.