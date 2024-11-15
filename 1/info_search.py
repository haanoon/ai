import heapq

graph = {
    'arad': {'zerind': 75, 'timisora': 118, 'sibiu': 140},
    'zerind': {'arad': 75, 'oradea': 71},
    'timisora': {'arad': 118, 'lugoj': 111},
    'sibiu': {'arad': 140, 'oradea': 151, 'fagaras': 99, 'rimicu': 80},
    'fagaras': {'sibiu': 99, 'bucharest': 211},
    'bucharest': {'fagaras': 211, 'pitesti': 101},
    'pitesti': {'bucharest': 101, 'rimicu': 97},
    'oradea': {'zerind': 71, 'sibiu': 151},
    'dabaeu': {'rimicu': 80},
    'lugoj': {'timisora': 111},
    'rimicu': {'sibiu': 80, 'pitesti': 97, 'dabaeu': 80}
}

heuristic = {
    'arad': 366, 'zerind': 374, 'timisora': 329, 'sibiu': 253,
    'fagaras': 176, 'bucharest': 0, 'pitesti': 100, 'oradea': 380,
    'dabaeu': 256, 'lugoj': 244, 'rimicu': 193
}

start = 'arad'
goal = 'bucharest'

def bestfirst(graph,heuristic,start,goal):
    li = []
    heapq.heappush(li,(heuristic[start],start))
    visited = set()
    previous_node = {start:None}

    while li:
        _, currentnode = heapq.heappop(li)

        if currentnode in visited:
            continue

        visited.add(currentnode)
        if currentnode == goal:
            break
        for n in graph[currentnode]:
            if n not in visited:
                heapq.heappush(li,(heuristic[n],n))
                previous_node[n] = currentnode
    path = []
    while currentnode:
        path.append(currentnode)
        currentnode = previous_node[currentnode]

    path.reverse()
    print(path)

    pathcost= 0
    for i in range(len(path) - 1):
        pathcost += graph[path[i]][path[i+1]]
    print(pathcost)

bestfirst(graph, heuristic, start, goal)

def astar(graph, heuristic, start, goal):
    li = []
    heapq.heappush(li,(0,start))

    came_from = {start:None}
    g_cost = {start:0}

    while li:
        _,currentnode = heapq.heappop(li)

        if currentnode == goal:
            break
        for n, cost in graph[currentnode].items():
            t_cost = g_cost[currentnode] + cost
            if n not in g_cost or t_cost<g_cost[n]:
                g_cost[n] = t_cost
                f_cost = t_cost + heuristic[n]
                heapq.heappush(li,(f_cost,n))
                came_from[n] = currentnode
    path = []
    while currentnode:
        path.append(currentnode)
        currentnode = came_from[currentnode]

    print(path)

    print(g_cost[goal])

astar(graph, heuristic, start, goal)