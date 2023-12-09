"""
This is the solution for the second part problem of Advent of Code 2023 day 9.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-09
"""

from partOne_increase import file_to_list

def get_previous_number(numbers: list) -> int:
    """
    Get the next number
    :param numbers:
    :return next_number:
    """
    step_list = []
    step_list.append(numbers)
    while any(step_list[-1]):
        this_step = []
        for i in range(len(step_list[-1][:-1])):
            this_step.append(step_list[-1][i+1] - step_list[-1][i])
        step_list.append(this_step)

    step_list.reverse()
    # Calculate the result
    result = 0
    for i in range(len(step_list)):
        result = step_list[i][0] - result
    return result

def main():
    """
    Main function
    """
    filename = "numbers.txt"
    content = file_to_list(filename)
    result = 0
    for numbers in content:
        # Split the numbers
        numbers = numbers.split()
        # To int
        numbers = [int(i) for i in numbers]
        # Get the next number
        result += get_previous_number(numbers)

    print(result)
if __name__ == "__main__":
    main()