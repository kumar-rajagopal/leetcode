graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


def bfs_shortest_path(graph, start, goal):
	visited = {}
	queue = [[start]]
	while(queue):
		path = queue.pop(0)
		node = path[-1]
		if node not in visited:
			for n in graph[node]:
				new_path = list(path)
				new_path.append(n)
				queue.append(new_path)
				if goal == n:
					return new_path
			visited[node] = 1

	return -1

print(bfs_shortest_path(graph, 'G', 'Z')) #['G', 'C', 'A', 'B', 'D']

def bfs_short(graph, start, goal):
	q = [[start]]
	visited = {}
	while q:
		node = q.pop(0)
		path = node[1]
		if node not in visited:
			visited[node] = 1
			for n in graph[node]:
				new_path = list(path)
				new_path.append(path)
				q.append(new_path)


# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
bfs_connected_component(graph,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']


