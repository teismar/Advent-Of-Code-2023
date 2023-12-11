"""
This is the solution for the first part problem of Advent of Code 2023 day 10.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-10
"""


def file_to_list(filename: str) -> list:
    """
    Read the file and return a list of the strings of each line.
    :param filename:
    :return content:
    """
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def find_starting_point(content: list) -> (int, int):
    """
    Find the starting point of the maze
    :param content:
    :return:
    """
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == "S":
                return i, j


def next_pipe(content: list, current_point: (int, int), origin_point: (int, int)) -> (int, int):
    """
    Find the next pipe in the maze
    :param origin_point:
    :param content:
    :param current_point:
    :return:
    """
    up, right, down, left = None, None, None, None
    # Check if current point is the origin point
    if current_point[0] - 1 >= 0:
        if current_point[0] - 1 != origin_point[0]:
            up = content[current_point[0] - 1][current_point[1]]
    if current_point[1] + 1 < len(content[0]):
        if current_point[1] + 1 != origin_point[1]:
            right = content[current_point[0]][current_point[1] + 1]
    if current_point[0] + 1 < len(content):
        if current_point[0] + 1 != origin_point[0]:
            down = content[current_point[0] + 1][current_point[1]]
    if current_point[1] - 1 >= 0:
        if current_point[1] - 1 != origin_point[1]:
            left = content[current_point[0]][current_point[1] - 1]


    # Map of possible next pipes for each pipe
    if content[current_point[0]][current_point[1]] == "S":
        # Check Up
        if up == "|" or up == "F" or up == "7":
            return current_point[0] - 1, current_point[1]
        # Check Right
        if right == "-" or right == "J" or right == "7":
            return current_point[0], current_point[1] + 1
        # Check Down
        if down == "|" or down == "L" or down == "J":
            return current_point[0] + 1, current_point[1]
        # Check Left
        if left == "-" or left == "F" or left == "L":
            return current_point[0], current_point[1] - 1

    elif content[current_point[0]][current_point[1]] == "-":
        # Check Right
        if right == "-" or right == "J" or right == "7":
            return current_point[0], current_point[1] + 1
        # Check Left
        if left == "-" or left == "F" or left == "L":
            return current_point[0], current_point[1] - 1

    elif content[current_point[0]][current_point[1]] == "|":
        # Check Up
        if up == "|" or up == "F" or up == "7":
            return current_point[0] - 1, current_point[1]
        # Check Down
        if down == "|" or down == "L" or down == "J":
            return current_point[0] + 1, current_point[1]

    elif content[current_point[0]][current_point[1]] == "J":
        # Check Up
        if up == "|" or up == "F" or up == "7":
            return current_point[0] - 1, current_point[1]
        # Check left
        if left == "-" or left == "F" or left == "L":
            return current_point[0], current_point[1] - 1

    elif content[current_point[0]][current_point[1]] == "L":
        # Check Up
        if up == "|" or up == "F" or up == "7":
            return current_point[0] - 1, current_point[1]
        # Check Right
        if right == "-" or right == "J" or right == "7":
            return current_point[0], current_point[1] + 1

    elif content[current_point[0]][current_point[1]] == "7":
        # Check Down
        if down == "|" or down == "L" or down == "J":
            return current_point[0] + 1, current_point[1]
        # Check Left
        if left == "-" or left == "F" or left == "L":
            return current_point[0], current_point[1] - 1

    elif content[current_point[0]][current_point[1]] == "F":
        # Check Down
        if down == "|" or down == "L" or down == "J":
            return current_point[0] + 1, current_point[1]
        # Check Right
        if right == "-" or right == "J" or right == "7":
            return current_point[0], current_point[1] + 1

    return None


def find_furthest_point(content: list, starting_point: (int, int)) -> int:
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

    # Find the furthest point
    return len(path_points) // 2

def main():
    """
    Main function
    """
    content = file_to_list("pipes.txt")
    starting_point = find_starting_point(content)
    furthest_point = find_furthest_point(content, starting_point)
    print(content)
    print(starting_point)
    print(furthest_point)


if __name__ == "__main__":
    main()
