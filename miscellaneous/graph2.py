graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
vertex = list(graph.keys())

def dfs(graph):
	visited = {}
	vertex = list(graph.keys())
	for v in range(0, len(vertex)):
		if vertex[v] not in visited:
			visited[vertex[v]] = 1
			visit(visited, graph[vertex[v]])
	return visited

def visit(visited, edjes):
	for e in range(0, len(edjes)):
		if edjes[e] not in visited:
			print(edjes[e])
			visited[edjes[e]] = 1
	return visited
print(dfs(graph))