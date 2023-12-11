def file_to_list(filename):
    try:
        with open(filename) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def find_starting_point(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return None

def get_adjacent_points(grid, point):
    x, y = point
    directions = []
    if x > 0:
        directions.append((x-1, y))
    if x < len(grid) - 1:
        directions.append((x+1, y))
    if y > 0:
        directions.append((x, y-1))
    if y < len(grid[x]) - 1:
        directions.append((x, y+1))
    return directions

def is_valid_pipe(grid, point, from_point):
    x, y = point
    fx, fy = from_point
    pipe = grid[x][y]
    if pipe in ".S":
        return True
    if fx == x:
        return pipe in "|FJ7L"
    if fy == y:
        return pipe in "-FJ7L"
    return False

def find_loop(grid, start):
    loop = set()
    stack = [start]
    while stack:
        point = stack.pop()
        if point in loop:
            continue
        loop.add(point)
        for adj_point in get_adjacent_points(grid, point):
            if is_valid_pipe(grid, adj_point, point):
                stack.append(adj_point)
    return loop

def flood_fill(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] != '.':
        return
    visited[x][y] = True
    flood_fill(grid, x + 1, y, visited)
    flood_fill(grid, x - 1, y, visited)
    flood_fill(grid, x, y + 1, visited)
    flood_fill(grid, x, y - 1, visited)

def count_enclosed_tiles(grid, loop):
    visited = [[False for _ in row] for row in grid]
    for x in range(len(grid)):
        flood_fill(grid, x, 0, visited)
        flood_fill(grid, x, len(grid[0]) - 1, visited)
    for y in range(len(grid[0])):
        flood_fill(grid, 0, y, visited)
        flood_fill(grid, len(grid) - 1, y, visited)

    return sum(1 for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == '.' and not visited[x][y])

def main():
    grid = file_to_list("pipes.txt")
    start = find_starting_point(grid)
    if start is None:
        print("Starting point not found.")
        return
    loop = find_loop(grid, start)
    print(loop)
    enclosed_tiles = count_enclosed_tiles(grid, loop)
    print(f"Number of enclosed tiles: {enclosed_tiles}")

if __name__ == "__main__":
    main()
