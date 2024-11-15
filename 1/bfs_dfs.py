from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'D'],
    'D': ['B', 'E', 'C'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    if start not in graph and goal not in graph:
        return []
    
    visited = set()

    q = deque([start])
    result = []
    while q:
        node = q.popleft()
        
        if node == goal:
            return result + [node]
        if node not in visited:
            visited.add(node)
            result.append(node)

            q.extend(n for n in graph[node] if n not in visited)
    return result

print(bfs(graph,'A','F'))

def dfs(graph, start, goal, visited = None):
    if visited is None:
        visited = set()
    if start not in graph and goal not in graph:
        return []
    visited.add(start)
    result = [start]

    if start == goal:
        return result
    for n in graph[start]:
        if n not in visited:
            path = dfs(graph,n,goal,visited)

            if path:
                result.extend(path)
                return result
    return result


print(dfs(graph,'A','F'))