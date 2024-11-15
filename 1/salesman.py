from itertools import permutations

def totalDistance(graph, path):
    totalDist = 0
    for i in range(len(path) - 1):
        d

def travellingSalesman(graph, start, citynames):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_path = None
    min_distance = float('inf')

    for prem in permutations(cities):
        current_path = [start] + list(perm)
        current_distace = totalDistance(graph,current_path)
        if current_distace<min_distance:
            min_distance = current_distace
            min_path = current_path
        min_path.append(start)
    return min_path
