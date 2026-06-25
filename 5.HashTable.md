# Hash Table

## What is a Hash Table?

A **Hash Table** is a data structure that stores data in the form of **Key-Value Pairs**.

It uses a **Hash Function** to convert a key into an array index, allowing data to be stored and retrieved efficiently.

### Example

```text
Key         Value
-----------------
"march 6"   320
"march 7"   340
"march 8"   470
```

Instead of searching through all elements one by one, a Hash Table computes the location directly using a hash function.

---

# Why Do We Need Hash Tables?

Suppose we store stock prices in a list:

```python
[
    ("march 6", 320),
    ("march 7", 340),
    ("march 8", 470)
]
```

To find the stock price for `"march 8"`:

```text
Check march 6
Check march 7
Check march 8
```

Time Complexity:

```text
O(n)
```

With a Hash Table:

```text
"march 8"
     ↓
Hash Function
     ↓
Index
     ↓
Value Found
```

Time Complexity:

```text
O(1)
```

Average Case

---

# Key Components of a Hash Table

## 1. Key

A key is used to uniquely identify data.

Example:

```python
"march 6"
```

---

## 2. Value

The actual data associated with the key.

Example:

```python
320
```

---

## 3. Hash Function

A function that converts a key into an array index.

Example:

```python
hash("march 6")
```

---

## 4. Bucket

A bucket is a location in the underlying array where data is stored.

```text
Index

0
1
2
3
...
49
```

---

# Hash Table Implementation
## Internal Structure of Our Hash Table

We create a fixed-size array of length 50.

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

Initially, all buckets are empty.

---

# Hash Function

## Purpose

Convert a key into an array index.

### Implementation

```python
def get_hash(self,key):
    h = 0

    for char in key:
        h += ord(char)

    return h % self.MAX
```

---

## How It Works

Suppose:

```python
key = "march 6"
```

ASCII values:

```text
m = 109
a = 97
r = 114
c = 99
h = 104
(space) = 32
6 = 54
```

Sum:

```text
109 + 97 + 114 + 99 + 104 + 32 + 54
= 609
```

Array size:

```text
50
```

Index:

```text
609 % 50 = 9
```

So:

```text
"march 6"
    ↓
Hash Function
    ↓
Index 9
```

Data will be stored at:

```python
arr[9]
```

---

# Hash Table Implementation

```python
class HashTable:

    def __init__(self):
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0

        for char in key:
            h += ord(char)

        return h % self.MAX

    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self,key):
        h = self.get_hash(key)
        print(f"Stock Price on {key} is ",self.arr[h])

    def remove(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
```

---

# Operations on Hash Table

## 1. Insert (Add)

### Algorithm

1. Receive key and value.
2. Compute hash index.
3. Store value at that index.

### Code

```python
def add(self,key,value):
    h = self.get_hash(key)
    self.arr[h] = value
```

### Example

```python
t.add("march 6",320)
```

### Complexity

```text
O(1)
```

Average Case

---

## 2. Search (Get)

### Algorithm

1. Receive key.
2. Compute hash index.
3. Return value stored at that index.

### Code

```python
def get(self,key):
    h = self.get_hash(key)
    print(self.arr[h])
```

### Example

```python
t.get("march 6")
```

Output:

```text
320
```

### Complexity

```text
O(1)
```

Average Case

---

## 3. Delete (Remove)

### Algorithm

1. Receive key.
2. Compute hash index.
3. Replace value with None.

### Code

```python
def remove(self,key):
    h = self.get_hash(key)
    self.arr[h] = None
```

### Example

```python
t.remove("march 6")
```

### Complexity

```text
O(1)
```

Average Case

---

# Example Execution

```python
t = HashTable()

t.add("march 6",320)
t.add("march 7",340)
t.add("march 8",470)
t.add("march 9",510)
t.add("march 10",100)

t.get("march 9")
t.get("march 8")
t.get("march 7")

t.remove("march 8")

print(t.arr)

t.get("march 8")
```

---

# Time Complexity Table

| Operation | Complexity |
|------------|------------|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |
| Hash Calculation | O(k) |

Where:

```text
k = length of key
```

Example:

```python
"march 6"
```

Length:

```text
7
```

The hash function must process every character.

---

# Advantages of Hash Tables

- Extremely fast lookup.
- Efficient insertion.
- Efficient deletion.
- Direct access using keys.
- Foundation of Python dictionaries.
- Scales well for large datasets.

---

# Limitations of This Implementation

This implementation is intentionally simplified for learning purposes.

Current limitations:

### Fixed Size

```python
self.MAX = 50
```

The table cannot grow automatically.

---

### Only Stores Values

```python
self.arr[h] = value
```

The key itself is not stored.

---

### No Collision Handling

If two different keys generate the same index:

```text
Both try to use same bucket
```

Problems may occur.

Collision handling techniques will be implemented later.

---

# Real-World Applications of Hash Tables

- Python Dictionaries (`dict`)
- Python Sets (`set`)
- Database Indexing
- DNS Lookup
- Caching Systems
- Session Management
- Password Verification
- Search Engines
- Compilers
- Routing Tables

---

# Relationship Between Hash Table and Dictionary

A Hash Table is the underlying data structure used to build a Dictionary.

Our current implementation:

```python
t.add(key,value)
t.get(key)
t.remove(key)
```

Dictionary-style syntax:

```python
stock["march 6"] = 320
print(stock["march 6"])
del stock["march 6"]
```

By using Python's special methods:

```python
__setitem__()
__getitem__()
__delitem__()
```

we can make a Hash Table behave like a Dictionary.

---

# Summary

- Hash Table stores data using Key-Value Pairs.
- A Hash Function converts keys into array indices.
- Data is stored inside buckets of an array.
- Insert, Search, and Delete operations are O(1) on average.
- Python Dictionaries are built using Hash Tables.
- This implementation demonstrates the fundamental working of a Hash Table without collision handling.
- Collision handling and advanced features are the next step toward building a complete dictionary.