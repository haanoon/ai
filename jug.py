from collections import deque

def bfs(start, goal, a_cap, b_cap):
    queue = deque([(start, [])])  # Queue stores state and path to that state
    visited = set()

    while queue:
        (a, b), path = queue.popleft()
        
        # If we reach the goal state, return the path leading to the goal
        if (a, b) == goal:
            return path + [(a, b)]
        
        # Mark the current state as visited
        visited.add((a, b))
        
        # Possible next states from the current state (a, b)
        next_states = [
            (a_cap, b),                           # Fill jug A
            (a, b_cap),                           # Fill jug B
            (0, b),                               # Empty jug A
            (a, 0),                               # Empty jug B
            (a - min(a, b_cap - b), b + min(a, b_cap - b)),  # Pour A to B
            (a + min(b, a_cap - a), b - min(b, a_cap - a))   # Pour B to A
        ]
        
        # Enqueue each valid and unvisited state
        for state in next_states:
            if state not in visited:
                queue.append((state, path + [(a, b)]))  # Add new state and path
        print(visited)
    # Return empty list if goal is unreachable
    return []

# Test the function
result = bfs((0, 0), (4, 0), 5, 3)
print("Path to goal:", result)