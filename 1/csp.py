import random


def getNeighbors(state,graph):
    neighbors = []
    for node in graph.keys():
        for color in colors:
            if state[node] != color:
                neighbor = state.copy()
                neighbor[node] = color
                neighbors.append(neighbor)
    return neighbors

def countConflicts(state, graph):
    conflicts = 0
    for node in graph:
        for neighbor in graph[node]:
            if state[node] == state[neighbor]:
                conflicts += 1
    return conflicts
def hillclimbing(graph, colors, max_iters = 100):
    current_state = {node: random.choice(colors) for node in graph}
    print(current_state)

    cur_conflicts = countConflicts(current_state,graph)

    for i in range(max_iters):
        neighbors = getNeighbors(current_state,graph)
        neighbor_conflicts = [(neighbor,countConflicts(neighbor,graph)) for neighbor in neighbors]
        best_neighbor,best_conflicts = min(neighbor_conflicts,key=lambda x:x[1])

        if best_conflicts<cur_conflicts:
            current_state = best_neighbor
            cur_conflicts = best_conflicts
            print(current_state)
        else:
            break
    return current_state
n = 4
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']

# Run hill climbing with hardcoded data
final_state = hillclimbing(graph, colors)
print("Final state:")
print(final_state)