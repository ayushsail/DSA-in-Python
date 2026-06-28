# Array

## What is an Array?

An **Array** is a linear data structure used to store multiple elements in a contiguous block of memory. Each element is assigned an index, allowing direct access to any element using its position.

### Key Characteristics

* Stores multiple values in a single collection.
* Elements are stored in contiguous memory locations.
* Each element has a unique index.
* Provides O(1) random access.
* Traditional arrays have a fixed size.

---

## How Elements are Stored in an Array

Suppose we store the integer `298`.

An integer typically occupies **4 bytes** of memory.

```text
Value: 298

Memory:
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+

Total Size = 4 Bytes
```

Now consider an array:

```text
arr = [10, 20, 30, 40]
```

Since each integer occupies 4 bytes, memory may look like:

```text
Address     Value
1000        10
1004        20
1008        30
1012        40
```

Notice that each element is stored immediately after the previous one.

This contiguous memory layout is what makes arrays fast.

---

## How Elements are Accessed

The array variable stores the address of the first element.

```text
arr
 ↓
1000
```

### Formula

```text
Address of arr[i]

= Base Address + (i × Size of Data Type)
```

For example:

```text
arr = [10, 20, 30, 40]

Base Address = 1000
Size of int = 4 bytes

Address of arr[3]
= 1000 + (3 × 4)
= 1012
```

Visualization:

```text
Index:      0      1      2      3

Address:  1000   1004   1008   1012

Value:     10     20     30     40
```

Because the address can be calculated directly using a formula, accessing an element takes **O(1)** time.

---

## Static vs Dynamic Arrays

### Static Array

A static array has a fixed size that cannot be changed after creation.

Example (Java):

```java
int[] nums = new int[5];
```

Properties:

* Fixed size
* Memory allocated once
* Fast access
* May waste memory if size is larger than needed

---

### Dynamic Array

A dynamic array can automatically resize when it becomes full.

Examples:

* Python List
* Java ArrayList
* C++ Vector

```python
nums = [1, 2, 3]
```

Properties:

* Resizable
* More flexible
* Slight memory overhead
* Amortized O(1) insertion at the end

---

## Dynamic Array Allocation

Assume the initial capacity is 10.

### Step 1

```text
Capacity = 10

[ _ _ _ _ _ _ _ _ _ _ ]
```

---

### Step 2

After inserting 10 elements:

```text
[ 1 2 3 4 5 6 7 8 9 10 ]
```

Array becomes full.

---

### Step 3

Insert the 11th element.

Since no space is available, a larger memory block is allocated at different area.

Additional Capacity = current capacity * 2 = 10*2 = 20 

Example:

```text
Old Capacity = 10

New Capacity = 20

```

---

### Step 4

Copy all existing elements into the new memory location.

```text
Old Memory

[1 2 3 4 5 6 7 8 9 10]

          ↓ Copy

New Memory

[1 2 3 4 5 6 7 8 9 10 _ _ _ _ _ _ _ _ _ _]
```

---

### Step 5

Insert the new element.

```text
[1 2 3 4 5 6 7 8 9 10 11 _ _ _ _ _ _ _ _ _]
```

This resizing operation takes O(n), but it doesn't happen often.

Therefore:

```text
Append at End = Amortized O(1)
```

---

## Why Insertion in the Middle is Slow

Suppose:

```text
Index:  0  1  2  3
Value: [1, 2, 3, 4]
```

Insert `99` at index 1.

Before:

```text
[1, 2, 3, 4]
```

After:

```text
[1, 99, 2, 3, 4]
```

Elements must be shifted:

```text
2 → right
3 → right
4 → right
```

Time Complexity:

```text
O(n)
```

---

## Array Time Complexities

| Operation             | Complexity |
| --------------------- | ---------- |
| Access by Index       | O(1)       |
| Update by Index       | O(1)       |
| Search                | O(n)       |
| Insert at End         | O(1)*      |
| Insert at Beginning   | O(n)       |
| Insert in Middle      | O(n)       |
| Delete from End       | O(1)       |
| Delete from Beginning | O(n)       |
| Delete from Middle    | O(n)       |

* Amortized Complexity

---

---

# Array Implementation

To better understand how arrays work internally, I implemented both **Fixed Array** and **Dynamic Array** from scratch in Python.

The implementation demonstrates how insertion, deletion, shifting, resizing, and shrinking are performed behind the scenes instead of relying on Python's built-in list methods.

## Implementations

### 1. Fixed Array

A fixed array has a predefined capacity that cannot be changed after creation.

#### Features Implemented

- Constructor
- `isEmpty()`
- `isFull()`
- `insert_at_begining()`
- `insert_at_end()`
- `insert_at(index, data)`
- `delete_at(index)`
- `display()`

Characteristics

- Fixed memory allocation
- Fast random access
- Insertion at end → **O(1)**
- Insertion/deletion at beginning or middle → **O(n)** due to shifting
- Throws **Array Overflow** when the array is full

---

### 2. Dynamic Array

A dynamic array automatically increases or decreases its capacity depending on the number of stored elements.

In addition to all operations available in the Fixed Array implementation, two new methods are introduced:

- `resize()`
- `shrink()`

#### resize()

When the array becomes full,

```
New Capacity = Current Capacity × 2
```

A new larger array is created, all existing elements are copied, and the old array is replaced.

Example

```
Capacity = 5

↓

Insert 6th element

↓

Capacity = 10
```

---

#### shrink()

When the number of elements becomes less than or equal to **25%** of the current capacity,

```
New Capacity = Current Capacity ÷ 2
```

The array shrinks automatically.

However, the array **never shrinks below its initial capacity**, preventing excessive resizing.

Example

```
Initial Capacity = 5

Capacity grows to 20

↓

Delete many elements

↓

Capacity becomes 10

↓

Delete more elements

↓

Capacity becomes 5

↓

No further shrinking
```

---

## Complexity Comparison

| Operation | Fixed Array | Dynamic Array |
|-----------|-------------|---------------|
| Access | O(1) | O(1) |
| Update | O(1) | O(1) |
| Search | O(n) | O(n) |
| Insert at End | O(1) | Amortized O(1) |
| Insert at Beginning | O(n) | O(n) |
| Insert at Index | O(n) | O(n) |
| Delete | O(n) | O(n) |
| Resize | Not Applicable | O(n) |
| Shrink | Not Applicable | O(n) |

---

## Source Code

the source code contains:

- Fixed Array implementation
- Dynamic Array implementation
- Automatic resizing
- Automatic shrinking
- Sample test cases demonstrating all operations

## Advantages of Arrays

* Fast random access
* Cache friendly
* Simple implementation
* Efficient memory usage

---

## Disadvantages of Arrays

* Fixed size (traditional arrays)
* Expensive insertions and deletions
* Requires contiguous memory
* Resizing requires copying elements

---

## Interview Definition

> An array is a linear data structure that stores elements in contiguous memory locations and allows direct access to elements using their index.
