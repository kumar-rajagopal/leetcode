import collections
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


def bfs_shortest_path(graph, start, goal):
    visited = {}
    #queue = [[start]]
    queue = collections.deque([start])
    while(queue):
        path = queue.popleft()
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

print(bfs_shortest_path(graph, 'G', 'D')) #['G', 'C', 'A', 'B', 'D']



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
    queue = collections.deque([start])
    #queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        #node = queue.pop(0)
        node = queue.popleft()
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
                
    return explored
 
print(bfs_connected_component(graph,'G')) # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']

"""
Tip: To make the code more efficient, you can use the deque object from the collections module instead of a list,
for implementing queue. This way you can use the popleft() method instead of the  pop(0) built-in function on queue. 
This will result in a quicker code as popleft()has a time complexity of O(1) while pop(0) has O(n).

The good and the bad of BFS
There’s a great news about BFS: it’s complete. That’s because this algorithm is always able to find a solution to a problem, if there is one. For example, if a path exists that connects two nodes in a graph, BFS will always be capable of identifying it – given the search space is finite.

Completeness is a nice-to-have feature for an algorithm, but in case of BFS it comes to a high cost. The execution time of BFS is fairly slow, because the time complexity of the algorithm is exponential. What’s worse is the memory requirements. That’s because BFS has to keep track of all of the nodes it explores. In the case of problems which translate into huge graphs, the high memory requirements make the use of BFS unfeasible. For example, to solve the Rubik’s Cube with BFS we need c. 10 zettabytes (1021 bytes)of RAM, which, the last time I checked, is not yet available on our laptops!

Lesson learned: You should use BFS only for relatively small problems.

What can you use BFS for?
Even though BFS is not the best option for problems involving large graphs, it can be  successfully employed for a number of applications. I’ll list just a few of them to give you an idea:

Shortest path of unweighted graphs (we did this already – hooray!).
Discover all nodes reachable from an initial vertex (we did this too!)
Find neighbour nodes in peer to peer networks like BitTorrent.
Used by crawlers in search engines to visit links on a webpage, and keep doing the same recursively.
Find people at a given distance from a person in social networks.
Identify all neighbour locations in GPS systems.
Search whether there’s a path between two nodes of a graph (path finding).
Allow broadcasted packets to reach all nodes of a network.
Conclusion
Breadth-first search is an algorithm used to traverse and search a graph. If you’ve followed the tutorial all the way down here, you should now be able to develop a Python implementation of BFS for traversing a connected component and for finding the shortest path between two nodes.

There are a few takeway messages I’d like you to remember from this tutorial:

Graphs are the data structure of election to search for solutions in complex problems.
BFS explores nodes one depth level at a time. It starts from a node, then checks the neighbours of the initial node, then the neighbours of the neighbours and so on…
BFS is complete, in that it always returns a solution in case there is one.
BFS is often impracticable in large real-world problems, because of excessive memory requirements.
"""

