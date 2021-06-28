from math import inf 
from collections import deque
class Graph: 
    def __init__(self, matrix) -> None:
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
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = inf  # shortest distance from source
            vertex.potential_wall_breaks = None
    
    def add_edges(self):
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
        output = ""
        for vertex in self.vertices:
            output += f"Vertex {str(vertex)}\n"
        return output 
    
    def bfs_with_bomb(self, source, sink, bombs):
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
                print(u)
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
    def __init__(self, id, x, y, is_wall) -> None:
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
        self.edges.append(edge)

    def __str__(self) -> str:
        output=f"{str(self.id)}: [{str(self.y)}][{str(self.x)}] {'!' if self.is_wall else ''}\n  Edges: "
        for edge in self.edges:
            output += f"{str(edge)}, "
        return output 

class Edge: 
    def __init__(self, u, v, w = 1) -> None:
        self.u = u 
        self.v = v
        self.w = w 
    
    def __str__(self) -> str:
        return f"({self.u},{self.v})"

def main():
    # map = [
    #     [0, 1, 1, 0], 
    #     [0, 0, 0, 1], 
    #     [1, 1, 0, 0], 
    #     [1, 1, 1, 0]
    # ]

    map = [
        [0,0,0],
        [1,0,1],
        [0,0,1],
        [0,1,0],
        [0,0,0]
    ]

    # map = [
    #     [0, 0, 0, 0, 0, 0], 
    #     [1, 1, 1, 1, 1, 0], 
    #     [0, 0, 0, 0, 0, 0], 
    #     [0, 1, 1, 1, 1, 1], 
    #     [0, 1, 1, 1, 1, 1], 
    #     [0, 0, 0, 0, 0, 0]
    # ]

    graph = Graph(map)
    # print(graph)

    height = len(map)
    width = len(map[0])
    source = 0 
    sink = (height * width) - 1
    print(sink)
    bombs = 1
    print(graph.bfs_with_bomb(source, sink, bombs))

if __name__ == "__main__":
    main()