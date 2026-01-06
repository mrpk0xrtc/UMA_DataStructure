class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

class Graph:
    def __init__(self): pass
    def __str__(self): pass
    def add_vertex(self, vertex): pass
    def add_edge(self, v1, v2): pass
    def remove_edge(self, v1, v2): pass
    def remove_vertex(self, vertex): pass
    def BFS(self): pass
    def DFS(self): pass
