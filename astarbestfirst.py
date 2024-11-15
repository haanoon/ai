import heapq


def besstf(graph,heuristic,start , goal):
    li = []
    heapq.heappush(li,(heuristic[start],start))
    visited = set()
    previous_node = {start:None}

    while li:
        _, currentNode = heapq.heappop(li)
        if currentNode in visited:
            continue
        visited.add(currentNode)

        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                heapq.heappush(li,(heuristic[neighbor],neighbor))
                previous_node[neighbor] = currentNode

        
    path = []
    while currentNode:
        path.append(currentNode)
        currentNode = previous_node[currentNode]
    path.reverse()

    path_cost = 0
    for  i in range(len(path) - 1):
        path_cost += graph[path[i]][path[i+1]]
    return path, path_cost

def astar(graph, start, goal, heuristic):
    li = []
    heapq.heappush(li,(heuristic[start],start))
    came_from = {start:None}
    g_costs = {start:0}

    while li:
        _, currentNode = heapq.heappop(li)
        if currentNode == goal:
            break

        for node, cost in graph[currentNode].items():
            t_cost = g_costs[currentNode] + cost
            if node not in g_costs or g_costs[node]>t_cost:
                g_costs[node] = t_cost
                f_cost = t_cost + heuristic[node]
                heapq.heappush(li,(f_cost,node))
                came_from[node] = currentNode

    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    pathcost = g_costs[goal]
    return path, pathcost

nodes = input('enter nodes: ').split()
graph = {}
for node in nodes:
    graph[node] = {}
    neighbors = input(f'enter neighbors of {node}').split()
    for neighbor in neighbors:
        if neighbor not in graph.keys():
            graph[neighbor]={}
        distance = int(input(f'enter distance between {node} and {neighbor}'))
        graph[node][neighbor] = distance
        graph[neighbor][node] = distance

print(graph)

heuristic = {}
for node in graph.keys():
    h = int(input(f'heuristc of {node}'))
    heuristic[node] = h
print(heuristic)

bpath, bpathcost = besstf(graph,heuristic,'a','e')

print(bpath,bpathcost)

print()

apath,acost = astar(graph,'a','e',heuristic)

print(apath,acost)

