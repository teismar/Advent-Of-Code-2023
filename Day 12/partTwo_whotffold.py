# file: partTwo_whotffold.py

"""
This is the solution for the second part problem of Advent of Code 2023 day 12.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-12
"""

from partOne_StupidEngineer import file_to_list, is_valid

def get_combinations(template, chars, defect):
    def build_combinations(current, index, all_combinations):
        if index == len(template):
            if is_valid(current, defect):
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


def get_possible_arrangements(content: list, cache: dict, times: int) -> (int, dict):
    """
    Get the possible arrangements of the broken springs.
    :param content:
    :return:
    """
    springs = content[0]
    defect = content[1]

    # Take the springs str times 'times' seperated by a '?'
    springs = (springs + "?") * times
    # Remove the last '?'
    springs = springs[:-1]

    # Take the defect list times 'times' seperated by a ','
    defect = (defect + ",") * times
    # Remove the last ','
    defect = defect[:-1]
    # Split the string at the ','
    defect = defect.split(",")

    for i in range(len(defect)):
        defect[i] = int(defect[i])

    comb = str(springs) + str(defect)
    if comb in cache:
        return cache[comb], cache

    # Get all possible arrangements that result in a valid arrangement of defect springs
    possible_arrangements = get_combinations(springs, ["#", "?"], defect)


    cache[comb] = len(possible_arrangements)

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
        new_arr, cache = get_possible_arrangements(line.split(" "), cache, 5)
        arr += new_arr

    print("The number of possible arrangements is: {}".format(arr))

if __name__ == "__main__":
    main()