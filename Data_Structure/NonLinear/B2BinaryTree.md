# 🌳 Binary Tree

## 📌 What is a Binary Tree?

A **Binary Tree** is a **non-linear hierarchical data structure** in which each node can have **at most two children**.

The two children are called:

- Left Child
- Right Child

Unlike a General Tree (where a node can have any number of children stored in a list), a Binary Tree restricts every node to exactly two possible child slots — `left` and `right`. This restriction is what makes Binary Trees the foundation for more specialized structures like Binary Search Trees, Heaps, and AVL Trees.

Example:

```text
          A
        /   \
       B     C
      / \   /
     D   E F
```

---

# Characteristics

- Hierarchical data structure.
- Consists of **nodes** connected by **edges**.
- Root node has no parent.
- Every node (except root) has exactly one parent.
- Every node has **at most 2 children** — left and right.
- No cycles are allowed.
- Connected graph.

---

# Why do we use Binary Trees?

Binary Trees are used whenever data has a hierarchical relationship AND each element naturally branches into at most two directions.

Examples:

- File Explorer (simplified hierarchies)
- Binary Search Trees
- Heaps (Min-Heap / Max-Heap)
- Expression Trees (operators have at most 2 operands)
- Huffman Coding Trees
- Decision Trees (binary decisions)

---

# Advantages

- Fast Searching (when balanced)
- Fast Insertion
- Fast Deletion
- Hierarchical Storage
- Efficient Traversals
- Dynamic Size
- Simple recursive structure — every subtree is itself a Binary Tree

---

# Disadvantages

- More memory than Arrays (extra pointers per node)
- Recursive algorithms can be difficult to reason about
- Worst-case (skewed) tree behaves like a Linked List
- No inherent ordering (a plain Binary Tree does not guarantee sorted data — that's what a BST adds)

---

# Binary Tree Terminology

## 1. Node

A single element of a tree.

```text
    10
```

---

## 2. Root Node

Top-most node. Only one root exists.

```text
      10
```

---

## 3. Parent Node

Node having children.

```text
      10
     /
    5
```

10 is the parent of 5.

---

## 4. Child Node

Node connected below a parent.

```text
      10
     /
    5
```

5 is the child of 10.

---

## 5. Leaf Node

Node having no children.

```text
      10
     / \
    5   20
```

Leaf Nodes: `5`, `20`

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

Internal Nodes: `10`, `5`

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

Number of edges in a path.

```text
10 → 5 → 2
```

Edges = 2

---

## 10. Level

Distance (number of edges) from the root.

```text
        10
       /  \
      5    20
     /
    2
```

- Level 0: `10`
- Level 1: `5, 20`
- Level 2: `2`

---

## 11. Depth

Number of edges from root to that node (same value as Level for a given node).

```text
Depth(root) = 0
Depth(5) = 1
Depth(2) = 2
```

---

## 12. Height of Node

Longest path (in edges) from that node down to a leaf.

```text
      10
     /
    5
   /
  2
```

- Height(10) = 2
- Height(5) = 1
- Height(2) = 0

---

## 13. Height of Tree

Height of the Root node.

---

## 14. Ancestors

All nodes above a given node, up to the root.

```text
10
|
5
|
2
```

Ancestors of `2`: `10`, `5`

---

## 15. Descendants

All nodes below a given node.

```text
10
|
5
|
2
```

Descendants of `10`: `5`, `2`

---

## 16. Siblings

Children sharing the same parent.

```text
      10
     / \
    5   20
```

`5` and `20` are siblings.

---

## 17. Subtree

Every node is itself the root of its own smaller tree.

```text
      10
     / \
    5   20
```

Subtree of `5` → `5`
Subtree of `20` → `20`

---

# Types of Binary Trees

## 1. Full Binary Tree

Every node has either 0 or 2 children (never just 1).

## 2. Complete Binary Tree

Every level is completely filled except possibly the last, and the last level is filled from left to right. Used in Heaps.

## 3. Perfect Binary Tree

Every internal node has exactly 2 children, and all leaf nodes sit at the same level.

## 4. Balanced Binary Tree

Height difference between left and right subtrees stays small at every node, keeping searches fast. Examples: AVL Tree, Red-Black Tree.

## 5. Degenerate (Skewed) Tree

Every node has only one child. Behaves exactly like a Linked List — the worst case.

---

# Binary Tree Formulas

Suppose Height = `h`

| Quantity | Formula |
|----------|---------|
| Maximum Nodes | `2^(h+1) - 1` |
| Maximum Nodes at Level L | `2^L` |
| Maximum Leaf Nodes | `2^h` |
| Minimum Height (for n nodes) | `⌈ log₂(n+1) ⌉ - 1` |
| Edges | `Nodes - 1` |
| Null Links | `n + 1` |

---

# Time Complexity (General Binary Tree)

| Operation | Complexity |
|-----------|------------|
| Traversal | O(n) |
| Searching | O(n) |
| Add Child (left/right) | O(1) |
| Remove Child | O(1) |
| Find | O(n) |
| Get Height | O(n) |
| Get Level | O(h) |
| Get Root / Get Path | O(h) |
| Count Nodes | O(n) |

Where **h** is the height of the tree and **n** is the total number of nodes. Because a plain Binary Tree has no ordering rule, Searching and Finding must visit nodes in the worst case — unlike a BST, they cannot rely on comparisons to eliminate half the tree at each step.

---

# Node Structure

Each node in this implementation stores four pieces of information:

```python
data
parent
left
right
```

```text
BinaryTree (Node)
│
├── data    → value stored in the node
├── parent  → reference to parent node (None for root)
├── left    → reference to left child (None if absent)
└── right   → reference to right child (None if absent)
```

Storing a `parent` reference (unlike the BST implementation, which only tracks `left`/`right`) is what allows this Binary Tree to support upward operations like `get_root()`, `get_level()`, and `get_path()` without needing to search from the top every time.

---

# Implementation Algorithms

## 1. Add Left / Add Right

### Purpose

Attach a new node as the left or right child of the current node.

### Algorithm

```
If child is not a BinaryTree instance
    Raise Exception

If child is the same object as self
    Raise ValueError (a node cannot be its own child)

If child already has a parent
    Raise ValueError (already attached elsewhere)

If the target slot (left/right) is already occupied
    Raise ValueError

Set child.parent = self
Set self.left (or self.right) = child
```

### Time Complexity

```
O(1)
```

### Code

```python
self.left.add_left(child)   # or add_right
```

---

## 2. Remove Left / Remove Right

### Purpose

Detach the left or right child from the current node and return it.

### Algorithm

```
If the target slot is empty
    Return None

Store the child in a temporary variable
Clear the child's parent reference
Clear the slot (left/right = None)
Return the stored child
```

### Time Complexity

```
O(1)
```

---

## 3. Display Tree

### Purpose

Print the tree sideways in a readable hierarchical form (right subtree on top, left subtree below, indentation shows depth).

### Algorithm

```
Recursively display the right subtree at level+1

Print the current node, indented by level

Recursively display the left subtree at level+1
```

### Time Complexity

```
O(n)
```

---

## 4. Find

### Purpose

Search the tree for a node containing the given data.

### Algorithm

```
If current node's data matches
    Return current node

If left subtree exists
    Search left subtree; if found, return it

If right subtree exists
    Search right subtree; if found, return it

Return None
```

### Time Complexity

```
O(n)
```

This is a **Preorder-style DFS search** — it checks the current node before either subtree.

---

## 5. Contains

### Purpose

Return `True`/`False` for whether the data exists in the tree.

### Algorithm

```
Return find(data) is not None
```

### Time Complexity

```
O(n)
```

---

## 6. Is Root

### Purpose

Check whether the current node is the root.

### Algorithm

```
Return parent is None
```

### Time Complexity

```
O(1)
```

---

## 7. Is Leaf

### Purpose

Check whether the current node has no children.

### Algorithm

```
Return left is None AND right is None
```

### Time Complexity

```
O(1)
```

---

## 8. Get Root

### Purpose

Return the root node, starting from any node in the tree.

### Algorithm

```
Start at current node

While node has a parent
    Move to parent

Return node
```

### Time Complexity

```
O(h)
```

---

## 9. Get Level

### Purpose

Return how many ancestors exist between this node and the root.

### Algorithm

```
level = 0
p = self.parent

While p is not None
    level += 1
    p = p.parent

Return level
```

### Time Complexity

```
O(h)
```

---

## 10. Get Height

### Purpose

Return the longest path (in edges) from this node down to a leaf.

### Algorithm

```
If node is a leaf
    Return 0

left_height = height of left subtree (0 if absent)
right_height = height of right subtree (0 if absent)

Return 1 + max(left_height, right_height)
```

### Time Complexity

```
O(n)
```

---

## 11. Get Path

### Purpose

Return the path from the root down to the current node as a readable string.

### Algorithm

```
Start at current node
path = []

While node is not None
    Append node.data to path
    Move to node.parent

Reverse path
Join elements with " --> "
```

### Time Complexity

```
O(h)
```

---

## 12. Count Node

### Purpose

Count the total number of nodes in the subtree rooted at the current node.

### Algorithm

```
count = 1   (count self)

If left subtree exists
    count += left.count_node()

If right subtree exists
    count += right.count_node()

Return count
```

### Time Complexity

```
O(n)
```

---

## 13. Count Leaf Node

### Purpose

Count how many leaf nodes exist in the subtree.

### Algorithm

```
count = 0

If current node is a leaf
    Return 1

If left subtree exists
    count += left.count_leaf_node()

If right subtree exists
    count += right.count_leaf_node()

Return count
```

### Time Complexity

```
O(n)
```

---

## 14. Count Internal Node

### Purpose

Count nodes that have at least one child (this includes the root, as long as it isn't a leaf).

### Algorithm

```
count = 1   (count self)

If current node is a leaf
    Return 0

If left subtree exists
    count += left.count_internal_node()

If right subtree exists
    count += right.count_internal_node()

Return count
```

### Time Complexity

```
O(n)
```

---

## 15. Clear (Detach)

### Purpose

Detach the current node (and its whole subtree) from its parent, without destroying the subtree itself — it still exists independently in memory.

### Algorithm

```
If current node is the root
    Raise ValueError (cannot detach root)

If current node is its parent's left child
    Set parent.left = None
Else
    Set parent.right = None

Set self.parent = None
```

### Time Complexity

```
O(1)
```

---

## 16. Clear (Destroy)

### Purpose

Recursively tear down an entire subtree, removing every internal reference so nothing remains connected.

### Algorithm

```
If left subtree exists
    Recursively destroy left subtree

If right subtree exists
    Recursively destroy right subtree

If current node is not root
    Detach current node from its parent

Clear self.parent, self.left, self.right
```

### Time Complexity

```
O(n)
```

---

# Tree Traversals

## DFS - Inorder (LNR)

```
Visit Left Subtree
Visit Current Node
Visit Right Subtree
```

For a plain Binary Tree this does **not** guarantee sorted output (that property only holds for a BST).

Time: `O(n)`

---

## DFS - Preorder (NLR)

```
Visit Current Node
Visit Left Subtree
Visit Right Subtree
```

Useful for copying or serializing a tree.

Time: `O(n)`

---

## DFS - Postorder (LRN)

```
Visit Left Subtree
Visit Right Subtree
Visit Current Node
```

Useful for deleting/freeing a tree, since children are cleaned up before the parent.

Time: `O(n)`

---

## BFS - Level Order

### Purpose

Visit the tree level by level, left to right, using a Queue.

### Algorithm

```
Create empty Queue
Enqueue root

While Queue is not empty
    Dequeue a node
    Visit (record) the node

    If node has a left child
        Enqueue left child

    If node has a right child
        Enqueue right child
```

### Time Complexity

```
O(n)
```

### Space Complexity

```
O(w)   where w = maximum width of the tree
```

This implementation relies on a Queue (`QueueLL`) built separately as a Linear Data Structure, imported into the Binary Tree module.

---

# DFS vs BFS

| DFS | BFS |
|------|------|
| Goes deep first | Goes level by level |
| Uses Recursion / Stack | Uses Queue |
| Space: O(h) | Space: O(w) |
| Good for subtree problems (height, count, path) | Good for shortest path & level-based problems |

---

# Methods Implemented

- `add_left()` / `add_right()`
- `remove_left()` / `remove_right()`
- `display()`
- `find()`
- `contains()`
- `is_root()`
- `is_leaf()`
- `get_root()`
- `get_level()`
- `get_height()`
- `get_path()`
- `count_node()`
- `count_leaf_node()`
- `count_internal_node()`
- `inorder_traversal()`
- `preorder_traversal()`
- `postorder_traversal()`
- `bfs_levelorder()`
- `clear_detach()`
- `clear_destroy()`

---

# Overall Complexity

| Method | Time |
|---------|------|
| add_left / add_right | O(1) |
| remove_left / remove_right | O(1) |
| display | O(n) |
| find | O(n) |
| contains | O(n) |
| is_root | O(1) |
| is_leaf | O(1) |
| get_root | O(h) |
| get_level | O(h) |
| get_height | O(n) |
| get_path | O(h) |
| count_node | O(n) |
| count_leaf_node | O(n) |
| count_internal_node | O(n) |
| inorder / preorder / postorder | O(n) |
| bfs_levelorder | O(n) |
| clear_detach | O(1) |
| clear_destroy | O(n) |

Where **h** is the height and **n** is the total number of nodes.

---

# Important Expressions

## Recursive Left/Right Attachment

```python
child.parent = self
self.left = child
```

## Detach a Subtree Without Destroying It

```python
node.clear_detach()
```

## Recursive Height Formula

```python
return 1 + max(left_height, right_height)
```

## Building a Path to Root

```python
path.reverse()
return " --> ".join(map(str, path))
```

---

# Applications

- File Explorer / Directory-like structures
- Binary Search Trees
- Heaps (Min-Heap / Max-Heap)
- Expression Trees (arithmetic parsing)
- Huffman Coding Trees
- Decision Trees with binary outcomes
- Game trees (binary branching decisions)

---

# Recursive Nature

Almost every Binary Tree operation is naturally recursive, because a subtree rooted at any node is itself a valid Binary Tree — the same algorithm applied to a smaller instance of the same problem.

---

> **Note:** This implementation is a **plain Binary Tree**, meaning nodes are attached manually via `add_left()` / `add_right()` with no ordering rule enforced. A **Binary Search Tree (BST)** builds on this same node shape but adds the constraint `Left < Node < Right`, which is documented separately.