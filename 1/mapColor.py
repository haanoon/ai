def isSafe(graph, node, color, colorsGiven, names):
    for neighbor in graph[node]:
        if colorsGiven[neighbor] == color:
            return False
    return True

    

def graphColoring(graph,colors,colorsGiven,node, name):
    if node == len(graph):
        return True
    available_colors = [color for color in colors if color not in [colorsGiven[n] for n in graph[node]]]
    for color in available_colors:
        if isSafe(graph, node, color, colorsGiven, name):
            colorsGiven[node] = color

            if graphColoring(graph, colors, colorsGiven, node+1, name):
                return True
            
            colorsGiven[node] = None

    return False


