
def isSafe(graph,node,color,colorsgiven):
    for n in graph[node]:
        if colorsgiven[node] == color:
            return False
    return True

        

def graphColoring(graph,colors,colorgiven,node):
    if node == len(graph):
        return True
    colors_available = [color for color in colors if color not in [colorgiven[n] for n in graph[node]]]
    for color in colors_available:
        if isSafe(graph,node,color,colorgiven):
            colorgiven[node] = color
            if graphColoring(graph,colors,colorgiven,node+1):
                return True
            
    return False
n = 4
m = 5
names = ['a','b','c','d']
graph = {i:[] for i in range(n)}

for _ in range(m):
    u_name,v_name = input().split(' ')
    u = names.index(u_name)
    v = names.index(v_name)
    graph[u].append(v)
    graph[v].append(u)

colors = input('coloes').split()
colors_given = [None]*n

graphColoring(graph, colors,colors_given,0)

print(colors_given)
