"""
This is the solution for the first part problem of Advent of Code 2023 day 8.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-08
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


def inputList_to_list_and_dict(inputList: list) -> (list, dict):
    """
    Get the input list and return a list of the instructions and a dict of the nodes
    :param inputList:
    :return:
    """
    instructions = [*inputList[0]]
    nodes = {}
    for i in range(2, len(inputList)):
        temp = inputList[i].split("=")
        temp [1] = temp[1].strip().strip("()").split(", ")
        nodes[temp[0].strip()] = (temp[1][0], temp[1][1])
    return instructions, nodes

def walk_tree(instructions: list, nodes: dict) -> int:
    """
    Walk the tree and return the value steps
    :param instructions:
    :param nodes:
    :return:
    """
    counter = 0
    current = "AAA"
    while current != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current = nodes[current][0]
            elif instruction == "R":
                current = nodes[current][1]
            else:
                print("Error")
        counter += 1

    return counter * len(instructions)

def main():
    """
    Main function.
    """
    content = file_to_list("net.txt")
    instructions, nodes = inputList_to_list_and_dict(content)
    counter = walk_tree(instructions, nodes)
    print(f"Solution: {counter}")


if __name__ == "__main__":
    main()
