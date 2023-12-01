"""
This is the soltuion for the first trebuchet problem of Advent of Code 2023 day 1.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-01
"""

def file_to_list(filename : str) -> list:
    """
    Read the file and return a list of the strings of each line.
    :param filename:
    :return content:
    """
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def calculate_calibration_value(input_string : str) -> int:
    """
    Calculate the calibration value of the input string.
    So search for the first and last occurence of an integer and concatenate them.
    :param input_string:
    :return:
    """
    # Search for the first integer
    first_int = 0
    for i in input_string:
        if i.isdigit():
            first_int = int(i)
            break

    # Reverse the string and search for the first integer
    last_int = 0
    for i in input_string[::-1]:
        if i.isdigit():
            last_int = int(i)
            break

    # Concatenate the two integers
    return int(str(first_int) + str(last_int))


def main():
    """
    Parse the input file and calculate the individual calibration values of each line.
    Then sum them up and print the result.
    :return:
    """
    input_list = file_to_list("trebuchet_input.txt")
    calibration_value = 0
    for line in input_list:
        calibration_value += calculate_calibration_value(line)
    print(calibration_value)

if __name__ == "__main__":
    main()