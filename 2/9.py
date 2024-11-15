import random


def countConflicts(state,graph):
    count = 0
    for node in graph:
        for neighbor in graph[node]:
            if state[node] == state[neighbor]:
                count += 1
    return count

def getNeighbors(state, graph):
    neighbors = []
    for node in graph.keys():
        for color in colors:
            if state[node] != color:
                neighbor = state.copy()
                neighbor[node] = color
                neighbors.append(neighbor)
    return neighbors

def hillClimbing(graph,colors,maxi):

    current_state = {node:random.choice(colors) for node in graph}
    current_conflicts = countConflicts(current_state)

    for i in range(maxi):
        neighbors = getNeighbors(current_state)
        neighbor_conflicts = [(neighbor,countConflicts(neighbor))for neighbor in neighbors]
        best_neighbor, best_conflicts = min(neighbor_conflicts,key= lambda x:x[1])
        if best_conflicts<current_conflicts:
            current_conflicts = best_conflicts
            current_state = best_neighbor
        else:
            break
    return current_state,current_conflicts
