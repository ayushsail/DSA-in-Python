# AVL Tree (Adelson-Velsky and Landis Tree)

## Introduction

An **AVL Tree** is a **self-balancing Binary Search Tree (BST)** in which the difference between the heights of the left and right subtrees of every node is at most **1**.

It was introduced by **Georgy Adelson-Velsky** and **Evgenii Landis** in 1962, making it the first self-balancing Binary Search Tree.

Unlike a normal BST, an AVL Tree automatically performs **rotations** after insertion and deletion whenever the tree becomes unbalanced. This guarantees that the height of the tree remains **O(log n)**, resulting in efficient searching, insertion, and deletion.

---

# Properties

* Self-balancing Binary Search Tree.
* Left subtree contains smaller values.
* Right subtree contains larger values.
* Duplicate values are not allowed.
* Balance Factor of every node must be:

  * -1
  * 0
  * +1
* Performs rotations whenever the balance factor becomes:

  * +2
  * -2

---

# Balance Factor

The balance factor of a node is

```text
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
```

Possible values:

| Balance Factor | Meaning                      |
| --- | ---------------------------- |
|  +2 | Left Heavy (Needs Rotation)  |
|  +1 | Left subtree is taller by 1  |
|   0 | Perfectly balanced           |
|  -1 | Right subtree is taller by 1 |
|  -2 | Right Heavy (Needs Rotation) |

---

# AVL Rotations

AVL Tree uses four types of rotations.

## 1. LL Rotation (Right Rotation)

Occurs when a node becomes left-heavy because of insertion/deletion in the left subtree of its left child.

```
        A
       /
      B
     /
    C

↓

        B
       / \
      C   A
```

---

## 2. RR Rotation (Left Rotation)

Occurs when a node becomes right-heavy because of insertion/deletion in the right subtree of its right child.

```
    A
     \
      B
       \
        C

↓

      B
     / \
    A   C
```

---

## 3. LR Rotation

Occurs when the imbalance is Left-Right.

Steps

1. Left Rotate Left Child
2. Right Rotate Root

---

## 4. RL Rotation

Occurs when the imbalance is Right-Left.

Steps

1. Right Rotate Right Child
2. Left Rotate Root

---

# Node Structure

Each node stores

* Data
* Left Child
* Right Child
* Parent
* Height

```
Node
│
├── data
├── left
├── right
├── parent
└── height
```

---

# Implementation

## Constructor

### `__init__(data)`

Initializes an AVL node.

### Algorithm

1. Store data.
2. Initialize left child as None.
3. Initialize right child as None.
4. Initialize parent as None.
5. Initialize height as 0.

---

## display()

Displays the tree sideways.

### Algorithm

1. Display right subtree.
2. Print current node.
3. Display left subtree.

---

## update_height()

Updates the height of the current node.

### Algorithm

1. Calculate left subtree height.
2. Calculate right subtree height.
3. Store

```
height = 1 + max(left_height, right_height)
```

---

## get_balance()

Returns balance factor.

### Algorithm

1. Calculate left subtree height.
2. Calculate right subtree height.
3. Return

```
left_height - right_height
```

---

## right_rotate()

Performs Right Rotation.

### Algorithm

1. Store old root.
2. Store new root.
3. Store transferred subtree.
4. Rotate nodes.
5. Update parent pointers.
6. Update heights.
7. Return new root.

---

## left_rotate()

Performs Left Rotation.

### Algorithm

1. Store old root.
2. Store new root.
3. Store transferred subtree.
4. Rotate nodes.
5. Update parent pointers.
6. Update heights.
7. Return new root.

---

## rebalance()

Balances the AVL Tree.

### Algorithm

1. Update current node height.
2. Compute balance factor.
3. If balance > 1

   * Perform LL or LR rotation.
4. If balance < -1

   * Perform RR or RL rotation.
5. Return balanced subtree.

---

## insert(data)

Inserts a new node.

### Algorithm

1. Compare data with current node.
2. Insert recursively in left subtree if smaller.
3. Insert recursively in right subtree if larger.
4. Ignore duplicate values.
5. Rebalance the tree.
6. Return new subtree root.

---

## delete(data)

Deletes a node.

### Algorithm

1. Search recursively.
2. If node has no children

   * Return None.
3. If node has one child

   * Return child.
4. If node has two children

   * Find inorder successor.
   * Replace current node.
   * Delete successor.
5. Rebalance the tree.
6. Return new subtree root.

---

## find_min()

Returns the minimum node.

### Algorithm

1. Move to left child repeatedly.
2. Return last node.

---

## find_max()

Returns the maximum node.

### Algorithm

1. Move to right child repeatedly.
2. Return last node.

---

## find(data)

Searches for a node.

### Algorithm

1. Compare data with current node.
2. If equal, return node.
3. If smaller, search left subtree.
4. If greater, search right subtree.
5. Return None if not found.

---

## contains(data)

Checks whether a value exists.

### Algorithm

1. Call find().
2. Return True if found.
3. Otherwise return False.

---

## is_root()

Checks whether the node is root.

### Algorithm

1. If parent is None

   * Return True.
2. Otherwise return False.

---

## is_leaf()

Checks whether the node is a leaf.

### Algorithm

1. If both children are None

   * Return True.
2. Otherwise return False.

---

## count_nodes()

Counts total nodes.

### Algorithm

1. Count current node.
2. Recursively count left subtree.
3. Recursively count right subtree.
4. Return total count.

---

## count_leaf_nodes()

Counts leaf nodes.

### Algorithm

1. If node is leaf

   * Return 1.
2. Count leaf nodes in left subtree.
3. Count leaf nodes in right subtree.
4. Return total count.

---

## count_internal_nodes()

Counts internal nodes.

### Algorithm

1. If node is leaf

   * Return 0.
2. Count current node.
3. Count internal nodes in left subtree.
4. Count internal nodes in right subtree.
5. Return total count.

---

## get_level()

Returns level of current node.

### Algorithm

1. Start from current node.
2. Move to parent repeatedly.
3. Count levels.
4. Return level.

---

## get_path()

Returns path from root to current node.

### Algorithm

1. Traverse parent pointers until root.
2. Store nodes.
3. Reverse the list.
4. Return path.

---

## inorder_traversal()

Traversal order

```
Left → Node → Right
```

### Algorithm

1. Traverse left subtree.
2. Visit node.
3. Traverse right subtree.

---

## preorder_traversal()

Traversal order

```
Node → Left → Right
```

### Algorithm

1. Visit node.
2. Traverse left subtree.
3. Traverse right subtree.

---

## postorder_traversal()

Traversal order

```
Left → Right → Node
```

### Algorithm

1. Traverse left subtree.
2. Traverse right subtree.
3. Visit node.

---

## bfs_levelorder()

Traverses tree level by level.

### Algorithm

1. Create queue.
2. Enqueue root.
3. While queue is not empty:

   * Dequeue node.
   * Visit node.
   * Enqueue left child.
   * Enqueue right child.

---

## clear_detach()

Detaches a subtree.

### Algorithm

1. Remove subtree from parent.
2. Set parent pointer to None.
3. Subtree remains in memory.

---

## clear_destroy()

Destroys a subtree.

### Algorithm

1. Recursively destroy left subtree.
2. Recursively destroy right subtree.
3. Detach current node.
4. Remove all references.

---

# Time Complexity

| Operation | Time Complexity |
| --------- | --------------: |
| Search    |        O(log n) |
| Insert    |        O(log n) |
| Delete    |        O(log n) |
| Find Min  |        O(log n) |
| Find Max  |        O(log n) |
| Rotation  |            O(1) |

---

# Space Complexity

| Operation            | Space Complexity |
| -------------------- | ---------------: |
| AVL Tree             |             O(n) |
| Recursive Operations |         O(log n) |

---

# Advantages

* Guaranteed O(log n) searching.
* Faster searching than ordinary BST.
* Automatically balanced.
* Efficient insertion and deletion.
* Suitable for frequently updated datasets.

---

# Disadvantages

* More complex implementation.
* Rotations increase insertion/deletion overhead.
* Extra memory required for height field.
* Slightly slower insertion/deletion than an unbalanced BST due to balancing operations.

---

# Applications

* Database indexing.
* File systems.
* Memory management.
* Dictionaries and symbol tables.
* Routing tables.
* In-memory searching.
* Ordered data storage.

---

# Summary

AVL Tree is a self-balancing Binary Search Tree that maintains a balance factor between -1 and +1 for every node. Whenever an insertion or deletion causes an imbalance, one of four rotations (LL, RR, LR, RL) is performed to restore balance. This guarantees **O(log n)** search, insertion, and deletion, making AVL Trees one of the most efficient balanced search tree data structures.
