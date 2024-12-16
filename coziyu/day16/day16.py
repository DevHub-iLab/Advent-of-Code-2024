import aocd
input = aocd.get_data(day=16, year=2024)

maze = input.strip().split("\n")

E = (0, 1)
N = (-1, 0)
W = (0, -1)
S = (1, 0)

def parse(maze):
    start = end = None
    
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    
    return maze, start, end

def rotate_direction(dir, right_turn):
    dirs = [E, S, W, N]
    ind = dirs.index(dir)
    if right_turn:
        return dirs[(ind + 1) % 4]
    return dirs[(ind - 1) % 4]

def is_valid(grid, pos):
    rows, cols = len(grid), len(grid[0])
    row, col = pos
    return (0 <= row < rows and 
            0 <= col < cols and 
            grid[row][col] != '#')

from collections import defaultdict
import heapq
def dijkstra(grid, start, end):
    # PQ - score, (pos, dir), visited_pos
    start_state = (start, E)
    queue = [(0, start_state, [start])]
    
    # Track minimum scores for each state
    visited = defaultdict(lambda: float('inf'))
    visited[start_state] = 0
    
    best_score = float('inf')
    paths = []
    
    while queue:
        score, state, path_pos = heapq.heappop(queue)
        pos, dir = state
        
        if score > best_score:
            break

        if pos == end:
            if score <= best_score:
                if score < best_score:
                    paths = []
                    best_score = score
                paths.append(path_pos)
            continue
            
        # Try forward
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if is_valid(grid, new_pos):
            new_state = (new_pos, dir)
            new_score = score + 1
            if new_score <= visited[new_state]:
                visited[new_state] = new_score
                new_pos = path_pos + [new_pos] 
                heapq.heappush(queue, (new_score, new_state, new_pos))
        
        # Try rotate
        for right_turn in [True, False]:
            new_dir = rotate_direction(dir, right_turn)
            new_state = (pos, new_dir)
            new_score = score + 1000
            if new_score <= visited[new_state]:
                visited[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state, path_pos))
    
    return best_score, paths


### Part 1 - Dijkstra with score as criterion
grid, start, end = parse(maze)
score, paths = dijkstra(grid, start, end)
print(score)

### Part 2 - we need all the best paths!
unique_paths = set()
for path in paths:
    for pos in path:
        unique_paths.add(pos)
print(len(unique_paths))