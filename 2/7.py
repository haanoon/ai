n = 4
m = 5
names = ['a','b','c','d']

graph = {i:[] for i in range(n)}
print('enter edges')
for i in range(m):
    u_name,v_name = input().split()
    u = names.index(u_name)
    v = names.index(v_name)
    graph[v].append(u)
    graph[u].append(v)
print(graph)
# colors = input("Enter Colors").split()
colors = ['r','g','b']
colors_given = [None] * n


def isSafe(graph,node,color,colors,colors_given):
    
    for neighbor in graph[node]:
        if colors_given[node] == colors_given[neighbor]:
        
            return False
    return True


def graphColoring(graph,colors,colors_given,node):
    if node == len(graph):
        
        return True
    colors_available = [color for color in colors if color not in [colors_given[node]for node in graph]]
    print(colors_available)
    for color in colors:
        colors_given[node] = color
        if isSafe(graph,node,color,colors,colors_given):
            
            if graphColoring(graph,colors,colors_given,node+1):
                return True
            colors_given[node] = None

    return False

if graphColoring(graph,colors,colors_given,0):
    print('last')
    print(colors_given)
else:
    print('unsolvable')