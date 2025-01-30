import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heapq

def create_grid(rows, cols, obstacles):
    """Creates the grid with given rows, cols, and obstacle positions."""
    grid = np.zeros((rows, cols), dtype=int)
    for obs in obstacles:
        grid[obs] = 1  # Set obstacles as '1' in the grid
    return grid

def get_user_input():
    """Prompt user for grid size, obstacles, start and destination points."""
    rows = int(input("Enter grid rows: "))
    cols = int(input("Enter grid columns: "))
    num_obstacles = int(input("Enter the number of obstacles: "))
    
    obstacles = []
    for _ in range(num_obstacles):
        r, c = map(int, input("Enter obstacle position (row col): ").split())
        obstacles.append((r, c))
    
    start = tuple(map(int, input("Enter starting point (row col): ").split()))
    destination = tuple(map(int, input("Enter destination point (row col): ").split()))
    
    return rows, cols, obstacles, start, destination

def heuristic(a, b):
    """Calculates Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_algorithm(grid, start, destination):
    """Implements the A* pathfinding algorithm."""
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {point: float('inf') for point in np.ndindex(grid.shape)}
    g_score[start] = 0
    f_score = {point: float('inf') for point in np.ndindex(grid.shape)}
    f_score[start] = heuristic(start, destination)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == destination:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor] == 1:
                    continue  # Ignore obstacles
                tentative_g_score = g_score[current] + 1
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, destination)
                    if (f_score[neighbor], neighbor) not in open_set:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

def visualize_path(grid, path, start, destination, obstacles):
    """Visualizes the grid, showing obstacles, path, start, and destination."""
    plt.imshow(grid, cmap="gray")
    for (r, c) in obstacles:
        plt.gca().add_patch(plt.Rectangle((c, r), 1, 1, color='black'))
    
    for (r, c) in path:
        plt.gca().add_patch(plt.Circle((c, r), 0.3, color='red'))
    
    plt.gca().add_patch(plt.Circle((start[1], start[0]), 0.3, color='green', label='Start'))
    plt.gca().add_patch(plt.Circle((destination[1], destination[0]), 0.3, color='blue', label='Destination'))
    
    plt.legend(loc="upper right")
    plt.title("Grid with Path")
    plt.gca().invert_yaxis()
    plt.show()

def main():
    """Main function to run the robot navigation application."""
    while True:
        rows, cols, obstacles, start, destination = get_user_input()
        grid = create_grid(rows, cols, obstacles)
        
        # Show initial grid as a DataFrame for clarity
        print("\nInitial Grid Layout:")
        print(pd.DataFrame(grid))
        
        # Run A* algorithm
        path = a_star_algorithm(grid, start, destination)
        
        if path:
            print("\nPath found!")
            visualize_path(grid, path, start, destination, obstacles)
        else:
            print("No valid path found.")
        
        retry = input("Would you like to try again with different inputs? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting the application. Goodbye!")
            break

# Run the application
main()
