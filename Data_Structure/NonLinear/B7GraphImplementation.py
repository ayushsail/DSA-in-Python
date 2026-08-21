from Data_Structure.Linear.A8QueueImplementation import QueueLL

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

    print("added edge : ", g.add_edge("d","a"))
    print("added edge : ", g.add_edge("d","b"))
    print("added edge : ", g.add_edge("d","c"))
    print("added edge : ", g.add_edge("d","e"))
    print("added edge : ", g.add_edge("d","f"))

    print("added edge : ", g.add_edge("c","a"))
    print("added edge : ", g.add_edge("a","b"))
    print("added edge : ", g.add_edge("b","f"))
    print("added edge : ", g.add_edge("e","f"))
    print("added edge : ", g.add_edge("e","c"))

    print("neighbour of 'd' are : ",g.get_neighbours("d"))
    print("vertex count : ", g.vertex_count())
    print("edge count : ", g.edge_count())
    g.display()


    print("BFS from vertex 'd' : ", g.bfs("d"))
    print("BFS from vertex 'a' : ", g.bfs("a"))






