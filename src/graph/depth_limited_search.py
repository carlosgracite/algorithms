# coding: utf-8
from graph import Graph
from util import build_path

def depth_limited_search(source, target, graph, depth):
	""" 
		Depth-limited graph search.
		The minimum depth parameter is 0, corresponding 
		to the root node (source).
	"""
	fringe = [(source, 0)]
	parent = {source:None}

	while fringe:
		(v_in, curr_depth) = fringe.pop()

		if v_in == target:
			return build_path(parent, target)

		curr_depth += 1

		if curr_depth > depth:
			continue

		for v_out in graph.adj(v_in):
			if v_out not in parent:
				fringe.append((v_out, curr_depth))
				parent[v_out] = v_in
				
	return None
