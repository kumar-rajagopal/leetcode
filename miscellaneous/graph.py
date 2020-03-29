"""
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    #print(graph, type(graph))
    if start not in graph:
        return None
    for node in graph[start]:
        print('N ',node)
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                print(newpath)
                return newpath
    return None


def find_shortest_path(graph, start, end, path=[]):
    print('st ',start)
    path = path + [start]
    #print(path, "s: ",start, "e: ",end)
    if start == end:
        print("PA: ",path, "s: ",start, "e: ",end)
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            print('recurse ',node)
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    print("short: ",shortest)
    return shortest

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
r =find_shortest_path(graph, 'A', 'D')
print('res ',r)
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

r = list(dfs_paths(graph, 'A', 'F'))
print(r)