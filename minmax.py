class TreeNode:
    def __init__(self,name,value = None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self,child):
        self.children.append(child)


def alphaBeta(node, depth, alpha, beta, visited, ismax, path):
    if depth == 0 or not node.children:
        return node.value , path
    
    if ismax:
        best_value = float('-inf')
        best_path = None
        for child in node.children:
            visited.add(node.name)
            current_value,current_path = alphaBeta(child,depth - 1,alpha,beta,visited,False,path+[child.name])
            if current_value > best_value:
                best_value = current_value
                best_path = current_path
            alpha = max(alpha,best_value)
            if beta<=alpha:
                break
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = None
        for child in node.children:
            visited.add(node.name)
            current_value, current_path = alphaBeta(child,depth - 1, alpha, beta,visited,True,path+[child.name])
            if current_value < best_value:
                best_value = current_value
                best_path = current_path
            beta = min(beta,best_value)
            if beta <= alpha:
                break
        return best_value, best_path
    


# def minmax(node,depth,ismax,path):
#     if depth == 0 or not node.children:
#         return node.value , path
#     if ismax:









root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D", 3)
e = TreeNode("E", 5)
f = TreeNode("F", 6)
g = TreeNode("G", 9)
h = TreeNode("H", 1)
i = TreeNode("I", 2)
j = TreeNode("J", 0)

# Build the tree
root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)
c.add_child(h)
c.add_child(i)
i.add_child(j)

# Set up parameters for alpha-beta pruning
depth = 3
alpha = float('-inf')
beta = float('inf')
visited = set()
ismax = True
path = [root.name]

# Run the alphaBeta function and print the result
best_value, best_path = alphaBeta(root, depth, alpha, beta, visited, ismax, path)
print("Best Value:", best_value)
print("Best Path:", best_path)