def find_root(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                return i, j
    return None

def is_valid_move(maze, x, y, visited):
    return (0 <= x < len(maze) and 
            0 <= y < len(maze[0]) and 
            maze[x][y] in [1, 3] and 
            (x, y) not in visited)

def dfs_maze(maze, x, y, visited):
    if maze[x][y] == 3:
        return True  

    visited.add((x, y)) 

    #Possible moves 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if is_valid_move(maze, nx, ny, visited):
            if dfs_maze(maze, nx, ny, visited): 
                return True

    return False  

def can_reach_target(maze):
    start = find_root(maze)
    if start is None:
        return False 
    visited = set()
    return dfs_maze(maze, start[0], start[1], visited)


maze1 = [
    [2, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 3, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0]
]


result = can_reach_target(maze1)
print("There is a path from 2 to 3:", result)
