"""
This is the solution for the second game problem of Advent of Code 2023 day 2.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-02
"""

from partOne_game import file_to_list, get_game_metadata

def main():
    """
    Parse the input file and calculate the individual minimal number of each color. (minRed * minGreen * minBlue)
    Then sum them up and print the result.
    :return:
    """
    input_list = file_to_list("game_input.txt")
    sum_of_powers = 0
    for input_str in input_list:
        metadata = get_game_metadata(input_str)
        sum_of_powers += metadata["red"] * metadata["green"] * metadata["blue"]

    print(f"The sum of the powers is: {sum_of_powers}")


if __name__ == "__main__":
    main()