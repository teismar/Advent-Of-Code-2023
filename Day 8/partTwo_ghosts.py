"""
This is the solution for the second part problem of Advent of Code 2023 day 8.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-08
"""

from partOne_network import file_to_list, inputList_to_list_and_dict


def find_starting_poinzs(nodes: dict) -> list:
    """
    Find the starting points of the network.
    :param nodes:
    :return:
    """
    starting_points = []
    for node in nodes:
        if 'A' in node:
            starting_points.append(node)
    return starting_points


def walk_tree(instructions: list, nodes: dict, start: str) -> str:
    """
    Walk the tree and return the value we end up with.
    :param instructions:
    :param nodes:
    :param start:
    :return:
    """
    current = start
    for instruction in instructions:
        if instruction == "L":
            current = nodes[current][0]
        elif instruction == "R":
            current = nodes[current][1]
        else:
            print("Error")
    return current


def z_in_all(currents: list) -> bool:
    """
    Check if all currents contain a Z.
    :param currents:
    :return:
    """
    for current in currents:
        if 'Z' not in current:
            return False
    return True


def find_number_of_steps(instructions: list, nodes: dict, starting_points: list) -> int:
    """
    Find the number of repetitions needed.
    :param instructions:
    :param nodes:
    :param starting_points:
    :return:
    """
    counter = 0
    while not z_in_all(starting_points):
        for start in range(len(starting_points)):
            starting_points[start] = walk_tree(instructions, nodes, starting_points[start])
        counter += 1
    return counter * len(instructions)


def main():
    """
    Main function.
    """
    content = file_to_list("ghost.txt")
    instructions, nodes = inputList_to_list_and_dict(content)
    starting_points = find_starting_poinzs(nodes)
    counter = find_number_of_steps(instructions, nodes, starting_points)
    print(f"Solution: {counter}")


if __name__ == "__main__":
    main()
