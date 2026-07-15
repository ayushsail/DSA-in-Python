# 🌳 Binary Search Tree (BST)

## 📌 What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a **Binary Tree** that follows one extra ordering rule at every single node:

```
Left Subtree < Root < Right Subtree
```

This ordering rule is what turns a plain Binary Tree into a structure that supports fast searching — at every node, comparing the target value against the current node tells you which entire subtree to discard.

Duplicates are usually not allowed. This implementation silently ignores duplicate inserts.

Example:

```text
          50
        /    \
      30      70
     / \      / \
   20  40   60  80
```

---

# Characteristics

- A specialized Binary Tree — every node has at most 2 children.
- Every node satisfies `Left < Node < Right`.
- Every subtree of a BST is itself a valid BST (recursive property).
- No parent reference is stored in this implementation — only `left` and `right`.
- Inorder traversal always yields values in ascending sorted order.

---

# Advantages

- Fast Searching
- Fast Insertion
- Fast Deletion
- Maintains Sorted Data
- Efficient Range Queries

---

# Disadvantages

- Worst case (skewed insert order) degrades to a Linked List → O(n) operations.
- Not self-balancing — repeated inserts of increasing/decreasing values create a skewed tree.
- Deletion logic is more involved than insertion (must handle 3 distinct cases).

---

# Time Complexity

| Operation | Average | Worst |
|-----------|---------|--------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Find Max | O(log n) | O(n) |
| Find Min | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

Worst case occurs when the BST becomes skewed (e.g., inserting already-sorted data), at which point the tree behaves exactly like a Linked List and every operation must walk through all `n` nodes instead of eliminating half the tree at each comparison.

---

# Node Structure

Each node in this implementation stores three pieces of information:

```python
data
left
right
```

```text
BinarySearchTreeNode
│
├── data   → value stored in the node
├── left   → reference to left child (values smaller than data)
└── right  → reference to right child (values larger than data)
```

Unlike the general Binary Tree implementation, a BST node does **not** track a `parent` reference — deletion and insertion here rely purely on recursive comparisons against `data`, so upward traversal is never needed.

---

# BST Implementation Algorithms

## 1. Add Node

### Purpose

Insert a new value into the tree while preserving the BST property.

### Algorithm

```
Compare new value with current node's data

If equal
    Ignore (duplicate) — do nothing

If smaller
    If left child exists
        Recurse into left subtree
    Else
        Create new node as left child

If greater
    If right child exists
        Recurse into right subtree
    Else
        Create new node as right child
```

### Time Complexity

```
O(log n) average, O(n) worst (skewed tree)
```

### Code

```python
if self.data == data: return       # duplicate case
elif data < self.data:
    if self.left: self.left.add_node(data)
    else: self.left = BinarySearchTreeNode(data)
else:
    if self.right: self.right.add_node(data)
    else: self.right = BinarySearchTreeNode(data)
```

---

## 2. Search Node

### Purpose

Determine whether a given value exists in the tree.

### Algorithm

```
Compare target with current node's data

If equal → Found (return True)

If smaller → search left subtree
    If left subtree is empty → Not Found

If greater → search right subtree
    If right subtree is empty → Not Found
```

### Time Complexity

```
O(log n) average, O(n) worst
```

---

## 3. Inorder Traversal (LNR)

### Purpose

Visit nodes in ascending sorted order.

### Algorithm

```
Visit Left Subtree
Visit Current Node
Visit Right Subtree
```

Because every left value is smaller and every right value is larger than the current node, this traversal order naturally produces values in ascending order.

### Time Complexity

```
O(n)
```

---

## 4. Preorder Traversal (NLR)

### Purpose

Visit the current node before its subtrees — useful for copying or serializing a tree so it can be rebuilt in the same shape.

### Algorithm

```
Visit Current Node
Visit Left Subtree
Visit Right Subtree
```

### Time Complexity

```
O(n)
```

---

## 5. Postorder Traversal (LRN)

### Purpose

Visit children before the parent — useful for safely deleting/freeing a tree bottom-up.

### Algorithm

```
Visit Left Subtree
Visit Right Subtree
Visit Current Node
```

### Time Complexity

```
O(n)
```

---

## 6. Find Minimum

### Purpose

Find the smallest value in the (sub)tree.

### Algorithm

```
Move continuously to the left child
Stop when no left child exists
Return current node's value
```

### Time Complexity

```
O(log n) average, O(h) worst
```

---

## 7. Find Maximum

### Purpose

Find the largest value in the (sub)tree.

### Algorithm

```
Move continuously to the right child
Stop when no right child exists
Return current node's value
```

### Time Complexity

```
O(log n) average, O(h) worst
```

---

## 8. Delete Node

### Purpose

Remove a value from the tree while preserving the BST property. This is the most involved operation, split into three cases.

### Algorithm

```
If data < current node's data
    Recurse into left subtree
    (raise error if left subtree doesn't exist — data not found)

Else if data > current node's data
    Recurse into right subtree
    (raise error if right subtree doesn't exist — data not found)

Else (data == current node's data — this is the node to delete):

    Case 1: No children (leaf node)
        Return None

    Case 2: Only left child exists
        Return left child (parent reconnects directly to it)

    Case 3: Only right child exists
        Return right child (parent reconnects directly to it)

    Case 4: Two children exist
        Find the minimum value in the right subtree (inorder successor)
        Replace current node's data with that successor value
        Recursively delete the successor from the right subtree

Return self (the — possibly modified — current node)
```

### Time Complexity

```
O(log n) average, O(n) worst
```

### Why the Inorder Successor?

The smallest value in the right subtree is guaranteed to be larger than everything in the left subtree and smaller than everything else in the right subtree — so swapping it into the deleted node's position preserves the BST ordering rule everywhere.

An equally valid alternative (commented out in the implementation) is to use the **inorder predecessor** instead — the maximum value of the left subtree.

---

## 9. Build Tree

### Purpose

Construct a BST from a plain list of elements.

### Algorithm

```
If the list is empty
    Return None

Create the root node using the first element

For every remaining element in the list
    Insert it using add_node()

Return the root node
```

### Time Complexity

```
O(n log n) average (n inserts, each O(log n))
O(n²) worst case (already-sorted input → skewed tree)
```

---

# Important Expressions

## Recursive Left Search

```python
self.left = self.left.delete(data)
```

## Recursive Right Search

```python
self.right = self.right.delete(data)
```

## Replace Node with Right Child

```python
return self.right
```

## Replace Node with Left Child

```python
return self.left
```

## Delete Leaf

```python
return None
```

## Find Inorder Successor

```python
min_val = self.right.find_min()
```

## Replace Data

```python
self.data = min_val
```

## Delete Successor

```python
self.right = self.right.delete(min_val)
```

## Update Root After Deletion

Always write:

```python
root = root.delete(value)
```

Reason:

- If the root itself changes (or is removed), the returned node becomes the new root.
- If the root doesn't change, the same root object is simply returned again.
- Since `delete()` may return `None`, a different child, or `self`, the caller must always reassign the variable holding the root — never assume the root stays the same object.

---

# Extra Information

## Duplicate Handling

This implementation silently ignores duplicate values on insert:

```python
if self.data == data:
    return
```

No error is raised and no second node is created.

## BST Property

Every node in the tree must satisfy:

```
Left < Node < Right
```

This must hold true not just for the root, but for **every node at every level** — which is why each subtree of a BST is itself a valid BST.

## Why Inorder Gives Sorted Order

Because a BST always visits nodes in the sequence:

```
Left
  ↓
Node
  ↓
Right
```

and since `Left < Node < Right` holds at every step, this traversal order naturally processes values from smallest to largest.

## Why Build Tree Uses the First Element

The first element in the input list becomes the root simply because it's inserted first, before any comparisons are possible. Every remaining element is then inserted according to normal BST rules — meaning the final tree shape (and therefore its height) depends heavily on the **order** elements arrive in, not just which values are present.

## Recursive Nature

Almost every BST operation (insert, search, delete, traversal, min/max) is naturally recursive, because every subtree is itself a complete, independent BST that the same logic can be applied to.

---

# Methods Implemented

- `add_node()`
- `search_tree()`
- `inorder_traversal()`
- `preorder_traversal()`
- `postorder_traversal()`
- `find_min()`
- `find_max()`
- `delete()`
- `build_tree()` (module-level helper function)

---

# Overall Complexity

| Method | Average | Worst |
|---------|---------|-------|
| add_node | O(log n) | O(n) |
| search_tree | O(log n) | O(n) |
| delete | O(log n) | O(n) |
| find_min | O(log n) | O(n) |
| find_max | O(log n) | O(n) |
| inorder_traversal | O(n) | O(n) |
| preorder_traversal | O(n) | O(n) |
| postorder_traversal | O(n) | O(n) |
| build_tree | O(n log n) | O(n²) |
| Space (Recursive Stack) | O(h) | O(h) |

Where **h** is the height of the tree and **n** is the total number of nodes.

---

# Applications of BST

- Searching data efficiently
- Database indexing
- Symbol tables (compilers/interpreters)
- File systems
- Dictionary implementation
- Range searching
- Auto-complete systems (variants)
- In-memory ordered collections

---

> **Note:** This implementation is a **plain (unbalanced) Binary Search Tree**. It does not automatically rebalance itself, so worst-case performance degrades to O(n) on skewed insert patterns (e.g., inserting already-sorted data). Self-balancing variants such as AVL Trees or Red-Black Trees solve this by rotating nodes to keep height close to `O(log n)`.