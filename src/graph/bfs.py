# coding: utf-8
from util import build_path
from graph import Graph


# Breadth-first graph search
def bfs(source, target, graph):
	fringe = [source]
	parent = {source:None}

	while fringe:
		x = fringe.pop(0)

		if x == target:
			return parent

		for v in graph.adj(x):
			if v not in parent:
				fringe.append(v)
				parent[v] = x
	return None
