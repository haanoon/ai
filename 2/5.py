import numpy as np

def isSolvable(puzzle,goal):
    flat_puzzle = [ j for i in puzzle for j in i]
    flat_goal = [ j for i in goal for j in i]

    inv_count = getInvCount(flat_puzzle,flat_goal)
    return (inv_count%2 == 0)
    

def getInvCount(puzzle,goal):
    goal_index = {value:idx for idx,value in enumerate(goal)}
    mapped = [goal_index[value] for value in puzzle if value != 0]
    count = 0
    for i in range(len(mapped)):
        for j in range(i,len(mapped)):
            if mapped[i]>mapped[j]:
                count += 1
    return count

def getblankPosition(state):
    for i in range(len(state)):
        if 0 in state[i]:
            return (i,state[i].index(0))


    
# def up(row,col,state):
#     global frontier
#     state[row][col] = state[row-1][col]
#     state[row-1][col] = 0
#     if not any([np.array_equal(state,j)for j in explored]):
#         frontier.append(state)

# def down(row,col,state):
#     global frontier
#     state[row][col] = state[row+1][col]
#     state[row+1][col] = 0
#     if not any([np.array_equal(state,j)for j in explored]):
#         frontier.append(state)

# def left(row,col,state):
#     global frontier
#     state[row][col] = state[row][col-1]
#     state[row][col-1] = 0
#     if not any([np.array_equal(state,j)for j in explored]):
#         frontier.append(state)

# def right(row,col,state):
#     global frontier
#     state[row][col] = state[row][col+1]
#     state[row][col+1] = 0
#     if not any([np.array_equal(state,j)for j in explored]):
#         frontier.append(state) 
# 
def up(row, col, state):
    global frontier
    new_state = np.copy(state)  # FIX: Deep copy of the state to avoid unintended side effects
    new_state[row][col] = new_state[row - 1][col]
    new_state[row - 1][col] = 0
    if not any(np.array_equal(new_state, j) for j in explored):
        frontier.append(new_state)

def down(row, col, state):
    global frontier
    new_state = np.copy(state)  # FIX: Deep copy of the state
    new_state[row][col] = new_state[row + 1][col]
    new_state[row + 1][col] = 0
    if not any(np.array_equal(new_state, j) for j in explored):
        frontier.append(new_state)

def left(row, col, state):
    global frontier
    new_state = np.copy(state)  # FIX: Deep copy of the state
    new_state[row][col] = new_state[row][col - 1]
    new_state[row][col - 1] = 0
    if not any(np.array_equal(new_state, j) for j in explored):
        frontier.append(new_state)

def right(row, col, state):
    global frontier
    new_state = np.copy(state)  # FIX: Deep copy of the state
    new_state[row][col] = new_state[row][col + 1]
    new_state[row][col + 1] = 0
    if not any(np.array_equal(new_state, j) for j in explored):
        frontier.append(new_state)
  
frontier = []
def possibleStates(state):
    row , col = getblankPosition(state.tolist())
    if row>=0 and row <2:
        down(row,col,state.copy())
    if row<=2 and row>0:
        up(row,col,state.copy())
    if col>=0 and col < 2:
        right(row,col,state.copy())
    if col<=2 and col>0:
        left(row,col,state.copy())
    frontier.sort(key=lambda x:heuristic(x))

def heuristic(state):
    h = np.sum(np.array(state) != goal)
    print(state,h)
    return h

initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
a= np.array(initial_state)
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
goal = np.array(goal_state)
temp = a.copy()
v = temp
explored = [temp]

possibleStates(v)
if isSolvable(temp,goal):
    while heuristic(v) != 0:
        v = frontier.pop(0)
        print(v)
        explored.append(v)
        possibleStates(v)
else:
    print('unsolvable')
