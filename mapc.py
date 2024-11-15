def main():
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))
    names = []
    for i in range(n):
        name = input(f"Enter the name of node {i + 1}: ")
        names.append(name)
    graph = {i: [] for i in range(n)}    
    print("\nEnter the edges pairwise by node names:")
    for _ in range(m):
        u_name, v_name = input().split()
        u = names.index(u_name)
        v = names.index(v_name)
        graph[u].append(v)
        graph[v].append(u)    
    colors = input("\nEnter the available colors (separated by spaces): ").split()
    colors_given = [None] * n    
    if graphColoring(graph, colors, colors_given, 0):
        print("\nNode and corresponding colors are:")
        for i in range(n):
            print(f"Node {names[i]} ---> {colors_given[i]}")
    else:
        print("No solution exists")

def graphColoring(graph, colors, colorsGiven, node):
    if node == len(graph):
        return True
    for color in colors:
        if isSafe(graph,node,color,colorsGiven):
            colorsGiven[node] = color
            if graphColoring(graph,colors,colorsGiven,node+1,):
                return True
            colorsGiven[node] = None
    return False


def isSafe(graph, node, color, colorsgiven):
    for neighbor in graph[node]:
        if colorsgiven[neighbor] == color:
            return False
    return True
main()