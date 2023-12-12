# file: partOne_StupidEngineer.py

"""
This is the solution for the first part problem of Advent of Code 2023 day 12.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-12
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

def get_combinations(template, chars):
    def build_combinations(current, index, all_combinations):
        if index == len(template):
            all_combinations.append(current)
            return

        if template[index] == '?':
            for char in chars:
                build_combinations(current + char, index + 1, all_combinations)
        else:
            build_combinations(current + template[index], index + 1, all_combinations)

    combinations = []
    build_combinations('', 0, combinations)
    return combinations

def is_valid(arrangement: str, defects: list) -> bool:
    """
    Check if the arrangement of springs is valid.
    :param arrangement:
    :param defect:
    :return:
    """
    list_of_defects = []
    defect_len = 0

    for char in arrangement:
        if char == "#":
            defect_len += 1
        else:
            list_of_defects.append(defect_len)
            defect_len = 0

    list_of_defects.append(defect_len)

    # Remove all zeros from the list
    list_of_defects = list(filter(lambda a: a != 0, list_of_defects))

    # Check if the arrangement is valid
    if list_of_defects == defects:
        return True
    else:
        return False

def get_possible_arrangements(content: list, cache: dict) -> (int, dict):
    """
    Get the possible arrangements of the broken springs.
    :param content:
    :return:
    """
    springs = content[0]
    defect = content[1].split(",")
    for i in range(len(defect)):
        defect[i] = int(defect[i])

    comb = str(springs) + str(defect)
    if comb in cache:
        return cache[comb], cache

    # Get all possible arrangements that result in a valid arrangement of defect springs
    possible_arrangements = get_combinations(springs, ["#", "?"])

    new_possible_arrangements = []

    # Remove all arrangements that do not result in a valid arrangement of defect springs
    for arrangement in possible_arrangements:
        if is_valid(arrangement, defect):
            new_possible_arrangements.append(arrangement)

    cache[comb] = len(new_possible_arrangements)

    return cache[comb], cache


def main():
    """
    Main function
    """
    filename = "springplan.txt"
    content = file_to_list(filename)
    arr = 0
    cache = {}
    for line in content:
        new_arr, cache = get_possible_arrangements(line.split(" "), cache)
        arr += new_arr

    print("The number of possible arrangements is: {}".format(arr))

if __name__ == "__main__":
    main()