# coding: utf-8
from util import *
from graph import Graph


# Depth-first graph search
def dfs(v1, v2, graph):
	fringe = [v1]
	parent = {v1:None}

	while (len(fringe) > 0):
		x = fringe.pop()

		if (x == v2):
			return parent

		for v in graph.adj(x):
			if not parent.has_key(v):
				fringe.append(v)
				parent[v] = x
	return None
