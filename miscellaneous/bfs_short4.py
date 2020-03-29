graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def short(graph, start, goal):
	queue = [[start]]
	while(queue):
		path = queue.pop(0)
		node = path[-1]
		for n in graph[node]:
			new_path = list(path)
			new_path.append(n)
			queue.append(new_path)
			if n == goal:
				return new_path
	return -1

print(short(graph, 'E','F'))