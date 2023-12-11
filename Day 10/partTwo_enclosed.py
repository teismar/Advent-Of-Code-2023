"""
This is the solution for the second part problem of Advent of Code 2023 day 10.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-10
"""

from partOne_furthest import file_to_list, find_starting_point, next_pipe

def flood_fill(grid, x, y, visited):
    """ Perform flood fill algorithm to mark all reachable '.' from (x, y) """
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] != 'O':
        return
    visited[x][y] = True
    flood_fill(grid, x + 1, y, visited)
    flood_fill(grid, x - 1, y, visited)
    flood_fill(grid, x, y + 1, visited)
    flood_fill(grid, x, y - 1, visited)

def get_flood_rest(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Marking all outer '.' as visited
    for i in range(rows):
        if grid[i][0] == 'O':
            flood_fill(grid, i, 0, visited)
        if grid[i][cols-1] == 'O':
            flood_fill(grid, i, cols-1, visited)

    for j in range(cols):
        if grid[0][j] == 'O':
            flood_fill(grid, 0, j, visited)
        if grid[rows-1][j] == 'O':
            flood_fill(grid, rows-1, j, visited)

    # List of coordinates of all enclosed points
    enclosed_points = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O' and not visited[i][j]:
                enclosed_points.append((i, j))

    return enclosed_points

def count_enclosed_points(grid, path_points):
    """ Count the number of enclosed points """

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in path_points:
                grid[i][j] = 'O'

    for line in grid:
        print(line)

    r_list = []
    flip_vert = 0
    flip_hor = 1
    for point in path_points:
        p = grid[point[0]][point[1]]
        up, right, down, left = None, None, None, None
        if point[0] > 0:
            up = grid[point[0] - 1][point[1]]
        if point[0] < len(grid) - 1:
            down = grid[point[0] + 1][point[1]]
        if point[1] > 0:
            left = grid[point[0]][point[1] - 1]
        if point[1] < len(grid[0]) - 1:
            right = grid[point[0]][point[1] + 1]
            
        if p == '-':
            if flip_hor == 1:
                if down == 'O':
                    grid[point[0] +1][point[1]] = 'R'
            else:
                if up == 'O':
                    grid[point[0] -1][point[1]] = 'R'
        if p == '|':
            if flip_vert == 0:
                if left == 'O':
                    grid[point[0]][point[1] -1] = 'R'
            else:
                if right == 'O':
                    grid[point[0]][point[1] +1] = 'R'
        if p == '7':
            if flip_hor == 0:
                if up == 'O':
                    grid[point[0] -1][point[1]] = 'R'
            if flip_vert == 0:
                if right == 'O':
                    grid[point[0]][point[1] +1] = 'R'
            flip_hor = 0
            flip_vert = 0

        if p == 'L':
            if flip_hor == 0:
                if down == 'O':
                    grid[point[0] +1][point[1]] = 'R'
            flip_hor = 1
            flip_vert = 1
        if p == 'F':
            if flip_hor == 0:
                if up == 'O':
                    grid[point[0] -1][point[1]] = 'R'
            if flip_vert == 0:
                if left == 'O':
                    grid[point[0]][point[1] -1] = 'R'
            flip_vert = 0
            flip_hor = 1
        if p == 'J':
            if flip_vert == 1:
                if right == 'O':
                    grid[point[0]][point[1] +1] = 'R'
            flip_hor = 0
            flip_vert = 1

    counter = 0

    for line in grid:
        # Print the char list as a string
        str = ""
        for char in line:
            str += char
        print(str)

    for i in range(500):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    up, right, down, left = None, None, None, None
                    if i > 0:
                        up = grid[i - 1][j]
                    if i < len(grid) - 1:
                        down = grid[i + 1][j]
                    if j > 0:
                        left = grid[i][j - 1]
                    if j < len(grid[0]) - 1:
                        right = grid[i][j + 1]
                    if up == 'R' or right == 'R' or down == 'R' or left == 'R':
                        grid[i][j] = 'R'

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'R':
                counter += 1

    print(counter)

def find_enclosed_count(content: list, starting_point: (int, int)) -> int:
    """
    Find the furthest point from the starting point and return the distance (number of steps)
    :param content:
    :param starting_point:
    :return:
    """
    path_points = []

    path_points.append(starting_point)
    next_point = next_pipe(content, starting_point, starting_point)
    path_points.append(next_point)
    previous_point = starting_point

    while next_point is not None:
        next_point = next_pipe(content, next_point, previous_point)
        previous_point = path_points[-1]
        path_points.append(next_point)

    # Remove last point because it is None
    path_points.pop(-1)

    # content to list of lists
    for i in range(len(content)):
        content[i] = [*content[i]]

    print(path_points)
    for i in range(len(content)):
        tline = ""
        for j in range(len(content[0])):
            if (i, j) in path_points:
                tline += content[i][j]
            else:
                tline += "."
        print(tline)

    print(count_enclosed_points(content, path_points))

    return len(path_points)

def main():
    """
    Main function
    """
    # Increase recursion limit
    import sys
    sys.setrecursionlimit(10000000)
    content = file_to_list("pipes.txt")
    starting_point = find_starting_point(content)
    furthest_point = find_enclosed_count(content, starting_point)


if __name__ == "__main__":
    main()