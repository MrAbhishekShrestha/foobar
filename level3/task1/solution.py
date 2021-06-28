"""
Google Foobar 
Challenge 3 
Task 1 

date: 26th June 2021
"""

from math import inf 
from collections import deque                
class Graph: 
    """
    Representing the Maze as a Graph 
    """
    def __init__(self, matrix) -> None:
        """
        Initialize a Graph where each vertex represents a box in the matrix 
        Each vertex is given a unique id 
        """
        self.matrix = matrix 
        self.vertices = []
        self.height = len(matrix)
        self.width = len(matrix[0]) 
        id = 0 
        for i in range(self.height):
            for j in range(self.width):
                self.vertices.append(Vertex(id, j, i, self.matrix[i][j] == 1))
                id += 1 

        self.add_edges()

    def reset(self):
        """
        Resets attributes of each vertex 
        """
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = inf  # shortest distance from source
            vertex.potential_wall_breaks = None
    
    def add_edges(self):
        """
        Add edges between the vertices in the UNDIRECTED graph. 
        For each vertex, add an edge to the vertex (if it exists) to its bottom and right.
        """
        limit = self.height * self.width
        for id in range(limit):
            down = right = None 
            if id + self.width < limit:
                down = id + self.width 
            if id % self.width < self.width - 1:
                right = id + 1
            
            current = self.vertices[id]
            if down is not None: 
                current.add_edge(Edge(id, down))
                # undirected 
                down_vertex = self.vertices[down]
                down_vertex.add_edge(Edge(down, id))
            if right is not None: 
                current.add_edge(Edge(id, right))
                # undirected 
                right_vertex = self.vertices[right]
                right_vertex.add_edge(Edge(right, id))
    
    def __str__(self) -> str:
        """
        String representation of the graph. 
        """
        output = ""
        for vertex in self.vertices:
            output += f"Vertex {str(vertex)}\n"
        return output 
    
    def bfs_with_bomb(self, source, sink, bombs):
        """
        uses bfs to find shortest path from source to sink. Terminates when sink vertex is reached.
        returns distance of shortest path 
        returns inf when there is no path from source to sink 
        :param: bombs - number of bombs have -> number of walls that can be blasted
        
        discovered is a deque
        initially, source.potential_wall_breaks = bombs. This information is propagated to neighboring
        vertices. If neighboring vertex is a wall, potential_wall_breaks decrements by 1. 
        As long as potential_wall_break is not negative, current wall can be blasted & traversed.
        """
        source = self.vertices[source]
        sink = self.vertices[sink]

        discovered = deque()
        discovered.append(source)
        source.discovered = True
        source.distance = 1 
        source.potential_wall_breaks = bombs 
        while discovered:
            u = discovered.popleft()
            u.visited = True 

            if u == sink:
                return u.distance

            for edge in u.edges:
                v = self.vertices[edge.v]
                if not v.discovered:
                    v.discovered = True 
                    v.distance = u.distance + 1
                    if v.is_wall:
                        v.potential_wall_breaks = u.potential_wall_breaks - 1
                        if v.potential_wall_breaks < 0:
                            continue 
                    else: 
                        v.potential_wall_breaks = u.potential_wall_breaks
                    discovered.append(v)
        return inf 
                    
class Vertex: 
    """
    A Graph contains many vertices 
    """
    def __init__(self, id, x, y, is_wall) -> None:
        """
        Initializes a Vertex object
        Keeps track of its OUTGOING edges only 
        has `potential_wall_break` to track number of walls that can be passed through by blasting walls
        """
        self.id = id 
        self.x = x 
        self.y = y 
        self.is_wall = is_wall
        self.edges = []

        self.discovered = False 
        self.visited = False 
        self.distance = inf 
        self.potential_wall_breaks = None 
        self.previous = None 
    
    def add_edge(self, edge):
        """
        Add Edge from current vertex to another vertex in the graph 
        """
        self.edges.append(edge)

    def __str__(self) -> str:
        """
        String representation of Vertex Object 
        ! at the end if vertex is a wall 
        """
        output=f"{str(self.id)}: [{str(self.y)}][{str(self.x)}] {'!' if self.is_wall else ''}\n  Edges: "
        for edge in self.edges:
            output += f"{str(edge)}, "
        return output 

class Edge: 
    """
    Edges connect the Vertices in the Graph 
    """
    DEFAULT_WEIGHT = 1
    def __init__(self, u, v, w = DEFAULT_WEIGHT) -> None:
        """
        Constructor
        Since this is an unweighted graph, each edge has weight of 1 
        u and v are the ids of the two vertices this edge connects 
        """
        self.u = u 
        self.v = v
        self.w = w 
    
    def __str__(self) -> str:
        """
        String representation of an Edge 
        """
        return f"({self.u},{self.v})"

def solution(map):
    """
    Working Solution
    Finds shortest path in given map (2D matrix) from source (0,0) to sink (w-1, h-1)
    Converts map into a graph 
    runs a modified version of BFS to find the length of shortest path 
    """
    graph = Graph(map)
    # print(graph)

    height = len(map)
    width = len(map[0])
    source = 0 
    sink = (height * width) - 1
    bombs = 1
    return graph.bfs_with_bomb(source, sink, bombs)

def main():
    map = [
        [0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]
    ]
    # print(solution1(map))
    print(solution(map))

    map = [
        [0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0]
    ]
    print(solution(map))

    map = [
        [0,0,0],
        [1,0,1],
        [0,0,1],
        [0,1,0],
        [0,0,0]
    ]
    print(solution(map))

if __name__ == "__main__":
    main()
