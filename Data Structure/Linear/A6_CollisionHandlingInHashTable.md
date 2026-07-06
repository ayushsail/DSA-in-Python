# Collision Handling in Hash Table

## What is Collision?

A **collision** occurs when two or more different keys produce the same hash value and therefore try to occupy the same index (bucket) in a hash table.

### Example

Suppose the hash table size is **10**.

```
Hash("march 6")  = 9
Hash("march 17") = 9
```

Both keys want to be stored at index **9**.

```
Index

0
1
2
3
4
5
6
7
8
9  ← Collision
```

Since only one element can occupy a bucket (in a simple array implementation), we need a **Collision Handling Technique**.

---

# Collision Handling Techniques

There are several techniques used to resolve collisions.

| Method | Description |
|---------|-------------|
| Chaining | Store multiple elements in the same bucket using another data structure (usually Linked List or Dynamic Array). |
| Linear Probing | Search sequentially for the next empty bucket. |
| Quadratic Probing | Search using quadratic increments (1², 2², 3²...). |
| Double Hashing | Use another hash function to determine the next bucket. |

The first two methods are the most common and easiest to understand.

---

# 1. Chaining

## Overview

Instead of storing a single value at each index, every bucket stores another collection (usually a Linked List or Dynamic Array).

```
Index

0
1
2
3
4
5
6
7
8
9 ─────►
         ┌────────────────────────────┐
         │ ("march 6",320)            │
         │ ("march 17",520)           │
         │ ("march 27",650)           │
         └────────────────────────────┘
```

Multiple keys can exist in the same bucket.

---

## Advantages

- Very simple implementation.
- Easy insertion.
- Deletion is straightforward.
- No clustering problem.
- Table never becomes completely full (until memory runs out).

---

## Disadvantages

- Extra memory required.
- Searching becomes slower if many elements collide.
- Cache performance is worse than open addressing.

---

# Chaining Algorithm

## ADD

### Algorithm

1. Calculate hash value.
2. Go to the corresponding bucket.
3. Traverse every tuple in that bucket.
4. If key already exists
    - Update its value.
5. Otherwise
    - Append new `(key, value)` tuple.

---

## GET

### Algorithm

1. Calculate hash value.
2. Traverse every tuple in that bucket.
3. If key matches
    - Return value.
4. If traversal finishes
    - Key not found.

---

## REMOVE

### Algorithm

1. Calculate hash value.
2. Traverse every tuple.
3. If key matches
    - Delete that tuple.
4. Otherwise
    - Key not found.

---

## Time Complexity (Chaining)

| Operation | Average | Worst |
|-----------|---------|--------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

Average complexity remains O(1) when the hash function distributes keys uniformly.

---

# 2. Linear Probing (Open Addressing)

## Overview

Instead of storing multiple values in one bucket, we search for the next available empty bucket.

```
Hash("march 6") = 9
```

```
Index

0
1
2
3
4
5
6
7
8
9  ("march 6")
```

Now suppose

```
Hash("march 17") = 9
```

Bucket 9 is occupied.

Linear probing checks

```
9 → 0 → 1 → 2 → 3 → ...
```

until an empty bucket is found.

```
Index

0 ("march 17")
1
2
3
4
5
6
7
8
9 ("march 6")
```

---

## Probe Sequence

Your implementation creates the probe sequence using

```python
[*range(index, len(arr))] + [*range(0, index)]
```

Example

```
Index = 5
Array Size = 10
```

Probe sequence

```
5 → 6 → 7 → 8 → 9 → 0 → 1 → 2 → 3 → 4
```

Every bucket is visited exactly once.

---

# Why Tombstones are Required?

Suppose

```
Index

9 → ("march 6")
0 → ("march 17")
```

Both keys hash to index 9.

If we remove

```
("march 6")
```

by replacing it with

```
None
```

the table becomes

```
9 → None
0 → ("march 17")
```

Now searching for `"march 17"` starts at index 9.

Since index 9 is empty, the search incorrectly concludes that the key does not exist.

This breaks the probing chain.

---

## Tombstone (Deleted Marker)

Instead of replacing a deleted element with

```
None
```

replace it with

```
DELETED
```

```
9 → DELETED
0 → ("march 17")
```

Now searching continues past the deleted bucket.

---

# find_slot()

## Purpose

Find the correct position for inserting a key.

It handles

- Empty bucket
- Deleted bucket
- Updating existing key
- Hash table full

---

## Algorithm

### Step 1

Generate probe sequence.

```
hash(key)

↓

Probe Range
```

---

### Step 2

Initialize

```
deleted_index = None
```

---

### Step 3

Traverse every bucket.

---

### Case 1

Bucket is empty.

```
None
```

If a deleted bucket was previously found

Return that deleted bucket.

Otherwise

Return current bucket.

---

### Case 2

Bucket contains

```
DELETED
```

Remember its index.

Continue probing.

Do NOT stop because the key may still exist further in the probe sequence.

---

### Case 3

Key already exists.

Return that bucket.

This allows updating existing values.

---

### Case 4

No empty bucket exists.

Raise

```
Hashmap Full
```

---

# ADD Algorithm

1. Compute hash.
2. Call `find_slot()`.
3. Store `(key, value)` at returned index.

---

# GET Algorithm

1. Compute hash.
2. Generate probe sequence.
3. Traverse each bucket.

### If bucket is

```
None
```

Stop searching.

Key does not exist.

---

### If bucket is

```
DELETED
```

Continue searching.

---

### If key matches

Return value.

---

# REMOVE Algorithm

1. Compute hash.
2. Generate probe sequence.
3. Traverse buckets.

### If bucket is

```
None
```

Key not found.

---

### If bucket is

```
DELETED
```

Continue probing.

---

### If key matches

Replace tuple with

```
DELETED
```

Do NOT replace it with `None`.

---

# Time Complexity (Linear Probing)

| Operation | Average | Worst |
|-----------|---------|--------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case occurs when the table becomes heavily occupied.

---

# Chaining vs Linear Probing

| Feature | Chaining | Linear Probing |
|----------|----------|----------------|
| Extra Memory | Yes | No |
| Cache Friendly | No | Yes |
| Easy Deletion | Yes | More Complex |
| Uses Linked List | Yes | No |
| Can Become Full | Practically No | Yes |
| Needs Tombstones | No | Yes |
| Suffers from Clustering | No | Yes (Primary Clustering) |

---

# Other Collision Handling Methods

## Quadratic Probing

Instead of checking

```
h + 1
h + 2
h + 3
```

it checks

```
h + 1²
h + 2²
h + 3²
```

Example

```
Hash = 5

5
↓

6
↓

9
↓

14
```

(modulo table size)

### Advantages

- Reduces primary clustering.

### Disadvantages

- May not visit every bucket.
- Slightly more complicated.

---

## Double Hashing

Uses a second hash function.

```
Index =

(Hash1(key) + i × Hash2(key)) % TableSize
```

Every collision uses a different step size.

### Advantages

- Best distribution.
- Very little clustering.

### Disadvantages

- More computationally expensive.
- Requires two hash functions.

---

# Complexity Summary

| Technique | Insert | Search | Delete |
|------------|--------|---------|--------|
| Chaining | O(1) Avg | O(1) Avg | O(1) Avg |
| Linear Probing | O(1) Avg | O(1) Avg | O(1) Avg |
| Quadratic Probing | O(1) Avg | O(1) Avg | O(1) Avg |
| Double Hashing | O(1) Avg | O(1) Avg | O(1) Avg |

Worst-case complexity for all methods is **O(n)**.

---

# Key Takeaways

- A collision occurs when multiple keys generate the same hash index.
- Chaining stores multiple elements inside the same bucket.
- Linear Probing searches sequentially for the next available bucket.
- Never replace a deleted element with `None` in Linear Probing.
- Use a **Tombstone (`DELETED`)** marker to preserve the probing sequence.
- `find_slot()` is responsible for finding the correct insertion position while supporting updates and deleted buckets.
- Good hash functions and maintaining a low load factor are essential for keeping operations close to **O(1)**.