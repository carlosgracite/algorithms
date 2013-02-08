from graph import Graph
from util import build_path


def iterative_deepening(source, target, graph):
	""" 
		Iterative deepening depth-first graph search algorithm
	"""
	depth = 0

	while True:
		end = True
		fringe = [(source, 0)]
		parent = {source:None}

		while fringe:
			(v_in, curr_depth) = fringe.pop()

			if v_in == target:
				return build_path(parent, target)

			curr_depth += 1
			if curr_depth > depth:
				if graph.adj(v_in):
					end = False
				continue

			for v_out in graph.adj(v_in):
				if v_out not in parent:
					fringe.append((v_out, curr_depth))
					parent[v_out] = v_in

		if end: return None

		depth += 1

