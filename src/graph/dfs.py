from util import *

class VerticeNotFoundException(BaseException):
	pass


class Graph(object):
	def __init__(self):
		self.n = 0
		self.edges = {}

	def add_vertice(self, v):
		if not self.edges.has_key(v):
			self.edges[v] = []

	def add_edge(self, v1, v2):
		self.add_vertice(v1)
		self.add_vertice(v2)
		self.edges[v1].append(v2)

	def adj(self, v):
		if v not in self.edges:
			raise VerticeNotFoundException
		return self.edges[v]


def dfs2(v1, v2, graph):
	visited = []
	fringe = [v1]
	parent = {}
	while (len(fringe) > 0):
		x = fringe.pop()
		if (x == v2):
			return parent
		visited.append(x)
		for v in graph.adj(x):
			if (v not in visited):
				fringe.append(v)
				parent[v] = x
	return None

# Implementacao classica do algoritmo.
# Algoritmo ajustado para sempre expandir respeitando
#  a ordem que os nos foram inseridos no grafo.
def dfs(v1, v2, graph):
	fringe = [v1]
	parent = {v1:None}
	while (len(fringe) > 0):
		x = fringe.pop()

		if (x == v2):
			return parent

		l = graph.adj(x)
		l.reverse()
		for v in l:
			fringe.append(v)
			parent[v] = x
	return None


x = Graph()
x.add_edge('s', 'd')
x.add_edge('s', 'e')
x.add_edge('s', 'p')
x.add_edge('b', 'a')
x.add_edge('d', 'b')
x.add_edge('d', 'c')
x.add_edge('d', 'e')
x.add_edge('p', 'q')
x.add_edge('c', 'a')
x.add_edge('h', 'p')
x.add_edge('h', 'q')
x.add_edge('e', 'h')
x.add_edge('e', 'r')
x.add_edge('r', 'f')
x.add_edge('f', 'c')
x.add_edge('f', 'g')

print build_path(dfs('s', 'g', x), 'g')