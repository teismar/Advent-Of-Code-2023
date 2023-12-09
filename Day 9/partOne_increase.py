"""
This is the solution for the first part problem of Advent of Code 2023 day 9.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-09
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

def get_next_number(numbers: list) -> int:
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


    # Calculate the result
    result = 0
    step_list.reverse()
    for i in range(len(step_list)):
        result += step_list[i][-1]

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
        result += get_next_number(numbers)

    print(result)
if __name__ == "__main__":
    main()