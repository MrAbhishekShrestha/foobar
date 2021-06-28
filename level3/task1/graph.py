from math import inf 

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
            if id + self.height < limit:
                down = id + self.height 
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
    
    def add_edge(self, edge):
        self.edges.append(edge)
        
    def __eq__(self, other) -> bool:
        return (self.x == other.x and self.y == other.y) or self.id == other.id

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
    map = [
        [0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]
    ]
    graph = Graph(map)
    print(graph)

if __name__ == "__main__":
    main()