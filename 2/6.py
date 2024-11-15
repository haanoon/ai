class TreeNode:
    def __init__(self,name,value = None):
        self.name = name
        self.value = value
        self.children = []
    def add_child(self,child):
        self.children.append(child)


def alphaBeta(node,depth,alpha,beta,ismax,visited,path):
    if depth == 0 or not node.children:
        return node.value, path
    if ismax:
        best_value = float('-inf')
        best_path = None
        for child in node.children:
            visited.add(node.name)
            value, bpath = alphaBeta(child,depth-1,alpha,beta,False,visited,path+[child.name])
            if best_value<value:
                best_path = bpath
                best_value = value
            alpha = max(alpha,best_value)
            if alpha>= beta:
                break
        return best_value,best_path
    else:
        best_value = float('inf')
        best_path = None
        for child in node.children:
            visited.add(node.name)
            value,bpath = alphaBeta(child,depth-1,alpha,beta,True,visited,path+[child.name])
            if best_value<value:
                best_value = value
                best_path = bpath
            beta = min(beta,best_value)
            if alpha>=beta:
                break
        return best_value,best_path5