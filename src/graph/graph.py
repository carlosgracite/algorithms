# coding: utf-8

class VerticeNotFoundException(BaseException):
	pass


class Graph(object):
	def __init__(self):
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
