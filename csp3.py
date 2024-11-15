import random


nodes = input('Enter Nodes Names').split()
graph = {}
for node in nodes:
    neighbours = input(f'Name of neighbors of node {node}').split()
    graph[node] = neighbours
colors = input("Colors Available: ").split()


def countConflicts(state ,graph):
    count = 0
    for node in graph:
        for neighbor in graph[node]:
            if state[node] == state[neighbor]:
                count += 1
    return count

def getNeighbors(state, graph):
    neighbours = []
    for node in graph.keys():
        for color in colors:
            if state[node] != color:
                neighbour = state.copy()
                neighbour[node] = color
                neighbours.append(neighbour)
    return neighbours





def hillClimbing(graph,colors,max_iters= 1000):
    current_state = {node:random.choice(colors) for node in graph}
    current_conflict = countConflicts(current_state)

    for i in range(max_iters):
        neighbours = getNeighbors(current_state,graph)
        neighbour_conflict = [(neighbour,countConflicts(neighbour))for neighbour in neighbours]
        best_neighbour,best_conflicts = min(neighbour_conflict,key=lambda x:x[1])
        if best_conflicts<current_conflict:
            current_state = best_neighbour
            current_conflict = best_conflicts
            print(f"Iteration {i+1}:")
            print(f"Current state: {current_state}")
            print(f"Conflicts: {current_conflict}\n")
        else:
            break
    return current_state, current_conflict
    

final_state, final_conflicts = hillClimbing(graph, colors)
print("Final state:")
print(final_state)
print(f"Final conflicts: {final_conflicts}")
