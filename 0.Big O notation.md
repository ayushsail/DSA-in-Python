# Big O Notation

## What is Big O Notation?

Big O Notation is a mathematical way to describe the **efficiency of an algorithm** — specifically how its runtime or memory usage grows as the input size (`n`) increases.

It answers the question: *"How does my algorithm scale?"*

Big O focuses on the **worst-case scenario** and drops constants and lower-order terms to capture the dominant growth trend.

```python
# Example: Linear Search
def linear_search(arr, target):
    for item in arr:        # loops n times → O(n)
        if item == target:
            return True
    return False
```

---

## Why Does It Matter?

| Input Size (n) | O(1)  | O(log n) | O(n)       | O(n log n)   | O(n²)          | O(2ⁿ)                  |
|----------------|-------|----------|------------|--------------|----------------|------------------------|
| 10             | 1     | 3        | 10         | 33           | 100            | 1,024                  |
| 100            | 1     | 7        | 100        | 664          | 10,000         | 1.27 × 10³⁰            |
| 1,000          | 1     | 10       | 1,000      | 9,966        | 1,000,000      | 10³⁰¹                  |
| 1,000,000      | 1     | 20       | 1,000,000  | 19,931,568   | 10¹²           | Practically ∞          |

> Even small differences in Big O class lead to **massive** real-world performance gaps.

---

## Rules for Calculating Big O
1. **Keep only fastest growing element**
1. **Drop constants** — `O(2n)` → `O(n)`
2. **Drop lower-order terms** — `O(n² + n)` → `O(n²)`
3. **Different inputs, different variables** — two separate loops over different arrays = `O(a + b)`, not `O(n)`
4. **Nested loops multiply** — a loop inside a loop = `O(n × m)` or `O(n²)`

---

## Time Complexity — All Main Types

Time complexity measures **how the number of operations grows** with input size `n`.

| Complexity    | Name             | Description                                                          | Python Example                            |
|---------------|------------------|----------------------------------------------------------------------|-------------------------------------------|
| **O(1)**      | Constant         | Always takes the same time, regardless of input size                 | `arr[0]`, `dict[key]`, `stack.append(x)` |
| **O(log n)**  | Logarithmic      | Halves the problem each step; very efficient                         | Binary search, balanced BST lookup        |
| **O(n)**      | Linear           | Visits every element once                                            | Linear search, single `for` loop          |
| **O(n log n)**| Linearithmic     | Efficient sorting; divide-and-conquer with a linear merge            | Merge sort, Timsort (`list.sort()`)       |
| **O(n²)**     | Quadratic        | Nested loops; slows drastically for large inputs                     | Bubble sort, insertion sort               |
| **O(n³)**     | Cubic            | Triple nested loops; only feasible for small inputs                  | Naive matrix multiplication               |
| **O(2ⁿ)**     | Exponential      | Doubles with each added element; impractical beyond ~30 elements     | Recursive Fibonacci, subset enumeration   |
| **O(n!)**     | Factorial        | Explores every permutation; only feasible for very small inputs      | Brute-force TSP, permutation generation   |

### Time Complexity — Efficiency Scale

```
Fastest ──────────────────────────────────────────────────► Slowest

O(1)  →  O(log n)  →  O(n)  →  O(n log n)  →  O(n²)  →  O(2ⁿ)  →  O(n!)
```

### Python Code Examples by Complexity

```python
# O(1) — Constant
def get_first(arr):
    return arr[0]

# O(log n) — Logarithmic
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) — Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:      # n iterations
        if num > max_val:
            max_val = num
    return max_val

# O(n log n) — Linearithmic
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)   # merge is O(n); called O(log n) times

# O(n²) — Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # outer loop: n
        for j in range(n - i - 1):  # inner loop: n
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(2ⁿ) — Exponential
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # 2 calls per level → 2ⁿ
```

---

## Common Data Structure Operations — Time Complexity

| Data Structure   | Access   | Search   | Insertion | Deletion | Notes                                   |
|------------------|----------|----------|-----------|----------|-----------------------------------------|
| **Array / List** | O(1)     | O(n)     | O(n)      | O(n)     | Insert/delete at end: O(1) amortized    |
| **Stack**        | O(n)     | O(n)     | O(1)      | O(1)     | Push/pop at top only                    |
| **Queue**        | O(n)     | O(n)     | O(1)      | O(1)     | Enqueue/dequeue at ends                 |
| **Linked List**  | O(n)     | O(n)     | O(1)*     | O(1)*    | *O(1) only with direct node reference   |
| **Hash Table**   | —        | O(1) avg | O(1) avg  | O(1) avg | O(n) worst case due to collisions       |
| **Binary Tree**  | O(n)     | O(n)     | O(n)      | O(n)     | Unbalanced worst case                   |
| **BST (balanced)**| O(log n) | O(log n) | O(log n)  | O(log n) | e.g., AVL tree, Red-Black tree          |
| **Heap**         | O(1)*    | O(n)     | O(log n)  | O(log n) | *O(1) only for min/max element          |

---

## Common Sorting Algorithms — Time Complexity

| Algorithm      | Best Case    | Average Case  | Worst Case   | Stable? | Notes                              |
|----------------|--------------|---------------|--------------|---------|------------------------------------|
| **Bubble Sort**    | O(n)         | O(n²)         | O(n²)        | ✅      | Simple but slow                    |
| **Selection Sort** | O(n²)        | O(n²)         | O(n²)        | ❌      | Always n² regardless               |
| **Insertion Sort** | O(n)         | O(n²)         | O(n²)        | ✅      | Great for nearly-sorted data       |
| **Merge Sort**     | O(n log n)   | O(n log n)    | O(n log n)   | ✅      | Consistent; uses extra space       |
| **Quick Sort**     | O(n log n)   | O(n log n)    | O(n²)        | ❌      | Fast in practice; pivot matters    |
| **Heap Sort**      | O(n log n)   | O(n log n)    | O(n log n)   | ❌      | In-place; consistent speed         |
| **Timsort**        | O(n)         | O(n log n)    | O(n log n)   | ✅      | Python's built-in (`list.sort()`)  |
| **Counting Sort**  | O(n + k)     | O(n + k)      | O(n + k)     | ✅      | Only for integers in range k       |

---

## Space Complexity — All Main Types

Space complexity measures **how much extra memory** an algorithm uses relative to input size `n`.  
It counts **auxiliary space** (extra space you allocate), not the input itself (unless specified).

| Complexity    | Name          | Description                                                      | Python Example                                     |
|---------------|---------------|------------------------------------------------------------------|----------------------------------------------------|
| **O(1)**      | Constant      | Uses a fixed amount of extra memory regardless of input size     | Swapping two variables, in-place sort              |
| **O(log n)**  | Logarithmic   | Memory grows logarithmically; common in recursive divide-conquer | Binary search call stack, balanced BST recursion   |
| **O(n)**      | Linear        | Extra memory scales linearly with input                          | Storing a copy of an array, hash map of n items    |
| **O(n log n)**| Linearithmic  | Slightly more than linear; rare but appears in some algorithms   | Some parallel sorting algorithms                   |
| **O(n²)**     | Quadratic     | Stores a 2D matrix or all pairs                                  | Adjacency matrix for a graph, DP 2D table          |
| **O(2ⁿ)**     | Exponential   | Storing all subsets or recursive states without memoization      | Power set generation                               |

### Common Sorting Algorithms — Space Complexity

| Algorithm       | Space Complexity | Notes                                             |
|-----------------|------------------|---------------------------------------------------|
| **Bubble Sort** | O(1)             | In-place                                          |
| **Insertion Sort** | O(1)          | In-place                                          |
| **Selection Sort** | O(1)          | In-place                                          |
| **Merge Sort**  | O(n)             | Needs auxiliary array for merging                 |
| **Quick Sort**  | O(log n)         | Call stack depth (average); O(n) worst case       |
| **Heap Sort**   | O(1)             | In-place                                          |
| **Timsort**     | O(n)             | Python's built-in; needs temp storage             |

### Python Space Complexity Examples

```python
# O(1) Space — only uses a counter variable
def sum_array(arr):
    total = 0          # one variable regardless of arr size
    for num in arr:
        total += num
    return total

# O(n) Space — creates a new list proportional to input
def double_values(arr):
    result = []        # grows with n
    for num in arr:
        result.append(num * 2)
    return result

# O(n) Space — recursive call stack depth = n
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # n frames on call stack

# O(log n) Space — call stack depth = log n
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# O(n²) Space — 2D matrix
def create_matrix(n):
    return [[0] * n for _ in range(n)]   # n × n = n² cells
```

---

## Quick Reference Summary

| Notation      | Name          | Time Example              | Space Example                  | Verdict         |
|---------------|---------------|---------------------------|--------------------------------|-----------------|
| O(1)          | Constant      | Dictionary lookup         | In-place swap                  | 🟢 Excellent     |
| O(log n)      | Logarithmic   | Binary search             | Recursive binary search stack  | 🟢 Excellent     |
| O(n)          | Linear        | Linear search             | Copying an array               | 🟡 Good          |
| O(n log n)    | Linearithmic  | Merge sort, Timsort       | Merge sort buffer              | 🟡 Good          |
| O(n²)         | Quadratic     | Bubble sort               | 2D DP table                    | 🔴 Avoid if possible |
| O(n³)         | Cubic         | Naive matrix multiply     | 3D DP table                    | 🔴 Poor          |
| O(2ⁿ)         | Exponential   | Naive Fibonacci           | All subsets                    | ⛔ Impractical   |
| O(n!)         | Factorial     | Brute-force permutations  | All permutations stored        | ⛔ Impractical   |

---

## Tips for Python Specifically

| Operation                     | Time Complexity | Notes                                     |
|-------------------------------|-----------------|-------------------------------------------|
| `list[i]`                     | O(1)            | Index access                              |
| `list.append(x)`              | O(1) amortized  | Occasional resize is O(n) but rare        |
| `list.insert(0, x)`           | O(n)            | Shifts all elements                       |
| `x in list`                   | O(n)            | Linear scan                               |
| `x in set` / `x in dict`      | O(1) avg        | Hash-based lookup                         |
| `dict[key]`                   | O(1) avg        | Hash-based access                         |
| `sorted(list)` / `list.sort()`| O(n log n)      | Python uses Timsort                       |
| `len(list)` / `len(dict)`     | O(1)            | Stored as metadata                        |
| `list + list`                 | O(n)            | Creates a new list                        |
| `list[a:b]`                   | O(b - a)        | Slice creates a copy                      |

---