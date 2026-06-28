# Dictionary Implementation Using Hash Table

## Objective

The purpose of this implementation is to understand how Python dictionaries work internally using a Hash Table.

This implementation is **not a complete replacement for Python's built-in dictionary**, but it demonstrates the core concepts:

* Hash Function
* Key → Index Mapping
* Insert Operation
* Search Operation
* Delete Operation
* Operator Overloading
* Dictionary-like Syntax

---
# Implementation

## 1. Internal Structure

We create a fixed-size array.

```python
self.MAX = 50
self.arr = [None for i in range(self.MAX)]
```

Visualization:

```text
Index

0  -> None
1  -> None
2  -> None
3  -> None
...
49 -> None
```

---

## 2.  Hash Function

The hash function converts a key into an array index.

```python
def get_hash(self,key):
    h = 0

    for char in key:
        h += ord(char)

    return h % self.MAX
```

Example:

```python
key = "march 6"
```

Calculation:

```text
m + a + r + c + h + " " + 6
```

Total:

```text
Hash Value = 609
```

Then:

```text
609 % 50 = 9
```

Data will be stored at:

```text
arr[17]
```

---

## 3. Insert Operation

Method:

```python
__setitem__(self,key,value)
```

Usage:

```python
dict["march 6"] = 320
```

Python automatically calls:

```python
dict.__setitem__("march 6",320)
```

Steps:

1. Compute hash.
2. Get index.
3. Store value at that index.

Complexity:

```text
O(1)
```

Average Case

---

## 4. Search Operation

Method:

```python
__getitem__(self,key)
```

Usage:

```python
dict["march 6"]
```

Python automatically calls:

```python
dict.__getitem__("march 6")
```

Steps:

1. Compute hash.
2. Find index.
3. Return stored value.

Complexity:

```text
O(1)
```

Average Case

---

## 5. Delete Operation

Method:

```python
__delitem__(self,key)
```

Usage:

```python
del dict["march 6"]
```

Python automatically calls:

```python
dict.__delitem__("march 6")
```

Steps:

1. Compute hash.
2. Find index.
3. Replace value with None.

Complexity:

```text
O(1)
```

Average Case

---

## 6. Length Operation

Method:

```python
__len__(self)
```

Usage:

```python
len(dict)
```

Steps:

1. Traverse array.
2. Count non-empty entries.
3. Return count.

Complexity:

```text
O(n)
```

where n = size of hash table.

---

# Operator Overloading Used

| Method      | Syntax            |
| ----------- | ----------------- |
| **setitem** | dict[key] = value |
| **getitem** | dict[key]         |
| **delitem** | del dict[key]     |
| **len**     | len(dict)         |

---

# Limitation Of Current Implementation

Current implementation stores only the value.

```python
self.arr[h] = value
```

Example:

```python
dict["march 6"] = 320
```

Stored as:

```text
320
```

The key is discarded after hashing.

---

## 1. Collision Problem

Suppose:

```python
dict["abc"] = 100
dict["cab"] = 200
```

If both produce the same hash index:

```text
Index 15
```

Then:

```text
100 gets overwritten by 200
```

Result:

```python
dict["abc"]
```

returns:

```text
200
```

which is incorrect.

---

## 2. Making It Closer To A Real Dictionary

Instead of storing only values:

```python
self.arr[h] = value
```

store:

```python
self.arr[h] = (key, value)
```

Example:

```python
("march 6", 320)
```

Now both key and value are preserved.

---

# Collision Handling (Chaining)

A better approach:

```python
self.arr[h] = [
    (key1, value1),
    (key2, value2)
]
```

Visualization:

```text
Index 10

[
  ("abc",100),
  ("cab",200),
  ("bca",300)
]
```

Benefits:

* No overwriting
* Multiple keys can share same bucket
* Collision handling becomes possible

Complexity:

```text
Average : O(1)
Worst   : O(n)
```

---

# Additional Methods Needed For A Better Dictionary

## **contains**()

Allows:

```python
"march 6" in dict
```

Purpose:

* Checks whether a key exists.

---

## **iter**()

Allows:

```python
for key in dict:
    print(key)
```

Purpose:

* Iterate through all keys.

---

## **str**()

Allows:

```python
print(dict)
```

Output:

```python
{
    "march 6": 320,
    "march 7": 340
}
```

instead of:

```text
<Dictionary object at 0x00000123>
```

---

## Optional Methods

### keys()

Returns:

```python
dict.keys()
```

Output:

```python
["march 6", "march 7"]
```

---

### values()

Returns:

```python
dict.values()
```

Output:

```python
[320, 340]
```

---

### items()

Returns:

```python
dict.items()
```

Output:

```python
[
    ("march 6",320),
    ("march 7",340)
]
```

---

# Complexity Table

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Insert    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |
| Contains  | O(1)         | O(n)       |
| Length    | O(n)         | O(n)       |
| Iterate   | O(n)         | O(n)       |

---

# What This Project Teaches

This implementation helps understand:

* Hash Tables
* Hash Functions
* Buckets
* Dictionary Internals
* Operator Overloading
* Collision Problems
* Collision Resolution
* Time Complexity Analysis

Although simplified, this project demonstrates the core idea behind one of Python's most powerful data structures: the Dictionary.
