graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_short(graph, start, target):
	visited = {}
	queue = [[start]]

	if start == target:
		return queue
	while(queue):
		print(queue)
		path = queue.pop(0)
		node = path[-1]
		if node not in visited:
			visited[node] = 1
			
			for n in graph[node]:
				new_list = list(path)
				new_list.append(n)
				print("nl ",path)
				queue.append(new_list)
				if n == target:
					return new_list
				
	return -1

print(bfs_short(graph, 'G', 'E'))

[['G']]
[['G', 'C']]
[['G', 'C', 'A'], ['G', 'C', 'F'], ['G', 'C', 'G']]
['G', 'C', 'A', 'E']




