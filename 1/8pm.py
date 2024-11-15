import heapq

# Defining the goal state
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Defining the directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to find the position of 0 in the state
def find_zero(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

# Function to calculate the Manhattan distance (heuristic) using divmod
def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                target_r, target_c = divmod(value - 1, 3)  # divmod gives quotient (row) and remainder (column)
                distance += abs(target_r - r) + abs(target_c - c)
    return distance

# Function to get valid neighbors of a state
def get_neighbors(state):
    neighbors = []
    zero_r, zero_c = find_zero(state)
    
    for dr, dc in directions:
        new_r, new_c = zero_r + dr, zero_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = list(list(row) for row in state)  # Create a mutable copy
            new_state[zero_r][zero_c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[zero_r][zero_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    
    return neighbors

# Best-First Search (Greedy) algorithm
def best_first_search(start):
    # Priority queue (heap) for the open list (we prioritize by the heuristic)
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start), start))
    
    # Set to keep track of visited states
    visited = set()
    visited.add(start)
    
    # Dictionary to reconstruct the path
    came_from = {}
    
    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state == goal_state:
            # Reconstruct the path
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = came_from.get(current_state)
            return path[::-1]  # Reverse the path
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(open_list, (manhattan_distance(neighbor), neighbor))
                came_from[neighbor] = current_state
    
    return None  # If no solution is found

# Example starting state
start_state = ((2, 8, 3), (1, 6, 4), (7, 0, 5))

# Run the Best-First Search algorithm
solution_path = best_first_search(start_state)

# Print the solution path
if solution_path:
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found!")