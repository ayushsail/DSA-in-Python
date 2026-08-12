# Trie (Prefix Tree)

## 1. What is a Trie?

A **Trie**, also called a **Prefix Tree**, is a tree-based data structure used to store and retrieve strings efficiently.

Unlike a Binary Search Tree or Heap, a Trie stores data **character by character**.

For example, if we insert:

```text
apple
app
apply
```

the common prefix `app` is stored only once.

```text
root
└── a
    └── p
        └── p *
            ├── l
            │   ├── e *
            │   └── y *
```

`*` indicates that the node represents the **end of a complete word**.

### Main characteristics

* Stores strings character by character.
* Common prefixes are shared.
* Searching depends mainly on the length of the word, not the number of stored words.
* Particularly useful for prefix-based operations.
* Each node can have multiple children.
* A node needs an `EndOfWord` marker to distinguish complete words from prefixes.

---

# 2. Why is it called a Prefix Tree?

A **prefix** is the beginning portion of a string.

For example, prefixes of:

```text
computer
```

are:

```text
c
co
com
comp
compu
comput
compute
computer
```

A Trie stores these prefixes along paths from the root.

For:

```text
car
cat
can
```

the Trie becomes:

```text
root
└── c
    └── a
        ├── r *
        ├── t *
        └── n *
```

The prefix `ca` is stored only once.

---

# 3. Basic Structure of a Trie

A Trie consists of:

1. **Root node**
2. **Child nodes**
3. **End-of-word marker**

A node generally contains:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False
```

### `children`

The `children` dictionary stores:

```text
character → TrieNode
```

For example:

```python
{
    'a': TrieNode,
    'b': TrieNode
}
```

This means the current node has two possible next characters: `a` and `b`.

### `EndOfWord`

`EndOfWord` tells us whether the current node represents the end of a complete word.

Consider:

```text
app
apple
```

The node representing the second `p` must have:

```python
EndOfWord = True
```

because `app` itself is a valid word.

But it also has a child:

```text
p
└── l
```

Therefore, `EndOfWord` is necessary.

---

# 4. Trie Example

Suppose we insert:

```text
apple
app
ape
bat
```

The Trie looks approximately like:

```text
root
├── a
│   └── p
│       ├── p *
│       │   └── l
│       │       └── e *
│       └── e *
│
└── b
    └── a
        └── t *
```

The `*` represents:

```text
EndOfWord = True
```

---

# 5. TrieNode Implementation

Our implementation uses a Python dictionary as the children data structure.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False
```

### Why use a dictionary?

A dictionary provides efficient average-case lookup:

```python
if c in current.children:
```

and:

```python
current.children[c]
```

The dictionary stores only the characters that actually exist.

This is more memory-efficient than creating a fixed array of 26 positions for every node.

---

# 6. Trie Class

The Trie itself contains a root node.

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```

The root does not represent a character.

It is simply the starting point of every word.

---

# 7. Insert Operation

## Purpose

Insert a word into the Trie.

Example:

```text
insert("apple")
```

### Algorithm

```text
1. Check whether the word is empty.
2. Start at root.
3. For every character in the word:
   a. Check whether the character exists in children.
   b. If it doesn't exist, create a new TrieNode.
   c. Move to the child node.
4. Mark the final node as EndOfWord.
5. Return the inserted word.
```

### Implementation

```python
def insert(self, word: str) -> str:
    if not word:
        raise ValueError("Word cannot be empty!")

    current = self.root

    for c in word:
        if c not in current.children:
            current.children[c] = TrieNode()

        current = current.children[c]

    current.EndOfWord = True

    return word
```

### Example

Insert:

```text
cat
```

Step by step:

```text
root
 ↓
 c
 ↓
 a
 ↓
 t *
```

---

# 8. Search Operation

## Purpose

Check whether a **complete word** exists.

### Important distinction

Searching for:

```text
app
```

must return `False` if only:

```text
apple
```

exists.

The path exists, but `app` is not marked as an end of a word.

### Algorithm

```text
1. Validate the word.
2. Start at root.
3. Traverse one character at a time.
4. If a character doesn't exist:
      return False
5. After traversal:
      return EndOfWord
```

### Implementation

```python
def search(self, word: str) -> bool:
    if not word:
        raise ValueError("Word cannot be empty!")

    current = self.root

    for c in word:
        if c not in current.children:
            return False

        current = current.children[c]

    return current.EndOfWord
```

### Complexity

```text
Time:  O(L)
Space: O(1) auxiliary
```

where `L` is the length of the word.

---

# 9. Starts With

## Purpose

Check whether any word in the Trie starts with a given prefix.

For example:

```text
apple
application
banana
```

Then:

```text
starts_with("app") → True
starts_with("apl") → False
```

Notice that the prefix itself does not have to be a complete word.

### Algorithm

```text
1. Validate prefix.
2. Start at root.
3. Traverse every character.
4. If any character is missing:
      return False
5. If the entire prefix was traversed:
      return True
```

### Implementation

```python
def starts_with(self, prefix: str) -> bool:
    if not prefix:
        raise ValueError("Prefix cannot be empty!")

    current = self.root

    for c in prefix:
        if c not in current.children:
            return False

        current = current.children[c]

    return True
```

---

# 10. Find Node

`_find_node()` is a helper method.

Instead of returning only `True` or `False`, it returns the **last TrieNode corresponding to the given text**.

### Example

For:

```text
apple
```

```python
_find_node("app")
```

returns the node representing:

```text
app
```

If the path doesn't exist:

```python
None
```

is returned.

### Algorithm

```text
1. Validate text.
2. Start at root.
3. Traverse each character.
4. If character doesn't exist:
      return None
5. Return the final node.
```

### Implementation

```python
def _find_node(self, text) -> TrieNode | None:
    if not text:
        raise ValueError("Word cannot be empty!")

    current = self.root

    for c in text:
        if c not in current.children:
            return None

        current = current.children[c]

    return current
```

---

# 11. DFS Traversal

DFS stands for:

**Depth First Search**

It explores one branch completely before moving to another branch.

For a Trie, DFS is useful for:

* Getting all words
* Autocomplete
* Prefix counting
* Displaying the Trie
* Other traversal-based operations

### Example

```text
root
└── a
    └── p
        ├── p *
        └── e *
```

DFS explores one branch deeply before returning.

### Implementation

```python
def _dfs(self, current, current_word, wordlist) -> None:
    if current.EndOfWord:
        wordlist.append(current_word)

    for c, child in current.children.items():
        self._dfs(child, current_word + c, wordlist)
```

---

# 12. Get All Words

This method uses DFS to collect every complete word.

### Algorithm

```text
1. Create an empty word list.
2. Start DFS from root.
3. DFS adds a word whenever EndOfWord is True.
4. Return the word list.
```

### Implementation

```python
def get_word_list(self) -> list:
    wordlist = []

    self._dfs(self.root, "", wordlist)

    return wordlist
```

---

# 13. Is Empty

A Trie is empty when the root has no children.

### Logic

```text
root.children == {}
```

### Implementation

```python
def isEmpty(self) -> bool:
    return not self.root.children
```

### Complexity

```text
Time: O(1)
```

---

# 14. Display

The `display()` method displays:

1. All stored words
2. Trie tree structure

### Implementation

```python
def display(self) -> None:
    if self.isEmpty():
        raise ValueError("Trie is Empty!")

    print("\nTrie Words :")

    for word in self.get_word_list():
        print("-", word)

    print("\nTrie Tree :\n")
    print("root")

    self._display_tree(self.root)

    print()
```

---

# 15. Display Tree

The `_display_tree()` method recursively displays the Trie in a tree-like format.

### Example

For:

```text
abcd
ablg
efgh
```

Output:

```text
root
├── a
│   └── b
│       ├── c
│       │   └── d *
│       └── l
│           └── g *
└── e
    └── f
        └── g
            └── h *
```

### Implementation

```python
def _display_tree(self, current, prefix=""):
    children = list(current.children.items())

    for i, (c, child) in enumerate(children):
        child_is_last = i == len(children) - 1

        branch = "└── " if child_is_last else "├── "
        marker = " *" if child.EndOfWord else ""

        print(prefix + branch + c + marker)

        new_prefix = prefix + ("    " if child_is_last else "│   ")

        self._display_tree(child, new_prefix)
```

---

# 16. Word Count

`word_count()` returns the number of complete words stored in the Trie.

### Algorithm

```text
1. Get all words using DFS.
2. Return the length of the list.
```

### Implementation

```python
def word_count(self) -> int:
    return len(self.get_word_list())
```

### Important

Duplicate insertion does not create duplicate words.

```python
insert("apple")
insert("apple")
insert("apple")
```

Still results in:

```text
word_count = 1
```

because `EndOfWord` is simply set to `True`.

---

# 17. Prefix Count

`prefix_count()` returns the number of complete words that start with a particular prefix.

For:

```text
abcd
ablg
abxy
apple
```

we have:

```text
prefix_count("ab") → 3
```

### Algorithm

```text
1. Validate prefix.
2. Find the node corresponding to prefix.
3. If node doesn't exist:
      return 0
4. Run DFS from that node.
5. Count the resulting words.
6. Return count.
```

### Implementation

```python
def prefix_count(self, prefix) -> int:
    if not prefix:
        raise ValueError("Prefix cannot be empty!")

    node = self._find_node(prefix)

    if not node:
        return 0

    wordlist = []

    self._dfs(node, "", wordlist)

    return len(wordlist)
```

---

# 18. Autocomplete

Autocomplete returns all complete words that begin with a given prefix.

For:

```text
apple
application
apply
banana
```

then:

```python
auto_complete("app")
```

returns:

```text
[
    "apple",
    "application",
    "apply"
]
```

### Algorithm

```text
1. Validate prefix.
2. Find the node corresponding to prefix.
3. If it doesn't exist:
      return []
4. Start DFS from that node.
5. Start current_word with the prefix.
6. Return all discovered words.
```

### Implementation

```python
def auto_complete(self, prefix) -> list:
    if not prefix:
        raise ValueError("Prefix cannot be empty!")

    node = self._find_node(prefix)

    if not node:
        return []

    wordlist = []

    self._dfs(node, prefix, wordlist)

    return wordlist
```

### Difference from Prefix Count

```text
prefix_count()
        ↓
DFS
        ↓
number of words
```

Whereas:

```text
auto_complete()
        ↓
DFS
        ↓
actual words
```

---

# 19. Longest Common Prefix

The **Longest Common Prefix (LCP)** is the longest prefix shared by all words in the Trie.

Example:

```text
flower
flow
flight
```

Longest common prefix:

```text
fl
```

Another example:

```text
abcd
ablg
abxy
```

Result:

```text
ab
```

### Important Trie observation

The common prefix continues while:

```text
current node has exactly one child
```

and:

```text
current node is not EndOfWord
```

If there are multiple children, the words branch.

Therefore, the common prefix stops.

### Algorithm

```text
1. If Trie is empty:
      raise exception
2. Start from root.
3. Set prefix = ""
4. While:
      current has exactly one child
      AND current is not EndOfWord
5. Get the only child.
6. Add its character to prefix.
7. Move to the child.
8. Return prefix.
```

### Implementation

```python
def longest_common_prefix(self) -> str:
    if self.isEmpty():
        raise ValueError("Trie is Empty!")

    current = self.root
    prefix = ""

    while len(current.children) == 1 and not current.EndOfWord:
        for c, child in current.children.items():
            prefix += c
            current = child

    return prefix
```

### Example

```text
abcd
ablg
abxy
```

Trie:

```text
root
└── a
    └── b
        ├── c
        ├── l
        └── x
```

At `b`, there are three children.

Therefore:

```text
Longest Common Prefix = "ab"
```

---

# 20. Delete Operation

Deletion is the most complicated basic Trie operation.

The challenge is that deleting a word may require deleting unnecessary nodes, but we must not delete nodes that belong to another word.

Consider:

```text
app
apple
```

If we delete:

```text
apple
```

we must keep:

```text
app
```

Therefore, nodes are deleted only when they are no longer needed.

---

# 21. Delete Algorithm

### Step 1 — Validate the word

Traverse the Trie and make sure the word exists.

```text
If any character doesn't exist:
    word doesn't exist

If final node is not EndOfWord:
    word doesn't exist
```

### Step 2 — Recursive deletion

Start from:

```text
root
```

and recursively move toward the last character.

The `depth` parameter tells us which character we're currently processing.

```text
word = "apple"

depth = 0 → a
depth = 1 → p
depth = 2 → p
depth = 3 → l
depth = 4 → e
depth = 5 → end
```

### Step 3 — Reach the end

At:

```python
depth == len(word)
```

we have reached the final node.

Set:

```python
current.EndOfWord = False
```

Now determine whether the node should be deleted.

### Node can be deleted when:

```text
1. It has no children.
2. It is not the end of another word.
```

### Implementation

```python
def delete(self, word: str) -> str:
    if not word:
        raise ValueError("Word cannot be empty!")

    current = self.root

    for c in word:
        if c not in current.children:
            raise ValueError("The word doesn't exist in Trie!")

        current = current.children[c]

    if current.EndOfWord is False:
        raise ValueError("The word doesn't exist in Trie!")

    self._delete_helper(self.root, word, 0)

    return word
```

### Delete Helper

```python
def _delete_helper(self, current, word: str, depth: int) -> bool:
    if depth == len(word):
        current.EndOfWord = False

        if current.children:
            return False

        else:
            return True

    c = word[depth]
    child = current.children[c]

    should_delete = self._delete_helper(
        child,
        word,
        depth + 1
    )

    if should_delete:
        del current.children[c]

    if not current.children and not current.EndOfWord:
        return True

    return False
```

---

# 22. Understanding Recursive Delete

Suppose:

```text
abcd
ablg
```

Delete:

```text
abcd
```

The recursion travels:

```text
root
 ↓
 a
 ↓
 b
 ↓
 c
 ↓
 d
```

At `d`:

```text
EndOfWord = False
children = {}
```

Therefore `d` can be deleted.

Return to `c`.

If `c` has no children and is not another word:

```text
delete c
```

Continue upward.

Eventually:

```text
root
└── a
    └── b
        └── l
            └── g *
```

The shared nodes `a` and `b` remain because `ablg` still needs them.

---

# 23. Clear

`clear()` removes the entire Trie.

Instead of manually deleting every node, simply create a new root.

### Implementation

```python
def clear(self) -> None:
    self.root = TrieNode()
```

All old nodes become unreachable from the Trie.

---

# 24. Complexity

Let:

```text
L = length of the word/prefix
N = total number of nodes
W = number of stored words
K = number of words matching a prefix
```

| Operation                 | Time Complexity | Explanation                             |
| ------------------------- | --------------: | --------------------------------------- |
| `insert()`                |            O(L) | Traverse/create L nodes                 |
| `search()`                |            O(L) | Traverse L characters                   |
| `starts_with()`           |            O(L) | Traverse prefix                         |
| `_find_node()`            |            O(L) | Traverse text                           |
| `delete()`                |            O(L) | Traverse word and recursively backtrack |
| `peek/find node`          |            O(L) | Character-by-character traversal        |
| `get_word_list()`         |            O(N) | DFS over Trie                           |
| `_dfs()`                  |            O(N) | Visits Trie nodes                       |
| `word_count()`            |            O(N) | Builds complete word list               |
| `prefix_count()`          |       O(L + Nₚ) | Traverse prefix + DFS subtree           |
| `auto_complete()`         |       O(L + Nₚ) | Traverse prefix + DFS subtree           |
| `longest_common_prefix()` |            O(L) | Traverses common path                   |
| `isEmpty()`               |            O(1) | Checks root                             |
| `clear()`                 |           O(1)* | Resets root reference                   |
| `display()`               |            O(N) | Prints all nodes/words                  |

Where `Nₚ` is the number of nodes below the requested prefix.

`clear()` is considered O(1) for the operation itself; Python's garbage collector may later reclaim the detached nodes.

---

# 25. Trie vs Hash Table

| Feature           | Trie        | Hash Table                    |
| ----------------- | ----------- | ----------------------------- |
| Exact search      | O(L)        | O(1) average                  |
| Prefix search     | Excellent   | Poor                          |
| Autocomplete      | Excellent   | Requires extra processing     |
| Ordered traversal | Possible    | Not naturally ordered         |
| Memory            | Can be high | Usually lower                 |
| String processing | Excellent   | Good                          |
| Prefix counting   | Excellent   | Poor without extra structures |

A Trie is particularly useful when **prefix operations** are important.

---

# 26. Trie vs Binary Search Tree

| Feature       | Trie                   | BST                            |
| ------------- | ---------------------- | ------------------------------ |
| Search string | O(L)                   | O(L log N) average             |
| Prefix search | Excellent              | More complicated               |
| Autocomplete  | Natural                | Requires traversal/range logic |
| Ordering      | Character-based        | Key-based                      |
| Height        | Depends on word length | Depends on tree balance        |
| Memory        | Potentially high       | Generally lower                |

---

# 28. Trie Advantages

### 1. Fast string searching

Search depends mainly on word length.

```text
O(L)
```

### 2. Excellent prefix operations

Operations such as:

```text
starts_with()
prefix_count()
auto_complete()
```

are natural Trie operations.

### 3. Shared prefixes

Common prefixes are stored only once.

For:

```text
car
cat
can
```

the path:

```text
c → a
```

is shared.

### 4. Predictable search complexity

Unlike a hash table's average-case O(1), Trie operations are based on string length.

---

# 29. Trie Disadvantages

### 1. Memory usage

Each character can require a separate node.

A Trie containing many unrelated words can consume significant memory.

### 2. Implementation complexity

Compared with a hash table, operations such as deletion require more logic.

### 3. Character-set dependency

The implementation must decide how characters are represented.

For example:

```text
lowercase English letters
uppercase + lowercase
digits
Unicode
```

---

# 30. Children Data Structure Choices

There are several ways to store children.

## Dictionary / Hash Map

Our implementation:

```python
self.children = {}
```

Advantages:

* Flexible
* Stores only existing characters
* Good memory usage for sparse nodes
* Supports arbitrary characters
* Simple Python implementation

Average lookup:

```text
O(1)
```

---

## Fixed Array

For lowercase English letters:

```python
self.children = [None] * 26
```

Mapping:

```text
a → 0
b → 1
c → 2
...
z → 25
```

Advantages:

* Direct indexing
* Predictable access
* Can be faster in some implementations

Disadvantages:

* More memory usage
* Limited character set
* More complicated implementation

---

# 31. Which Child Structure Should We Use?

For our Python implementation:

```python
self.children = {}
```

is a very good choice.

For large-scale systems, the choice depends on:

```text
Character set
Memory constraints
Number of words
Number of operations
Performance requirements
```

A dictionary/hash-map based Trie is generally a practical implementation.

---

# 32. Important Trie Concepts

### Root

The starting node.

```text
root
```

does not represent a character.

### Child

A node representing the next character.

### EndOfWord

Indicates that the path from root to the current node forms a complete word.

### Prefix

Beginning portion of a word.

### Path

Sequence of characters from root to a node.

### Branch

A point where a node has multiple children.

### Leaf

A node with no children.

---

# 33. Common Trie Mistakes

### Mistake 1 — Forgetting EndOfWord

Without `EndOfWord`, we cannot distinguish:

```text
app
```

from:

```text
apple
```

### Mistake 2 — Deleting shared nodes

Never delete a node if another word still depends on it.

### Mistake 3 — Confusing prefix with complete word

```text
starts_with("app")
```

can be `True` even when:

```text
search("app")
```

is `False`.

### Mistake 4 — Losing the prefix during autocomplete

DFS should start with:

```python
self._dfs(node, prefix, wordlist)
```

rather than:

```python
self._dfs(node, "", wordlist)
```

when the goal is to return complete words.

### Mistake 5 — Treating every leaf as a word

A complete word can end at a node that has children.

Example:

```text
app *
└── l
    └── e *
```

`app` is a complete word even though its node isn't a leaf.

---

# 34. Trie Applications

Tries are widely used for:

### Autocomplete

Search bars and text editors.

```text
User enters: "app"

Suggestions:
apple
application
apply
appstore
```

### Spell Checking

Check whether a word exists in a dictionary.

### Search Engines

Prefix-based query suggestions.

### Contact Search

Searching contacts by name prefix.

### IP Routing

Specialized Trie structures such as Patricia Tries are used for routing.

### Dictionary Applications

Fast word lookup and prefix searching.

### Word Games

Games such as:

```text
Word Search
Boggle
Scrabble
```

can use Tries to efficiently find valid words.

---

# 35. Trie Variations

## Standard Trie

The implementation used here.

Each edge generally represents one character.

---

## Compressed Trie

Also called a:

```text
Radix Tree
Patricia Trie
```

Chains of single-child nodes can be compressed.

Instead of:

```text
c → o → m → p → u → t → e → r
```

a compressed Trie can store:

```text
computer
```

as one edge.

This saves memory.

---

## Ternary Search Trie

Uses three pointers:

```text
left
middle
right
```

It combines ideas from BSTs and Tries.

---

# 36. Trie Memory Model

For a word:

```text
hello
```

the basic Trie creates:

```text
root
 ↓
h
 ↓
e
 ↓
l
 ↓
l
 ↓
o *
```

Five character nodes are required.

If another word is:

```text
help
```

the first three/four characters can be shared:

```text
root
└── h
    └── e
        └── l
            ├── l
            │   └── o *
            └── p *
```

This is the main memory-sharing advantage of a Trie.

---


# 38. Summary

A **Trie** is a tree-based data structure designed primarily for strings.

The key idea is:

```text
One character = One step in the Trie
```

The most important concepts are:

```text
Trie
├── Root
├── Children
├── EndOfWord
├── Prefix
├── DFS
└── Shared paths
```

The most important operations are:

```text
insert()          → Add word
search()          → Find complete word
starts_with()     → Find prefix
delete()          → Remove word
auto_complete()   → Find words by prefix
prefix_count()    → Count words by prefix
word_count()      → Count all words
longest_common_prefix()
                  → Find shared prefix
```

### Key complexity

For a word of length `L`:

```text
Insert       → O(L)
Search       → O(L)
Starts With  → O(L)
Delete       → O(L)
```

This makes Tries particularly powerful for **prefix-based string operations**.

> **Core idea to remember:**
> A Trie trades additional memory for extremely efficient string and prefix operations.
h