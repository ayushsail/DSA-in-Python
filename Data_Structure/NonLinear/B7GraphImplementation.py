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


    def has_vertex(self,vertex) -> bool :
        return vertex in self.graph 

    def has_edge(self,source,destination) -> bool : 
        if source not in self.graph or destination not in self.graph:
            raise ValueError("Source or destination vertex does not exist !")
        return destination in self.graph[source]


    def get_neighbours(self,vertex) -> list :
        if not self.has_vertex(vertex) : raise ValueError("vertex does not exist !")

        return list(self.graph[vertex].keys())