n = 4
city_names = ['a','b','c','d']
graph = []
for i in range(n):
    dis = list(input(f'Enter the distance from {city_names[i]}').split())
    graph.append(dis)

start = 'a'


from itertools import permutations

def totalDistance(path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]
    return distance

def travelling(graph,city_names,start):
    cities = list(range(len(city_names)))
    cities.remove(city_names.index(start))
    min_path = None
    min_distance = float('inf')
    for perm in permutations(cities):
        current_path = [start] + perm
        distance = totalDistance(current_path)

        if distance<min_distance:
            min_distance = distance
            min_path = current_path
    min_path.append(start)
    
