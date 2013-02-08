from Queue import PriorityQueue
from graph import Graph
from util import build_path


def null_heuristic(state, graph):
    return 0

def astar(source, target, graph, heuristic=null_heuristic):
    """ A* algorithm """
    queue = PriorityQueue()
    queue.put((0, source))
    
    parent = {source:None}
    visited = {}

    while not queue.empty():
        (d, v_in) = queue.get()

        if v_in not in visited or d < visited[v_in]:

            if v_in == target:
                return (d, build_path(parent, target))

            for v_out in graph.adj(v_in):
                cost = graph.distance(v_in, v_out) + d
                fn = cost + heuristic(v_out, graph) # only diference in retion to UCS
                if v_out not in visited:
                    queue.put((fn, v_out))
                    parent[v_out] = v_in

            visited[v_in] = cost

    return None
