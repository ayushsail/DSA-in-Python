 # 🌳 Tree (General Tree)

## 📌 What is a Tree?

A **Tree** is a **non-linear hierarchical data structure** consisting of nodes connected by edges.

Unlike arrays or linked lists, data in a tree is organized in **parent-child relationships**, making it suitable for representing hierarchical information such as:

- File Systems
- Organization Charts
- HTML/XML DOM
- Category Trees
- Decision Trees

A tree starts with a single node called the **Root**, and every other node is connected through exactly one parent (except the root).

---

## 🌳 Basic Tree Structure

```text
            ________ Electronics________
           |              |             |    
           |              |             |
        Laptop            |            TV
     /   |   \            |           /  |  \
 Mac ThinkPad Surface   Phone   Samsung LG Sony
                          | 
                        iPhone
```                     


---

# Characteristics

- Hierarchical data structure.
- Consists of **nodes** connected by **edges**.
- Root node has no parent.
- Every node (except root) has exactly one parent.
- A node may have zero or more children.
- No cycles are allowed.
- Connected graph.

---

# Terminology

## Root

Top-most node of the tree.

```text
Electronics
```

---

## Parent

Node directly above another node.

```text
Electronics
    |
 Laptop
```

Electronics is parent of Laptop.

---

## Child

Node directly below another node.

```text
Laptop
   |
 Mac
```

Mac is child of Laptop.

---

## Siblings

Nodes having the same parent.

```text
Laptop
Phone
TV
```

---

## Ancestors

All parents up to the root.

Ancestors of **Mac**

```text
Laptop
Electronics
```

---

## Descendants

All children, grandchildren, etc.

Descendants of **Laptop**

```text
Mac
ThinkPad
Surface
```

---

## Leaf Node

Node having **no children**.

Examples

```text
Mac
LG
Sony
```

---

## Internal Node

Any node having **at least one child**.

Examples

```text
Electronics
Laptop
TV
```

---

## Level

Number of ancestors from the root.

```text
Level 0 : Electronics

Level 1 : Laptop Phone TV

Level 2 : Mac ThinkPad Surface
```

---

## Height

Number of **edges** in the longest path from a node to any leaf.

Example

```text
Electronics = 2

Laptop = 1

Mac = 0
```

---

## Subtree

Every node itself is the root of another tree.

Example

```text
Laptop
├── Mac
├── ThinkPad
└── Surface
```

is a subtree.

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Add Child | O(1) |
| Remove Child | O(n) |
| Find | O(n) |
| Contains | O(n) |
| Get Height | O(n) |
| Count Nodes | O(n) |
| Count Leaf Nodes | O(n) |
| Count Internal Nodes | O(n) |
| Get Root | O(h) (h = height of tree) |
| Get Path | O(h) (h = height of tree) |
| DFS Traversal | O(n) |
| BFS Traversal | O(n) |

---

# Tree Implementation

Each node stores three pieces of information.

```python
data
children
parent
```

```text
TreeNode
│
├── data
├── children → list of child nodes
└── parent → parent node
```

Unlike Binary Trees, a General Tree stores its children inside a **list**, allowing any number of children.

---

# Tree Implementation Algorithms

## 1. Add Child

### Purpose

Attach a child node to the current node.

### Algorithm

```
If child already has a parent

    Raise Exception

Set child's parent to current node

Append child into children list
```

Time Complexity:

```
O(1)
```

---

## 2. Remove Child

### Purpose

Remove a node from the tree recursively.

### Algorithm

```
For every child

    If child matches

        Remove child

        Return removed node

    Otherwise

        Search inside child's subtree recursively

If not found

    Return None
```

Time Complexity

```
O(n)
```

---

## 3. Display Tree

### Purpose

Print the tree in hierarchical form.

### Algorithm

```
Print current node

For every child

    Display child recursively
```

Produces

```text
Electronics
    |___Laptop
        |___Mac
        |___ThinkPad
```

---

## 4. Find

### Purpose

Search a node recursively.

### Algorithm

```
If current node matches

    Return current node

Search every subtree

If found

    Return node

Otherwise

Return None
```

Time Complexity

```
O(n)
```

---

## 5. Contains

Returns

```
True
```

or

```
False
```

Internally uses

```
find()
```

---

## 6. Is Root

Checks

```
parent == None
```

Time

```
O(1)
```

---

## 7. Is Leaf

Checks whether

```
children list is empty
```

Time

```
O(1)
```

---

## 8. Get Level

Counts number of ancestors.

Algorithm

```
Move upward using parent

Increment level

Repeat until root
```

Time

```
O(h)
```

---

## 9. Get Height

Height is calculated recursively.

Algorithm

```
If node is leaf

    Return 0

Find maximum height among children

Return

1 + maximum child height
```

Time

```
O(n)
```

---

## 10. Count Nodes

Counts every node in subtree.

Algorithm

```
Count current node

Recursively count every child

Return total
```

Time

```
O(n)
```

---

## 11. Count Leaf Nodes

Algorithm

```
If current node is leaf

    Return 1

Recursively count leaves of every child

Return total
```

Time

```
O(n)
```

---

## 12. Count Internal Nodes

Algorithm

```
If current node is leaf

    Return 0

Count current node

Recursively count internal nodes

Return total
```

Time

```
O(n)
```

---

## 13. Get Root

Move upward until

```
parent == None
```

Return root.

Time

```
O(h)
```

---

## 14. Get Path

Returns path from root to current node.

Algorithm

```
Create empty list

Move upward using parent

Insert every node at beginning

Join list using arrows
```

Example

```text
Electronics
        ↓
Laptop
        ↓
Mac
```

returns

```text
Electronics --> Laptop --> Mac
```

---

## 15. Clear (Detach)

Removes all direct children.

Subtrees remain intact.

```text
Root

Children removed

Subtrees still exist independently
```

---

## 16. Clear (Destroy)

Recursively removes every node.

Algorithm

```
Destroy every child subtree

Remove parent reference

Clear children list
```

Entire subtree is deleted.

---

# Tree Traversals

Traversal means

> Visiting every node exactly once in a specific order.

---

## DFS (Depth First Search)

DFS explores one branch completely before moving to another.

Implemented using

- Recursion
- Stack

---

### DFS - Preorder

Visit parent before children.

Algorithm

```
Visit current node

For every child

    Preorder(child)
```

Example

```text
Electronics
Laptop
Mac
ThinkPad
Surface
Phone
TV
```

Time

```
O(n)
```

Space

```
O(h)
```

---

### DFS - Postorder

Visit children before parent.

Algorithm

```
For every child

    Postorder(child)

Visit current node
```

Example

```text
Mac
ThinkPad
Surface
Laptop
Phone
TV
Electronics
```

Time

```
O(n)
```

---

## BFS (Breadth First Search)

Visits tree level by level.

Uses a **Queue**.

Algorithm

```
Create Queue

Enqueue root

While queue not empty

    Dequeue node

    Visit node

    Enqueue all children
```

Traversal

```text
Electronics

Laptop
Phone
TV

Mac
ThinkPad
Surface
iPhone
Nothing
Samsung
LG
Sony
```

Time

```
O(n)
```

Space

```
O(w)
```

where

```
w = maximum width of tree
```

---

# DFS vs BFS

| DFS | BFS |
|------|------|
| Goes deep first | Goes level by level |
| Uses Recursion / Stack | Uses Queue |
| Space: O(h) | Space: O(w) |
| Good for subtree problems | Good for shortest path & level problems |

---

# Advantages

- Natural representation of hierarchical data.
- Efficient parent-child relationships.
- Dynamic size.
- Easy recursive algorithms.
- Foundation for Binary Trees, BSTs, Heaps, Tries, and File Systems.

---

# Disadvantages

- More memory than arrays.
- Recursive algorithms may consume stack space.
- Searching is O(n) in a General Tree.
- More complex implementation than linear structures.

---

# Applications

- File Systems
- HTML / XML DOM
- Organization Charts
- AI Decision Trees
- Game Scene Graphs
- Expression Trees
- Category Hierarchies
- Compiler Syntax Trees
- Menu Systems

---

# Methods Implemented

- add_child()
- remove_child()
- print_tree()
- find()
- contains()
- is_root()
- is_leaf()
- get_level()
- get_height()
- count_node()
- count_leaf_node()
- count_internal_node()
- get_root()
- get_path()
- clear_detach()
- clear_destroy()
- dfs_preorder()
- dfs_postorder()
- bfs_levelorder()

---

# Overall Complexity

| Method | Time |
|---------|------|
| add_child | O(1) |
| remove_child | O(n) |
| print_tree | O(n) |
| find | O(n) |
| contains | O(n) |
| is_root | O(1) |
| is_leaf | O(1) |
| get_level | O(h) |
| get_height | O(n) |
| count_node | O(n) |
| count_leaf_node | O(n) |
| count_internal_node | O(n) |
| get_root | O(h) |
| get_path | O(h) |
| clear_detach | O(k) |
| clear_destroy | O(n) |
| dfs_preorder | O(n) |
| dfs_postorder | O(n) |
| bfs_levelorder | O(n) |

---

> **Note:** This implementation is a **General Tree (N-ary Tree)**, where each node can have any number of children. Binary Trees and Binary Search Trees (BSTs) are specialized tree structures with additional constraints and will be implemented separately.