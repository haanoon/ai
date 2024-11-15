import math


class TreeNode:
    def __init__(self,name,value = None):
        self.name = name
        self.value = value
        self.children = []

        def add_child(self,child):
            self.children.append(child) 


def minmax(node, depth, minORmax, path):
    if depth  == 0 or not node.children:
        return node.value if node.value else 0 ,path
    
    if minORmax:
        best_value = -math.inf
        best_path = None
        for child in node.children:
            value, currentpath = minmax(child,depth-1,False,path+[child.name])
            if value>best_value:
                best_value = value
                best_path = currentpath
        return best_value,best_path
    else:
        best_value = math.inf
        best_path = None
        for child in node.children:
            value, currentpath = minmax(child,depth-1,True,path+[child.name])
            if value<best_value:
                best_value = value
                best_path = currentpath
        return best_value,best_path
def alpha_beta(node, depth, alpha, beta, minORmax, visitednodes, path):
    if depth == 0 or not node.children:
        return node.value if node.value else 0, path
    
    if minORmax:
        best_value = -math.inf
        best_path = None
        visitednodes.add(node.name)
        for child in node.children:
            value, currentpath = alpha_beta(child,depth-1,alpha,beta,False,visitednodes,path+[child.name])
            if best_value<value:
                best_value = value
                best_path = currentpath
            alpha = max(alpha,value)
            if alpha>= beta:
                break
        return value, best_path
    else:
        best_value = math.inf
        best_path = None
        visitednodes.add(node.name)
        for child in node.children:
            value, currentpath = alpha_beta(child,depth-1,alpha,beta,True,visitednodes,path+[child.name])
            if best_value > value:
                best_value = value
                best_path = currentpath
            alpha = min(beta,value)
            if alpha>= beta:
                break
        return value, best_path
    

import math

# Example Tree Setup
root = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D", 3)     # Leaf node with value 3
E = TreeNode("E", 5)     # Leaf node with value 5
F = TreeNode("F", 2)     # Leaf node with value 2
G = TreeNode("G", 9)     # Leaf node with value 9
H = TreeNode("H", -6)    # Leaf node with value -6
I = TreeNode("I", -8)    # Leaf node with value -8
J = TreeNode("J", 4)     # Leaf node with value 4

# Constructing the tree
root.children.extend([B, C])
B.children.extend([D, E, F])
C.children.extend([G, H, I, J])

# Test Minimax Function
minmax_value, minmax_path = minmax(root, depth=3, minORmax=True, path=[root.name])
print("Minimax Result:", minmax_value, "Path:", minmax_path)

# Test Alpha-Beta Pruning Function
visited_nodes = set()
alpha_beta_value, alpha_beta_path = alpha_beta(root, depth=3, alpha=-math.inf, beta=math.inf, minORmax=True, visitednodes=visited_nodes, path=[root.name])
print("Alpha-Beta Result:", alpha_beta_value, "Path:", alpha_beta_path)
print("Visited Nodes (Alpha-Beta):", visited_nodes)
