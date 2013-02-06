# coding: utf-8
from util import *
from graph import Graph


# Depth-first graph search
def dfs(source, target, graph):
	fringe = [source]
	parent = {source:None}

	while fringe:
		x = fringe.pop()

		if x == target:
			return parent

		for v in graph.adj(x):
			if v not in parent:
				fringe.append(v)
				parent[v] = x
	return None
