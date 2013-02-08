# coding: utf-8


class Graph(object):
    """
        This implementation actualy doesn't permits:
            - two or more edges between vertices;
    """
    def __init__(self):
        self.edges = {}
        self.distances = {}

    def add_vertice(self, v):
        if v not in self.edges:
            self.edges[v] = []

    def add_edge(self, v1, v2, d=1):
        self.add_vertice(v1)
        self.add_vertice(v2)
        self.edges[v1].append(v2)
        self.distances[(v1, v2)] = d

    def adj(self, v):
        if v not in self.edges:
            raise VerticeNotFoundException
        return self.edges[v]

    def distance(self, v1, v2):
        if (v1, v2) not in self.distances:
            raise EdgeNotFoundException
        return self.distances[(v1, v2)]


class VerticeNotFoundException(BaseException):
    pass


class EdgeNotFoundException(BaseException):
    pass
