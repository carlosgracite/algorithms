def build_path(search_tree, v):
	if search_tree == None or search_tree == {}:
		return []

	path = []
	while search_tree.has_key(v) and v != None:
		path.insert(0, v)
		v = search_tree[v]
	return path