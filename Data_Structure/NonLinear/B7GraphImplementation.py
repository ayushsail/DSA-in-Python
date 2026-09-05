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
    def display(self) -> None :
        if self.isEmpty() : raise Exception("Graph is Empty !")

        print("\nGraph :")
        for vertex, neighbour in self.graph.items() :
            print(f"{vertex} -> {list(neighbour.keys())}")

        print()

# DISPLAY - GRAPH
    def display_graph(self) -> None : 
        pass


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
        

# BIPARTITE GRAPH - divide all vertices into 2 groups such that No two vertices in the same group have an edge.

# For directed, detect cycles using DFS recursion with path tracking.
# For undirected, detect cycles using DFS with parent tracking. 
    def is_bipartite(self) :
        pass





    












    def clear(self) -> None:
        self.graph = {}
    

if __name__ == "__main__" :
    g = Graph(True,False)

    print("added vertex : ", g.add_vertex("a"))
    print("added vertex : ", g.add_vertex("b"))
    print("added vertex : ", g.add_vertex("c"))
    print("added vertex : ", g.add_vertex("d"))
    print("added vertex : ", g.add_vertex("e"))
    print("added vertex : ", g.add_vertex("f"))


    print("added edge : ", g.add_edge("a","b"))
    print("added edge : ", g.add_edge("b","c"))
    print("added edge : ", g.add_edge("b","e"))
    print("added edge : ", g.add_edge("c","d"))
    print("added edge : ", g.add_edge("d","e"))
    print("added edge : ", g.add_edge("e","f"))
    print("added edge : ", g.add_edge("f","a"))


    print("neighbour of 'b' are : ",g.get_neighbours("b"))
    print("vertex count : ", g.vertex_count())
    print("edge count : ", g.edge_count())
    g.display()

    print("BFS from vertex 'a' : ", g.bfs("a"))
    print("BFS from vertex 'b' : ", g.bfs("b"))

    print("\nDFS from vertex 'd' : ", g.dfs("d"))
    print("DFS from vertex 'a' : ", g.dfs("a"))

    print("\nIs this graph a COMPLETE GRPAH : ", g.is_complete())
    print("\nIs this graph a CONNECTED GRPAH : ", g.is_connected())
    print("\nIs this graph a CYCLIC GRPAH : ", g.is_cyclic())
    





