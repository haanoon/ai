from collections import deque


def readGraph():
    graph = {}
    n = int(input('Enter number of nodes'))
    e = int(input('enter nnumber of edges'))

    nodes = input("enter nodes").split()
    print(nodes)
    for node in nodes:
        graph[node] = []
        graph[node].extend(input(f'nodes of {node}').split())
    for node in graph:
        for c_node in graph[node]:
            if node not in graph[c_node]:
                graph[c_node].append(node)
    
    return graph

graph =  readGraph()

def bfs(graph,start,goal):
    if start not in graph and goal not in graph:
        return []
    q = deque([start])
    visited = set()
    result = []
    while q:
        vertex = q.popleft()
        if vertex == goal:
            result.append(vertex)
            return result
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            q.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return result
# def dfs(graph,start,goal, visited = None):
#     if visited == None:
#         visited = set()
#     if start not in graph and goal not in graph:
#         return []
#     visited.add(start)
#     result = [start]
#     if start == goal:
#         return result
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             path = dfs(graph,neighbor,goal,visited)
#             if goal in graph:
#                 result.extend(path)
#                 return result
#     return result
def dfs(graph,start,goal,visited = None):
    if visited is None:
        visited = set()
    if start not in graph or goal not in graph:
        return[]
    visited.add(start)
    result = [start]

    if start == goal:
        return result
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph,neighbor,goal,visited)
            if goal in path:
                result.extend(path)
                return result
    return result
start = input('start:  ')
goal = input('goal: ')

print(bfs(graph,start,goal))
print(dfs(graph,start,goal))