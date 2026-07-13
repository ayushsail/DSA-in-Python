# Binary Tree & Binary Search Tree (BST)

---

# 1. What is a Binary Tree?

A **Binary Tree** is a non-linear hierarchical data structure in which each node can have **at most two children**.

The two children are called:

- Left Child
- Right Child

Unlike Linked Lists, Trees are used to represent hierarchical relationships.

Example:

```text
          A
        /   \
       B     C
      / \   /
     D   E F
```

---

# Why do we use Trees?

Trees are used whenever data has a hierarchical relationship.

Examples:

- File Explorer
- Organization Structure
- HTML DOM
- Folder Structure
- Decision Trees
- Database Indexing
- Binary Search Tree
- Heaps
- Trie
- Expression Trees

---

# Advantages

- Fast Searching
- Fast Insertion
- Fast Deletion
- Hierarchical Storage
- Efficient Traversals
- Dynamic Size
- Better than Linked List for searching

---

# Disadvantages

- More memory than Arrays
- Recursive algorithms can be difficult
- Worst-case BST becomes a Linked List

---

# Binary Tree Terminology

## 1. Node

A single element of a tree.

```text
    10
```

---

## 2. Root Node

Top-most node.

```text
      10
```

Only one root exists.

---

## 3. Parent Node

Node having children.

```text
      10
     /
    5
```

10 is parent of 5.

---

## 4. Child Node

Node connected below a parent.

```text
      10
     /
    5
```

5 is child of 10.

---

## 5. Leaf Node

Node having no children.

```text
      10
     / \
    5   20
```

Leaf Nodes:

- 5
- 20

---

## 6. Internal Node

Node having at least one child.

```text
      10
     /
    5
   /
  2
```

Internal Nodes:

- 10
- 5

---

## 7. Edge

Connection between two nodes.

```text
10 ----> 5
```

One connection = One edge.

---

## 8. Path

Sequence of connected nodes.

```text
10 → 5 → 2
```

---

## 9. Path Length

Number of edges.

```text
10 → 5 → 2
```

Edges = 2

---

## 10. Level

Distance from root.

```text
        10
       /  \
      5    20
     /
    2
```

Level 0

```
10
```

Level 1

```
5 20
```

Level 2

```
2
```

---

## 11. Depth

Number of edges from root to node.

Example:

```
Depth(root) = 0
Depth(5) = 1
Depth(2) = 2
```

---

## 12. Height of Node

Longest path from that node to a leaf.

Example

```text
      10
     /
    5
   /
  2
```

Height(10) = 2

Height(5) = 1

Height(2) = 0

---

## 13. Height of Tree

Height of Root.

---

## 14. Ancestors

Nodes above a node.

```text
10
|
5
|
2
```

Ancestors of 2:

- 10
- 5

---

## 15. Descendants

Nodes below a node.

```text
10
|
5
|
2
```

Descendants of 10:

- 5
- 2

---

## 16. Siblings

Children having same parent.

```text
      10
     / \
    5   20
```

5 and 20 are siblings.

---

## 17. Subtree

Every node itself forms a tree.

```text
      10
     / \
    5   20
```

Subtree of 5

```text
5
```

Subtree of 20

```text
20
```

---

# Types of Binary Trees

## 1. Full Binary Tree

Every node has either

- 0 children
- 2 children

---

## 2. Complete Binary Tree

- Every level completely filled except possibly last.
- Last level filled from left.

Used in Heaps.

---

## 3. Perfect Binary Tree

Every internal node has 2 children.

All leaf nodes at same level.

---

## 4. Balanced Binary Tree

Height difference between left and right subtree remains small.

Searching is fast.

Examples:

- AVL Tree
- Red Black Tree

---

## 5. Degenerate (Skewed) Tree

Every node has only one child.

Looks like Linked List.

Worst case.

---

# Binary Tree Formulas

Suppose Height = h

---

Maximum Nodes

```
2^(h+1) - 1
```

---

Maximum Nodes at Level L

```
2^L
```

---

Maximum Leaf Nodes

```
2^h
```

---

Minimum Height

```
⌈ log₂(n+1) ⌉ - 1
```

---

Edges

```
Nodes - 1
```

---

Null Links

```
n + 1
```

---

Time Complexity

Traversal

```
O(n)
```

Searching (General Binary Tree)

```
O(n)
```

---

# Tree Traversals

## Inorder (LNR)

```
Left -> Node -> Right
```

BST produces sorted order.

---

## Preorder (NLR)

```
Node -> Left -> Right
```

Useful for copying tree.

---

## Postorder (LRN)

```
Left -> Right -> Node
```

Useful for deleting tree.

---

# 2. What is Binary Search Tree (BST)?

A **Binary Search Tree (BST)** is a Binary Tree that follows a special ordering rule.

For every node:

```
Left Subtree < Root < Right Subtree
```

Duplicates are usually not allowed (your implementation ignores duplicates).

Example:

```text
          50
        /    \
      30      70
     / \      / \
   20  40   60  80
```

---

# Advantages of BST

- Fast Searching
- Fast Insertion
- Fast Deletion
- Maintains Sorted Data
- Efficient Range Queries

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

Worst case occurs when BST becomes skewed.

---

# 3. BST Implementation Algorithms

## Add Node

- Compare new value with current node.
- If equal, ignore (duplicate).
- If smaller:
  - Move left.
  - Create node if left is empty.
- If greater:
  - Move right.
  - Create node if right is empty.
- Continue recursively until inserted.

---

## Search Node

- Compare target with current node.
- If equal → Found.
- If smaller → Search left subtree.
- If greater → Search right subtree.
- If subtree is empty → Not Found.

---

## Inorder Traversal (LNR)

- Visit Left Subtree.
- Visit Current Node.
- Visit Right Subtree.
- Returns elements in ascending order for BST.

---

## Preorder Traversal (NLR)

- Visit Current Node.
- Visit Left Subtree.
- Visit Right Subtree.

Useful for copying or serializing a tree.

---

## Postorder Traversal (LRN)

- Visit Left Subtree.
- Visit Right Subtree.
- Visit Current Node.

Useful for deleting/freeing a tree.

---

## Find Minimum

- Move continuously to the left child.
- Stop when no left child exists.
- Return current node's value.

---

## Find Maximum

- Move continuously to the right child.
- Stop when no right child exists.
- Return current node's value.

---

## Delete Node

There are **three deletion cases**:

### Case 1: Leaf Node

- Node has no children.
- Return `None`.

---

### Case 2: One Child

- Return the existing child.
- Parent automatically connects to it.

---

### Case 3: Two Children

- Find the minimum value in the right subtree (Inorder Successor).
- Replace current node's data with successor.
- Delete successor recursively from right subtree.

---

## Build Tree

- Create root using first element.
- Insert remaining elements one by one using `add_node()`.
- Return the root node.

---

# Important Expressions

## Recursive Left Search

```python
self.left = self.left.delete(data)
```

---

## Recursive Right Search

```python
self.right = self.right.delete(data)
```

---

## Replace Node with Right Child

```python
return self.right
```

---

## Replace Node with Left Child

```python
return self.left
```

---

## Delete Leaf

```python
return None
```

---

## Find Inorder Successor

```python
min_val = self.right.find_min()
```

---

## Replace Data

```python
self.data = min_val
```

---

## Delete Successor

```python
self.right = self.right.delete(min_val)
```

---

## Update Root After Deletion

Always write:

```python
root = root.delete(value)
```

Reason:

- If the root changes, the returned node becomes the new root.
- If the root does not change, the same root is returned.

---

# Extra Required Information

## Duplicate Handling

Your implementation ignores duplicate values:

```python
if self.data == data:
    return
```

---

## BST Property

Every node satisfies:

```
Left < Node < Right
```

---

## Why Inorder Gives Sorted Order?

Because BST always visits:

```
Left
↓

Node
↓

Right
```

which naturally processes values in ascending order.

---

## Why Build Tree Uses First Element?

The first element becomes the root.

Every remaining element is inserted according to BST rules.

---

## Recursive Nature

Most BST operations are naturally recursive because every subtree is itself a BST.

---

## Applications of BST

- Searching data
- Database indexing
- Symbol tables
- File systems
- Dictionary implementation
- Range searching
- Auto-complete systems (variants)
- In-memory ordered collections

---

# Complexity Summary

| Operation | Time |
|-----------|------|
| Insert | O(log n) average |
| Search | O(log n) average |
| Delete | O(log n) average |
| Find Min | O(log n) |
| Find Max | O(log n) |
| Traversals | O(n) |
| Space (Recursive Stack) | O(h) |

Where **h** is the height of the tree.
