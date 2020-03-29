graph = {
	'A' : ['B','C','D'],
	'B' : ['A','E'],
	'C' : ['A','E','F'],
	'D' : ['A','G'],
	'E' : ['B','C'],
	'F' : ['C','G'],
	'G' : ['D','F']
}

def bfs(graph, start, goal):
	queue = [[start]]
	visited = {}
	while queue:
		path = queue.pop()
		node = path[-1] # because it is a queue, the -1 or the end will remain unvisited
		print("node: ",node)
		if node not in visited:
			for n in graph[node]:
				new_path = list(path)
				new_path.append(n)
				queue.append(new_path)
				if n == goal:
					return new_path
			visited[node] = 1
	return False

print(bfs(graph, 'B', 'G')) #['B', 'E', 'C', 'F', 'G']
#1step -> visited will be BAE
#2 step -> visited will be
"""
node:  B
node:  E
node:  C
node:  F

"""