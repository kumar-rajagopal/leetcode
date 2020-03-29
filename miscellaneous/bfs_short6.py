graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_short(graph, start, target):
	if start == target:
		return
	visited = {}
	queue = [[start]]
	while(queue):
		print('que ',queue)
		path = queue.pop()
		node = path[-1]
		print('node ',node)
		if node not in visited:
			for n in graph[node]:
				new_path = list(path)
				new_path.append(n)
				queue.append(new_path)
				if target == n:
					return new_path
			visited[node] = 1
	return -1

print(bfs_short(graph, 'G', 'E'))
"""
Visit G - start
C
From C visit
A
F
G is -1 now so visit nodes of G
From G 
C already visited call goes to key C and now F is popped from queue but F of C is visited and so now A is popped and nodes in keys of A is visited
B
C
E - target
['G', 'C', 'A', 'E']
"""
