# coding: utf-8
from util import build_path
from graph import Graph


def dfs(source, target, graph):
	""" Depth-first graph search """
	fringe = [source]
	parent = {source:None}

	while fringe:
		x = fringe.pop()

		if x == target:
			return build_path(parent, target)

		for v in graph.adj(x):
			if v not in parent:
				fringe.append(v)
				parent[v] = x
	return None
