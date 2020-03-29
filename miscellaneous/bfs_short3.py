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
				if n == goal:
					return new_path
			visited[node] = 1

print(bfs_shortest_path(graph, 'E', 'F')) #['E', 'A', 'C', 'F']
"""
q:  [['E']]
path  ['E']
node:  E
visit  {}
GNODE  ['A', 'B', 'D']
node val  A 
np  ['E']
q inside:  [['E', 'A']]
node val  B
np  ['E']
q inside:  [['E', 'A'], ['E', 'B']]
node val  D
np  ['E']
q inside:  [['E', 'A'], ['E', 'B'], ['E', 'D']]
q:  [['E', 'A'], ['E', 'B'], ['E', 'D']]


path  ['E', 'A']
node:  A
visit  {'E': 1}
GNODE  ['B', 'C', 'E']
node val  B
np  ['E', 'A']
q inside:  [['E', 'B'], ['E', 'D'], ['E', 'A', 'B']]
node val  C
np  ['E', 'A']
q inside:  [['E', 'B'], ['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C']]
node val  E
np  ['E', 'A']
q inside:  [['E', 'B'], ['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E']]
q:  [['E', 'B'], ['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E']]



path  ['E', 'B']
node:  B
visit  {'E': 1, 'A': 1}
GNODE  ['A', 'D', 'E']
node val  A
np  ['E', 'B']
q inside:  [['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A']]
node val  D
np  ['E', 'B']
q inside:  [['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D']]
node val  E
np  ['E', 'B']
q inside:  [['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E']]
q:  [['E', 'D'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E']]



path  ['E', 'D']
node:  D
visit  {'E': 1, 'A': 1, 'B': 1}
GNODE  ['B']
node val  B
np  ['E', 'D']
q inside:  [['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E'], ['E', 'D', 'B']]
q:  [['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E'], ['E', 'D', 'B']]
path  ['E', 'A', 'B']
node:  B
visit  {'E': 1, 'A': 1, 'B': 1, 'D': 1}
q:  [['E', 'A', 'C'], ['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E'], ['E', 'D', 'B']]
path  ['E', 'A', 'C']
node:  C
visit  {'E': 1, 'A': 1, 'B': 1, 'D': 1}
GNODE  ['A', 'F', 'G']
node val  A
np  ['E', 'A', 'C']
q inside:  [['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E'], ['E', 'D', 'B'], ['E', 'A', 'C', 'A']]
node val  F
np  ['E', 'A', 'C']
q inside:  [['E', 'A', 'E'], ['E', 'B', 'A'], ['E', 'B', 'D'], ['E', 'B', 'E'], ['E', 'D', 'B'], ['E', 'A', 'C', 'A'], ['E', 'A', 'C', 'F']]
['E', 'A', 'C', 'F']
"""