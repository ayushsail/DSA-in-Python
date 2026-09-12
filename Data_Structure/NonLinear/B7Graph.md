# Graph — Data Structure Notes


## 1. Graph Introduction

### What is a Graph?

A **Graph** is a non-linear data structure used to represent relationships or connections between objects.

A graph consists of:

- **Vertex (V):** A node/object in the graph.
- **Edge (E):** A connection between two vertices.

A graph is commonly represented as:

```text
G = (V, E)
```

where:

- `V` = set of vertices
- `E` = set of edges

### Example

```text
A ---- B
|      |
|      |
C ---- D
```

Vertices:

```text
V = {A, B, C, D}
```

Edges:

```text
E = {(A,B), (A,C), (B,D), (C,D)}
```

---

## Types of Graphs

### 1. Undirected Graph

An edge has **no direction**.

```text
A ---- B
```

`A` is connected to `B`, and `B` is connected to `A`.

In the implementation, adding an undirected edge stores the connection in both adjacency lists. 

### 2. Directed Graph

An edge has a direction.

```text
A ----> B
```

`A → B` does not automatically mean `B → A`.

### 3. Unweighted Graph

Edges do not carry numerical weights.

```text
A ---- B
```

The implementation stores `None` for an unweighted edge.

### 4. Weighted Graph

Every edge stores a numerical weight/cost.

```text
A --10--> B
```

The implementation stores the weight as the adjacency value.

---
### Important Graph Terms

| Term | Meaning |
|---|---|
| Vertex | A node in the graph |
| Edge | Connection between two vertices |
| Neighbour | A vertex directly connected to another vertex |
| Degree | Number of edges incident on a vertex in an undirected graph |
| In-degree | Number of incoming edges in a directed graph |
| Out-degree | Number of outgoing edges in a directed graph |
| Path | Sequence of vertices connected by edges |
| Cycle | A path that returns to its starting vertex |
| Connected Component | A maximal group of mutually reachable vertices under the relevant connectivity definition |

---

# 2. Graph Representation and Implementation

## Adjacency List

The graph is stored using a dictionary:

```python
self.graph = {}
```

Each vertex maps to another dictionary containing its neighbours.

### Unweighted example

```text
A -> {B: None, C: None}
B -> {A: None}
C -> {A: None}
```

### Weighted example

```text
A -> {B: 10, C: 5}
B -> {A: 10}
C -> {A: 5}
```

For an undirected graph, both directions are stored internally. For a directed graph, only the specified direction is stored.

---

## Graph Constructor

```python
Graph(directed=False, weighted=False)
```

The constructor stores:

- `directed` → whether edges have direction
- `weighted` → whether edges have numerical weights
- `graph` → adjacency-list dictionary

---

## Graph Implementation — Method Algorithms

### 1. `add_vertex(vertex)`

**Purpose:** Add a new vertex to the graph.

**Algorithm:**

- Check whether the vertex already exists.
- If it exists, raise an error.
- Create an empty neighbour dictionary for the vertex.
- Return the vertex as a string.

---

### 2. `remove_vertex(vertex)`

**Purpose:** Remove a vertex and all edges connected to it.

**Algorithm:**

- Check whether the vertex exists.
- Delete the vertex from the main graph dictionary.
- Visit every other vertex.
- Remove the deleted vertex from every neighbour dictionary where it appears.
- Return the removed vertex.

---

### 3. `add_edge(source, destination, weight=0)`

**Purpose:** Add an edge between two existing vertices.

**Algorithm:**

- Validate that `source` exists.
- Validate that `destination` exists.
- Reject self-loops.
- If the graph is weighted, verify that the weight is numeric and is not a boolean.
- Check that the edge does not already exist.
- Store the edge and weight.
- For an undirected graph, store the reverse edge as well.
- Return a string describing the edge direction.

**Weight validation used:**

```python
if self.weighted and (not isinstance(weight, (int, float)) or isinstance(weight, bool)):
    raise ValueError("Weight must be a number !")
```

This permits positive, zero, and negative numeric weights.

---

### 4. `remove_edge(source, destination)`

**Purpose:** Remove an existing edge.

**Algorithm:**

- Validate both vertices.
- Check whether the edge exists.
- Delete the edge.
- If the graph is undirected, also delete the reverse edge.
- Return a description of the removed edge.

---

### 5. `has_vertex(vertex)`

**Purpose:** Check whether a vertex exists.

**Algorithm:**

- Search for the vertex in the graph dictionary.
- Return `True` if found, otherwise `False`.

---

### 6. `has_edge(source, destination)`

**Purpose:** Check whether an edge exists.

**Algorithm:**

- Validate that both vertices exist.
- Search for `destination` inside the source's neighbour dictionary.
- Return the result.

---

### 7. `get_neighbours(vertex)`

**Purpose:** Return all direct neighbours of a vertex.

**Algorithm:**

- Verify that the vertex exists.
- Return the keys of its adjacency dictionary as a list.

---

### 8. `degree(vertex)`

**Purpose:** Find the degree of a vertex in an undirected graph.

**Algorithm:**

- Validate the vertex.
- Reject the operation for directed graphs.
- Return the number of neighbours.

---

### 9. `inDegree(vertex)`

**Purpose:** Count incoming edges of a directed vertex.

**Algorithm:**

- Validate the vertex.
- Reject the operation for undirected graphs.
- Start a counter at `0`.
- Visit every vertex.
- Count how many adjacency dictionaries contain the target vertex.
- Return the count.

---

### 10. `outDegree(vertex)`

**Purpose:** Count outgoing edges of a directed vertex.

**Algorithm:**

- Validate the vertex.
- Reject the operation for undirected graphs.
- Return the number of neighbours of the vertex.

---

### 11. `isEmpty()`

**Purpose:** Check whether the graph contains no vertices.

**Algorithm:**

- Check whether the main graph dictionary is empty.
- Return the result.

---

### 12. `display()` — Adjacency List

**Purpose:** Display the graph in adjacency-list form.

**Algorithm:**

- Reject an empty graph.
- Visit every vertex.
- For an unweighted graph, display the neighbour list.
- For a weighted graph, display each neighbour together with its weight.

Example:

```text
A -> ['B(10)', 'C(5)']
B -> ['D(8)']
C -> []
D -> []
```

---

### 13. `display_graph()` — Graphical Display

**Purpose:** Visualize the graph using NetworkX and Matplotlib.

**Algorithm:**

- Reject an empty graph.
- Create `DiGraph` for directed graphs or `Graph` for undirected graphs.
- Copy all vertices and edges into NetworkX.
- Copy edge weights for weighted graphs.
- Calculate node positions using `spring_layout`.
- Draw nodes, edges, vertex labels, and weight labels.
- Display the final graph.

---

### 14. `vertex_count()`

**Purpose:** Count the number of vertices.

**Algorithm:**

- Return the size of the main graph dictionary.

---

### 15. `edge_count()`

**Purpose:** Count the number of edges.

**Algorithm:**

- Add the number of neighbours for every vertex.
- For a directed graph, return the total directly.
- For an undirected graph, divide the count by `2` because each edge is stored twice.

---

# 3. Important Graph Properties

## 1.Complete Graph

A graph is **complete** when every vertex is directly connected to every other vertex.

### Undirected Complete Graph

For `n` vertices:

```text
E = n(n - 1) / 2
```

### Directed Complete Graph

For a simple directed graph:

```text
E = n(n - 1)
```

### Implementation Algorithm

* Count total vertices `n`.
* Count total edges.
* For directed graph, compare with `n(n - 1)`.
* For undirected graph, compare with `n(n - 1) / 2`.
* If equal → **Complete Graph**.
* Otherwise → **Not Complete**.

### Example

```text
    A
   / \
  B---C
```

Every pair of vertices is connected, so the graph is complete.

---

## 2.Connected Graph

A graph is **connected** when all vertices belong to one connected component.

### Undirected Graph

If DFS/BFS starting from any vertex reaches all vertices, the graph is connected.

### Implementation Algorithm

* Choose any starting vertex.
* Perform DFS.
* Count the visited vertices.
* If visited vertices = total vertices → **Connected**.
* Otherwise → **Disconnected**.

### Directed Graph — Current Implementation

The implementation uses **strong connectivity** for `is_connected()`.

### Implementation Algorithm

* Choose one starting vertex.
* Perform DFS on the original graph.
* Reverse every edge.
* Perform DFS again from the same starting vertex.
* If both traversals reach every vertex → **Strongly Connected**.
* Otherwise → **Not Strongly Connected**.

### Strongly Connected

For every pair of vertices `u` and `v`, there is a directed path:

```text
u → v
v → u
```

---

## 3.Weakly Connected Graph

A directed graph is **weakly connected** when connectivity exists after ignoring edge direction.

Example:

```text
A → B → C
```

The current implementation checks this by considering both incoming and outgoing neighbours.

### Implementation Algorithm

* Select a vertex having at least one edge.
* Perform BFS.
* Consider both incoming and outgoing neighbours.
* Ignore edge direction.
* Count vertices that actually have edges.
* If all such vertices are reached → **Weakly Connected**.

---

## 4.Cyclic Graph

A graph is **cyclic** if it contains a **cycle** — a path that returns to the starting vertex without repeating intermediate vertices.

### Directed Graph

Uses:

* `visited` → vertices already explored.
* `current_path` → vertices currently in the DFS path.

### Implementation Algorithm

* Start DFS from an unvisited vertex.
* Mark the vertex as `visited` and add it to `current_path`.
* For each neighbour:

  * If neighbour is already in `current_path` → **Cycle Found**.
  * If neighbour is unvisited → continue DFS.
* Remove the vertex from `current_path` while backtracking.
* Repeat for every component.

### Undirected Graph

Uses DFS with a `parent` vertex.

### Implementation Algorithm

* Start DFS from an unvisited vertex.
* Mark it as visited.
* For each neighbour:

  * If unvisited → continue DFS.
  * If visited and neighbour is not the parent → **Cycle Found**.
* Repeat for every component.

---

## 5.Bipartite Graph

A graph is **bipartite** if its vertices can be divided into two groups such that no edge connects vertices in the same group.

Another way to say it:

> Every adjacent pair must receive different colours.

The implementation uses **BFS + 2-colouring**:

```text
Colour 0 → Group 1
Colour 1 → Group 2
```

### Implementation Algorithm

* Choose an uncoloured vertex.
* Assign colour `0`.
* Perform BFS.
* Give every uncoloured neighbour the opposite colour.
* If two adjacent vertices have the same colour → **Not Bipartite**.
* Repeat for every uncoloured vertex.

### Important Property

A graph containing an **odd-length cycle** is not bipartite.

---

# 6.Eulerian Graph

Eulerian properties are based on **edges**.

## Eulerian Path

An Eulerian path traverses **every edge exactly once** and does not have to return to the starting vertex.

## Eulerian Circuit

An Eulerian circuit traverses **every edge exactly once** and returns to the starting vertex.

---

## Eulerian Conditions — Undirected

### Eulerian Circuit

* All vertices with edges must belong to one connected component.
* Every vertex must have **even degree**.

### Implementation Algorithm

* Check connectivity.
* Calculate the degree of every vertex.
* If any vertex has odd degree → `False`.
* Otherwise → **Eulerian Circuit**.

### Eulerian Path

* All vertices with edges must belong to one connected component.
* Exactly **0 or 2 vertices** have odd degree.

### Implementation Algorithm

* Check connectivity.
* Count vertices with odd degree.
* `0` odd vertices → Eulerian circuit also exists.
* `2` odd vertices → Eulerian path exists.
* Otherwise → **Not Eulerian Path**.

---

## Eulerian Conditions — Directed

### Eulerian Circuit

The current implementation requires:

* Strong connectivity.
* For every vertex:

```text
inDegree = outDegree
```

### Implementation Algorithm

* Check strong connectivity.
* Calculate `inDegree` and `outDegree` for every vertex.
* Compare them.
* If any vertex has different values → `False`.
* Otherwise → **Eulerian Circuit**.

### Eulerian Path

The current implementation requires weak connectivity of the edge-containing part and checks degree balance.

### Implementation Algorithm

For every vertex:

* `outDegree = inDegree + 1` → possible starting vertex.
* `inDegree = outDegree + 1` → possible ending vertex.
* `inDegree = outDegree` → normal vertex.
* Any other difference → `False`.

Valid cases:

```text
0 start + 0 end → Eulerian Circuit
1 start + 1 end → Eulerian Path
```

---

# 7.Hamiltonian Graph

Hamiltonian properties are based on **vertices**, unlike Eulerian properties which are based on edges.

## Hamiltonian Path

A Hamiltonian path visits **every vertex exactly once**.

It does not need to return to the starting vertex.

## Hamiltonian Circuit

A Hamiltonian circuit visits **every vertex exactly once** and then returns to the starting vertex.

---

## Hamiltonian Path Algorithm

The implementation uses **backtracking**:

* Choose a starting vertex.
* Mark it as visited.
* Try an unvisited neighbour.
* Continue recursively.
* If all vertices are visited → **Hamiltonian Path Found**.
* If the path cannot be completed:

  * Undo the last choice.
  * Try another neighbour.
* Repeat for every possible starting vertex.

## Hamiltonian Circuit Algorithm

Uses the same backtracking approach with one additional condition:

* Choose a starting vertex.
* Build a path visiting every vertex exactly once.
* After visiting all vertices, check whether the final vertex connects back to the starting vertex.
* If yes → **Hamiltonian Circuit Found**.
* Otherwise backtrack and try another path.

### Important Point

Hamiltonian path/circuit detection is much more expensive than BFS/DFS in the general case, so backtracking can become very slow for large graphs.

---

## Eulerian vs Hamiltonian

| Property                | Eulerian                         | Hamiltonian                        |
| ----------------------- | -------------------------------- | ---------------------------------- |
| Based on                | Edges                            | Vertices                           |
| Path                    | Every edge exactly once          | Every vertex exactly once          |
| Circuit                 | Every edge exactly once + return | Every vertex exactly once + return |
| Implementation approach | Degree + connectivity            | Backtracking                       |

---

# 4. Graph Traversal Algorithms

## Breadth First Search (BFS)

BFS explores the graph **level by level**.

### Data Structure Used

`QueueLL` is used as the queue.

### Algorithm

- Validate the starting vertex.
- Create a queue.
- Create a `visited` set.
- Enqueue the starting vertex.
- Mark it visited.
- While the queue is not empty:
  - Dequeue a vertex.
  - Add it to the result.
  - Visit all unvisited neighbours.
  - Enqueue each newly discovered neighbour.
- Return the traversal order.

### Typical Uses

- Shortest path in an unweighted graph
- Level-order exploration
- Connectivity
- Finding nearby vertices

---

## Depth First Search (DFS)

DFS explores as deeply as possible before backtracking.

### Data Structure Used

`StackLL` is used as the stack.

### Algorithm

- Validate the starting vertex.
- Create a stack.
- Create a `visited` set.
- Push the starting vertex.
- Mark it visited.
- While the stack is not empty:
  - Pop a vertex.
  - Add it to the result.
  - Visit all unvisited neighbours.
  - Push newly discovered neighbours onto the stack.
- Return the traversal order.

### Typical Uses

- Cycle detection
- Connectivity
- Backtracking foundations
- Path exploration

---

# 5. Complexity Table

Let:

- `V` = number of vertices
- `E` = number of edges
- `deg(v)` = degree/number of neighbours of vertex `v`

| Method | Time Complexity | Extra Space | Notes |
|---|---:|---:|---|
| `add_vertex()` | `O(1)` average | `O(1)` | Dictionary insertion |
| `remove_vertex()` | `O(V)` | `O(1)` | Scans all vertices to remove references |
| `add_edge()` | `O(1)` average | `O(1)` | Dictionary insertion |
| `remove_edge()` | `O(1)` average | `O(1)` | Dictionary deletion |
| `has_vertex()` | `O(1)` average | `O(1)` | Dictionary lookup |
| `has_edge()` | `O(1)` average | `O(1)` | Nested dictionary lookup |
| `get_neighbours()` | `O(deg(v))` | `O(deg(v))` | Creates a list |
| `degree()` | `O(1)` average | `O(1)` | Undirected only |
| `inDegree()` | `O(V)` | `O(1)` | Scans every vertex |
| `outDegree()` | `O(1)` average | `O(1)` | Dictionary size |
| `isEmpty()` | `O(1)` | `O(1)` | Dictionary truth check |
| `display()` | `O(V + E)` | `O(V)` | Output/list construction |
| `display_graph()` | `O(V + E)` + layout/rendering | Depends on NetworkX layout | Visualization dominates in practice |
| `vertex_count()` | `O(1)` | `O(1)` | Dictionary size |
| `edge_count()` | `O(V)` | `O(1)` | Scans every adjacency dictionary |
| `bfs()` | `O(V + E)` | `O(V)` | Queue + visited set |
| `dfs()` | `O(V + E)` | `O(V)` | Stack + visited set |
| `is_complete()` | `O(V)` | `O(1)` | Uses `edge_count()` |
| `is_connected()` | `O(V + E)` | `O(V)` | Directed case performs DFS on original + reversed graph |
| `is_weakly_connected()` | `O(V² + E)` worst case | `O(V)` | Incoming-neighbour scan makes it quadratic |
| `is_cyclic()` | `O(V + E)` | `O(V)` | DFS-based |
| `is_bipartite()` | `O(V + E)` | `O(V)` | BFS colouring |
| `is_eulerian_circuit()` | `O(V + E)` | `O(V)` | Includes connectivity + degree checks |
| `is_eulerian_path()` | `O(V + E)` for undirected; `O(V² + E)` worst case for directed | `O(V)` | Directed case uses weak connectivity |
| `is_hamiltonian_path()` | `O(V!)` worst case | `O(V)` | Backtracking |
| `is_hamiltonian_circuit()` | `O(V!)` worst case | `O(V)` | Backtracking |
| `clear()` | `O(1)` | `O(1)` | Replaces dictionary |

> **Note:** Dictionary operations in Python are treated as **average `O(1)`**. NetworkX/Matplotlib layout and rendering are external visualization costs, so `display_graph()` does not have a single useful pure-DSA runtime bound.

---

# 6. BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Main structure | Queue | Stack |
| Exploration | Level by level | Depth first |
| Time | `O(V + E)` | `O(V + E)` |
| Space | `O(V)` | `O(V)` |
| Shortest path in unweighted graph | ✅ | ❌ Not guaranteed |
| Cycle detection | ✅ Possible | ✅ Very common |
| Typical use | Shortest paths, levels | Cycle detection, backtracking |

---

# 7. Eulerian vs Hamiltonian

| Feature | Eulerian | Hamiltonian |
|---|---|---|
| Focus | **Edges** | **Vertices** |
| Path condition | Every edge exactly once | Every vertex exactly once |
| Circuit | Return to start | Return to start |
| Typical algorithm here | Degree conditions | Backtracking |
| General difficulty | Polynomial-time checks for these properties | Exponential-time backtracking in general |

### Easy Memory Trick

```text
EULERIAN    → EDGES
HAMILTONIAN → VERTICES
```

---

# 8. Important Properties at a Glance

| Property | Main Idea |
|---|---|
| Complete | Every vertex directly connected to every other vertex |
| Connected | All relevant vertices belong to one connected component |
| Strongly Connected | In a directed graph, every vertex can reach every other vertex |
| Weakly Connected | Directed graph becomes connected when direction is ignored |
| Cyclic | Contains at least one cycle |
| Bipartite | Vertices can be split into two groups with no same-group edge |
| Eulerian Path | Uses every edge exactly once |
| Eulerian Circuit | Uses every edge exactly once and returns to start |
| Hamiltonian Path | Visits every vertex exactly once |
| Hamiltonian Circuit | Visits every vertex exactly once and returns to start |

---

# 9. Common Edge Cases

### Empty Graph

Most property/traversal methods in this implementation explicitly reject an empty graph with:

```python
raise Exception("Graph is Empty !")
```

### Missing Vertex

Operations involving a non-existent vertex raise `ValueError`.

### Duplicate Vertex

`add_vertex()` rejects duplicate vertices.

### Duplicate Edge

`add_edge()` rejects an edge that already exists.

### Self-loop

Self-loops are explicitly rejected:

```python
if source == destination:
    raise ValueError("Self-loop is not allowed !")
```

### Invalid Weight

Weighted graphs accept numeric weights but reject booleans and non-numeric values.

### Disconnected Graph

Algorithms such as bipartite checking and cycle checking explicitly iterate through all components where required.

### Directed Graph

Always pay attention to direction. `inDegree`, `outDegree`, strong connectivity, weak connectivity, and directed Eulerian conditions depend on edge direction.

---

# 10. Important Observations About This Implementation

1. **Adjacency-list representation** is efficient for sparse graphs because only existing edges are stored.
2. Undirected edges are stored twice internally — once in each direction — so `edge_count()` divides the total by `2`.
3. `is_connected()` uses a strong-connectivity test for directed graphs by running DFS on the graph and a reversed temporary graph.
4. `is_weakly_connected()` ignores direction by checking both outgoing and incoming adjacency relationships.
5. Hamiltonian checks use backtracking, so they can become extremely expensive as the number of vertices increases.
6. The implementation supports weighted graphs, so graph traversal itself ignores weights unless a future shortest-path algorithm explicitly uses them.
7. The current example graph in `__main__` is a **directed weighted graph** with six vertices and seven weighted edges.

---

# 11. Quick Revision Sheet

```text
GRAPH
 ├── Vertex + Edge
 ├── Directed / Undirected
 ├── Weighted / Unweighted
 └── Adjacency List

TRAVERSAL
 ├── BFS → Queue
 └── DFS → Stack

PROPERTIES
 ├── Complete
 ├── Connected
 ├── Strongly Connected
 ├── Weakly Connected
 ├── Cyclic
 └── Bipartite

EULERIAN
 ├── Path   → Every EDGE once
 └── Circuit → Every EDGE once + return

HAMILTONIAN
 ├── Path   → Every VERTEX once
 └── Circuit → Every VERTEX once + return

KEY COMPLEXITY
 ├── BFS / DFS             → O(V + E)
 ├── Cycle detection       → O(V + E)
 ├── Bipartite             → O(V + E)
 ├── Eulerian checks       → O(V + E) in the common/undirected path
 └── Hamiltonian           → O(V!) worst case
```

---

# 12. Formula Summary

### Undirected Complete Graph

```text
E = n(n - 1) / 2
```

### Directed Complete Graph

```text
E = n(n - 1)
```

### Eulerian — Undirected

```text
Circuit → all degrees even
Path    → 0 or 2 odd-degree vertices
```

### Eulerian — Directed

```text
Circuit → inDegree = outDegree for every vertex
Path    → at most one +1 start imbalance and one +1 end imbalance
```

### Graph Traversal

```text
BFS = O(V + E)
DFS = O(V + E)
```

---

## Final Concept Map

```text
                         GRAPH
                           |
          +----------------+----------------+
          |                                 |
       VERTICES                            EDGES
          |                                 |
   +------+-------+                  +------+------+
   |              |                  |             |
Complete      Connectivity        Directed      Weighted
                 |
        +--------+--------+
        |        |        |
   Connected  Strong   Weak
        |
   +----+----+
   |         |
Cyclic   Bipartite

        EDGE-BASED                    VERTEX-BASED
            |                              |
        EULERIAN                       HAMILTONIAN
        /       \                      /        \
      Path    Circuit                Path     Circuit
```
