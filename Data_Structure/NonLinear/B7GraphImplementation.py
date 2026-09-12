# for graph display
import networkx as nx
import matplotlib.pyplot as plt

from Data_Structure.Linear.A8QueueImplementation import QueueLL             # for BFS
from Data_Structure.Linear.A7StackIplementation import StackLL              # for DFS

class Graph :
    def __init__(self,directed=False, weighted=False) :
        self.directed = directed
        self.weighted = weighted
        self.graph = {}


# ADD VERTEX
    def add_vertex(self, vertex) -> str :
        # vertex validation
        if vertex in self.graph : raise ValueError("Vertex already exist !")

        self.graph[vertex] = {}
        return str(vertex)


# REMOVE VERTEX
    def remove_vertex(self, vertex) -> str :
        # vertex validation
        if vertex not in self.graph : raise ValueError("Vertex does not exist !")

        # delete the vertex
        del self.graph[vertex]

        # remove deleted vertex from all neighbour lists
        for othervertex in self.graph :
            if vertex in self.graph[othervertex] :
                del self.graph[othervertex][vertex]

        return str(vertex)


# ADD EDGE
    def add_edge(self,source,destination,weight=0) -> str :
        # source and destination vertices validation
        if source not in self.graph : raise ValueError("Source vertex does not exist !")
        if destination not in self.graph : raise ValueError("Destination vertex does not exist !")

        # same source & destination validation
        if source == destination: raise ValueError("Self-loop is not allowed !")

        # weight validation
        if self.weighted and (not isinstance(weight, (int, float)) or isinstance(weight, bool)):
            raise ValueError("Weight must be a number !")

        # edge validation
        if destination in self.graph[source] : raise ValueError("Edge already exist !")

        # add edge
        if self.weighted : 
            self.graph[source][destination] = weight

            if not self.directed :  
                self.graph[destination][source] = weight

        else :
            self.graph[source][destination] = None

            if not self.directed :
                self.graph[destination][source] = None

        # return description
        if self.directed : return f"{source} --> {destination}"
        else : return f"{source} <--> {destination}"


# REMOVE EDGE
    def remove_edge(self,source,destination) -> str :
        # source and destination vertices validation
        if source not in self.graph : raise ValueError("Source vertex does not exist !")
        if destination not in self.graph : raise ValueError("Destination vertex does not exist !")

        # edge validation
        if destination not in self.graph[source] : raise ValueError("Edge does not exist !")

        # remove edge
        del self.graph[source][destination]

        if not self.directed :
            del self.graph[destination][source]
        
        # return description
        if self.directed : return f"{source} --> {destination}"
        else : return f"{source} <--> {destination}"


# HAS VERTEX
    def has_vertex(self,vertex) -> bool :
        return vertex in self.graph 


# HAS EDGE
    def has_edge(self,source,destination) -> bool : 
        if source not in self.graph or destination not in self.graph:
            raise ValueError("Source or destination vertex does not exist !")
        return destination in self.graph[source]


# GET NEIGHBOURS
    def get_neighbours(self,vertex) -> list :
        if not self.has_vertex(vertex) : raise ValueError("vertex does not exist !")

        return list(self.graph[vertex].keys())


# DEGREE
    def degree(self,vertex) -> int :
        if vertex not in self.graph : raise ValueError("Vertex does not exist !")
        if self.directed : raise Exception("The Graph is Directed Graph !")

        return len(self.graph[vertex])


# IN-DEGREE
    def inDegree(self,vertex) -> int :
        if vertex not in self.graph : raise ValueError("Vertex does not exist !")
        if not self.directed : raise Exception("The Graph is Undirected Graph !")

        inDegree = 0
        for othervertex in self.graph :
            if vertex in self.graph[othervertex] :
                inDegree += 1

        return inDegree


# OUT-DEGREE
    def outDegree(self,vertex) -> int :
        if vertex not in self.graph : raise ValueError("Vertex does not exist !")
        if not self.directed : raise Exception("The Graph is Undirected Graph !")

        return len(self.graph[vertex])


# IS-EMPTY
    def isEmpty(self) -> bool :
        return  not self.graph


# DISPLAY - ADJACENCY LIST
    def display(self) -> None:
        if self.isEmpty():
            raise Exception("Graph is Empty !")

        print("\nGraph :")

        for vertex, neighbours in self.graph.items():

            if self.weighted:
                edge_list = []

                for neighbour, weight in neighbours.items():
                    edge_list.append(f"{neighbour}({weight})")

                print(f"{vertex} -> {edge_list}")

            else:
                print(f"{vertex} -> {list(neighbours.keys())}")

        print()


# DISPLAY - GRAPH
    def display_graph(self) -> None:
        if self.isEmpty():
            raise Exception("Graph is Empty !")

        # Create NetworkX graph based on graph type
        if self.directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        # Add vertices and edges
        for vertex in self.graph:
            G.add_node(vertex)

            for neighbour in self.graph[vertex]:
                if self.weighted:
                    G.add_edge(
                        vertex,
                        neighbour,
                        weight=self.graph[vertex][neighbour]
                    )
                else:
                    G.add_edge(vertex, neighbour)

        # Create better layout
        pos = nx.spring_layout(
            G,
            k=2.5,
            iterations=200,
            seed=42
        )

        # Create figure
        plt.figure(figsize=(12, 8))

        # Draw nodes
        nx.draw_networkx_nodes(
            G,
            pos,
            node_size=1000,
            node_color="skyblue",
            edgecolors="black",
            linewidths=1.5
        )

        # Draw edges
        nx.draw_networkx_edges(
            G,
            pos,
            arrows=self.directed,
            arrowsize=20,
            edge_color="gray",
            width=1.8,
            connectionstyle="arc3,rad=0.08",
            min_source_margin=15,
            min_target_margin=15
        )

        # Draw vertex names
        nx.draw_networkx_labels(
            G,
            pos,
            font_size=12,
            font_weight="bold"
        )

        # Draw edge weights
        if self.weighted:
            edge_labels = nx.get_edge_attributes(G, "weight")

            nx.draw_networkx_edge_labels(
                G,
                pos,
                edge_labels=edge_labels,
                font_size=10,
                font_weight="bold",
                label_pos=0.5,
                bbox=dict(
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.8,
                    pad=2
                ),
                rotate=False
            )

        plt.axis("off")
        plt.tight_layout()
        plt.show()


# VERTEX COUNT
    def vertex_count(self) -> int :
        return len(self.graph)


# EDGE COUNT
    def edge_count(self) -> int :
        count = 0
        for vertex in self.graph :
            count += len(self.graph[vertex])

        if not self.directed :  count //= 2 

        return count


# BREADTH FIRST SEARCH
    def bfs(self, start) -> list :
        if start not in self.graph : raise ValueError("Vertex does not exist !")

        queue = QueueLL()
        visited = set()
        result = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.isEmpty() : 
            vertex = queue.dequeue()
            result.append(vertex)

            for neighbour in self.graph[vertex] :
                if neighbour not in visited :
                    queue.enqueue(neighbour)
                    visited.add(neighbour)

        return result


# DEPTH FIRST SEARCH
    def dfs(self,start) -> list :
        if start not in self.graph : raise ValueError("Vertex does not exist !")

        stack = StackLL()
        visited = set()
        result = []

        stack.push(start)
        visited.add(start)

        while not stack.isEmpty() :
            vertex = stack.pop()
            result.append(vertex)

            for neighbour in self.graph[vertex] :
                if neighbour not in visited :
                    stack.push(neighbour)
                    visited.add(neighbour)

        return result


# COMPLETE GRAPH - Checks whether every vertex is directly connected to every other vertex.
# For n vertices, an undirected complete graph has exactly n(n-1)/2 edges.
# For n vertices, an directed complete graph has exactly n(n-1) edges.
    def is_complete(self) -> bool :
        n = self.vertex_count()

        if self.directed : 
            return self.edge_count() == n * (n - 1)
        else : 
            return self.edge_count() == n * (n - 1) // 2


# CONNECTED GRAPH - checks whether all vertices in the graph belong to one connected group.
# For undirected, if dfs from any vertex == total vertex count -> connected graph
# For directed, if dfs from any vertex == reverse dfs from that vertex == total vertex count -> connected graph
    def is_connected(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        start = next(iter(self.graph))
        lengthOfDfs = len(self.dfs(start))

        # FOR UNDIRECTED GRAPH
        if not self.directed :
            return lengthOfDfs == self.vertex_count()
        

        # FOR DIRECTED GRAPH (strongly connected check)
        else :
            # create a temporary Graph
            tempGraph = Graph(self.directed,self.weighted)
            # add all vertices in tempGraph from main graph
            for vertex in self.graph :
                tempGraph.add_vertex(vertex)

            # reverse every edge
            for source in self.graph :
                for neighbour in self.graph[source] :
                    weight = self.graph[source][neighbour]
                    tempGraph.add_edge(neighbour,source,weight)

            lengthOfReverseDfs = len(tempGraph.dfs(start))

            return lengthOfDfs == self.vertex_count() and lengthOfReverseDfs == self.vertex_count()


# WEAKLY CONNECTED GRAPH - Check connectivity ignoring edge direction
# - Specially for Directed graph only
    def is_weakly_connected(self) -> bool:
        if self.isEmpty():
            raise Exception("Graph is Empty !")

        # Find a vertex that has at least one edge
        start = None
        for vertex in self.graph:
            if self.inDegree(vertex) + self.outDegree(vertex) > 0:
                start = vertex
                break

        # No edges in the graph
        if start is None:
            return True

        queue = QueueLL()
        visited = set()

        queue.enqueue(start)
        visited.add(start)

        while not queue.isEmpty():
            vertex = queue.dequeue()

            # Outgoing edges
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.enqueue(neighbour)

            # Incoming edges
            for othervertex in self.graph:
                if vertex in self.graph[othervertex]:
                    if othervertex not in visited:
                        visited.add(othervertex)
                        queue.enqueue(othervertex)

        # Count vertices that actually have edges
        edge_vertices = 0
        for vertex in self.graph:
            if self.inDegree(vertex) + self.outDegree(vertex) > 0:
                edge_vertices += 1

        return len(visited) == edge_vertices


# CYCLIC GRAPH - check path starting and ending at same vertex, without repeating vertices in between.
# For directed, detect cycles using DFS recursion with path tracking.
# For undirected, detect cycles using DFS with parent tracking. 
    def is_cyclic(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        # FOR DIRECTED GRAPH
        if self.directed :
            visited = set()
            current_path = set()

            def dfs_directed(vertex) :
                visited.add(vertex)
                current_path.add(vertex)

                for neighbour in self.graph[vertex] :

                    # Neighbour is in current dfs path -> cyclic graph
                    if neighbour in current_path : return True

                    # Neighbour is not visited -> dfs neighbour
                    if neighbour not in visited :
                        if dfs_directed(neighbour) : return True

                current_path.remove(vertex)
                return False
            
            # Check every component
            for vertex in self.graph :
                if vertex not in visited :
                        if dfs_directed(vertex) : return True


            # FOR UNDIRECTED GRAPH
            else :
                visited = set()

                def dfs_undirected(vertex,parent) :
                    visited.add(vertex)

                    for neighbour in self.graph[vertex] :

                        # Neighbour is not visited → continue DFS
                        if neighbour not in visited : 
                            if dfs_undirected(neighbour, vertex) : return True

                        # Neighbour is already visited and is not the parent -> Cyclic Graph
                        elif neighbour in visited and neighbour != parent : return True

                    return False

                # Check every component
                for vertex in self.graph :
                    if vertex not in visited :   
                        if dfs_undirected(vertex,None) : return True


            return False
        

# BIPARTITE GRAPH - divide all vertices into 2 groups such that no two vertices in the same group have an edge.
# - Every pair of adjacent vertices must have opposite colors.
# - using color as 0 and 1
    def is_bipartite(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        color = {}

        def bfs(vertex) :
            # assign color for the vertex
            color[vertex] = 0
            queue = QueueLL()
            queue.enqueue(vertex)
    
            while not queue.isEmpty() : 
                vertex = queue.dequeue()

                for neighbour in self.graph[vertex] :
                    # if adjacent vertices has no color, assign opposite color of vertex
                    if neighbour not in color :
                        color[neighbour] = 1 - color[vertex]
                        queue.enqueue(neighbour)

                    # If adjacent vertices have the same color, graph is not bipartite
                    elif color[neighbour] == color[vertex] : return False
    
            return True
        
        # Check every connected component
        # This is necessary because the graph may be disconnected.
        for vertex in self.graph :
            if vertex not in color :
                if not bfs(vertex) : return False

        return True


# EULERIAN GRAPH - there are two things - Eulerian circuit & Eulerian path.
# 1. Eulerian Circuit - traverse every edge exactly once and return to the starting vertex.
# Undirected:
#   - Graph must be connected
#   - Every vertex must have even degree
# Directed:
#   - Graph must be strongly connected
#   - inDegree(vertex) == outDegree(vertex)
    def is_eulerian_circuit(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        # UNDIRECTED GRAPH
        if not self.directed : 
            # An Eulerian circuit requires the graph to be connected
            if not self.is_connected() : return False

            # Check degree of every vertex  
            # Any odd-degree vertex means no Eulerian circuit
            for vertex in self.graph :
                if self.degree(vertex) % 2 != 0 : return False

            return True

        # DIRECTED GRAPH
        else :
            # An Eulerian circuit requires the graph to be strongly connected
            if not self.is_connected() : return False

            # Check In-degree & Out-degree of every vertex  
            # different In-degree & Out-degree of vertex means no Eulerian circuit
            for vertex in self.graph :
                if self.inDegree(vertex) != self.outDegree(vertex) : return False

            return True     
        

# 2. Eulerian Path - Traverses every edge exactly once, but does NOT necessarily return to the starting vertex.
# - exactly 2 vertices have odd degree
# Undirected:
#   - Graph must be connected
#   - Exactly 0(eulerian circuit) or 2 vertices have odd degree
# Directed:
#   - All vertices with edges must belong to one weakly connected component
#   - Either:
#       inDegree == outDegree for every vertex → Eulerian circuit
#       0 or 1 vertex: outDegree = inDegree + 1 → starting vertex
#       0 or 1 vertex: inDegree = outDegree + 1 → ending vertex
#       all others have inDegree == outDegree
    def is_eulerian_path(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        # UNDIRECTED GRAPH
        if not self.directed : 
            # An Eulerian path requires all vertices with edges to be connected
            if not self.is_connected() : return False

            # Check degree of every vertex  
            # Any odd-degree vertex means no Eulerian circuit
            odd_count = 0
            for vertex in self.graph :
                if self.degree(vertex) % 2 != 0 : 
                    odd_count += 1

            # Eulerian path exists with 0 or 2 odd-degree vertices
            if odd_count == 0 or odd_count == 2: return True

            return False

        # DIRECTED GRAPH
        else :
             # Check connectivity ignoring edge direction
            if not self.is_weakly_connected():
                return False

            # Check In-degree & Out-degree of every vertex
            start_count = 0
            end_count = 0
            for vertex in self.graph :
                # START vertex
                if self.outDegree(vertex) == self.inDegree(vertex) + 1 : 
                    start_count += 1

                # END vertex
                elif self.inDegree(vertex) == self.outDegree(vertex) + 1 : 
                    end_count += 1

                # NORMAL vertex
                elif self.inDegree(vertex) == self.outDegree(vertex) : 
                    pass

                else : return False


        if (start_count == 0 and end_count == 0) or \
            (start_count == 1 and end_count == 1) :
            return True


# HAMILTONIAN GRAPH - there are two things - Hamiltonian path & Hamiltonian circuit.
# 1. Hamiltonian Path - Traverses every vertex exactly once,
#    but does NOT necessarily return to the starting vertex.
    def is_hamiltonian_path(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        visited = set()
        path = []

        def backtrack(vertex) :
            # base condition
            if len(path) == self.vertex_count() : return True

            # try all neighbours 
            for neighbour in self.graph[vertex] :
                if neighbour not in visited :
                    visited.add(neighbour)
                    path.append(neighbour)

                    # explore neighbour
                    if backtrack(neighbour) : return True
                    
                    # backtrack and try different path
                    else : 
                        path.pop()
                        visited.remove(neighbour)

            # no valid path found
            return False
          

        for vertex in self.graph :
            # choose a starting vertex
            visited.add(vertex)
            path.append(vertex)

            if backtrack(vertex) : return True

            # backtrack and try different path
            else :
                path.pop()
                visited.remove(vertex)

        # no valid path found
        return False


# 2. Hamiltonian Circuit - Traverses every vertex exactly once
#    and returns to the starting vertex.
    def is_hamiltonian_circuit(self) -> bool :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        visited = set()
        path = []

        def backtrack(vertex,start) :
            # Base condition:
            # - Visit every vertex
            # - Last vertex should connect back to starting vertex
            if len(path) == self.vertex_count() : 
                if start in self.graph[vertex] :
                    return True
                
            # try all neighbours 
            for neighbour in self.graph[vertex] :
                if neighbour not in visited :
                    visited.add(neighbour)
                    path.append(neighbour)


                    # explore neighbour
                    if backtrack(neighbour,start) : return True
                    
                    # backtrack and try different path
                    else : 
                        path.pop()
                        visited.remove(neighbour)

            # no valid path found
            return False

        for vertex in self.graph :
            # choose a starting vertex
            visited.add(vertex)
            path.append(vertex)

            if backtrack(vertex,vertex) : return True

            # else, undo this choice and try different path
            else :
                path.pop()
                visited.remove(vertex)

        # no valid path found
        return False


# CLEAR GRAPH
    def clear(self) -> None:
        self.graph = {}

    

if __name__ == "__main__" :
    g = Graph(True,True)

    print("added vertex : ", g.add_vertex("a"))
    print("added vertex : ", g.add_vertex("b"))
    print("added vertex : ", g.add_vertex("c"))
    print("added vertex : ", g.add_vertex("d"))
    print("added vertex : ", g.add_vertex("e"))
    print("added vertex : ", g.add_vertex("f"))


    print("added edge : ", g.add_edge("a","b",10))
    print("added edge : ", g.add_edge("b","c",2))
    print("added edge : ", g.add_edge("b","e",5))
    print("added edge : ", g.add_edge("c","d",7))
    print("added edge : ", g.add_edge("d","e",8))
    print("added edge : ", g.add_edge("e","f",1))
    print("added edge : ", g.add_edge("f","a",4))


    print("\nneighbour of 'b' are : ",g.get_neighbours("b"))
    print("vertex count : ", g.vertex_count())
    print("edge count : ", g.edge_count())
    g.display()

    print("\nBFS from vertex 'a' : ", g.bfs("a"))
    print("BFS from vertex 'b' : ", g.bfs("b"))

    print("\nDFS from vertex 'd' : ", g.dfs("d"))
    print("DFS from vertex 'a' : ", g.dfs("a"))
    
    g.display()

    print("\nIs this graph a COMPLETE GRPAH : ", g.is_complete())
    print("\nIs this graph a CONNECTED GRPAH : ", g.is_connected())
    print("\nIs this graph a WEAKLY CONNECTED GRPAH : ", g.is_weakly_connected())
    print("\nIs this graph a CYCLIC GRPAH : ", g.is_cyclic())
    print("\nIs this graph a BIPARTITE GRPAH : ", g.is_bipartite())
    print("\nIs this graph has a EULERIAN CIRUIT : ", g.is_eulerian_circuit())
    print("\nIs this graph has a EULERIAN PATH : ", g.is_eulerian_path())
    print("\nIs this graph has a HAMILTONIAN CIRUIT : ", g.is_hamiltonian_circuit())
    print("\nIs this graph has a HAMILTONIAN PATH : ", g.is_hamiltonian_path())

    g.display_graph()