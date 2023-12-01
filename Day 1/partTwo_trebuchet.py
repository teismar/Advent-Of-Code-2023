"""
This is the solution for the second trebuchet problem of Advent of Code 2023 day 1.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-01
"""

from partOne_trebuchet import file_to_list, calculate_calibration_value


def replace_textnumbers_with_ints(input_str: str) -> str:
    """
    Replace all text numbers with integers.
    :param input_str:
    :return:
    """
    # A mapping of text numbers to integers
    # Appending the rest of the text number to the integer for overlapping text numbers
    mapping = {"zero": "0ero", "one": "1ne", "two": "2wo", "three": "3hree", "four": "4our", "five": "5ive",
               "six": "6ix",
               "seven": "7even", "eight": "8ight", "nine": "9ine"}

    # A list to store the text numbers and their index
    tupel_list = []

    # For every element in the mapping
    for text_number in mapping.keys():

        # If the text number is in the input string
        if text_number in input_str:

            # for every occurence of the text number
            for i in range(input_str.count(text_number)):

                # get the index of the last found text number
                last_index = 0
                if i > 0:
                    last_index = tupel_list[-1][1] + 1

                # Get the index of the text number
                index = input_str.find(text_number, last_index)

                # Add the text number and its index to the list
                tupel_list.append((text_number, index))

    # Sort the list by the index
    tupel_list.sort(key=lambda tup: tup[1])

    # Save the input string before replacing the text numbers for debugging
    before = input_str

    # For every text number in the list
    for tupel in tupel_list:
        # If the text number is in the input string
        if tupel[0] in input_str:
            # Replace the text number with the integer
            input_str = input_str.replace(tupel[0], str(mapping[tupel[0]]), 1)

    # Check if there are still text numbers in the input string if so print the error and exit
    for map in mapping.keys():
        if map in input_str:
            print(f"ERROR: {map} is still in the input string")
            print(f"Before: {before}")
            print(f"After: {input_str}")
            print(f"Tuple list: {tupel_list}")
            exit()

    return input_str


def main():
    """
    Parse the input file and calculate the individual calibration values of each line.
    Then sum them up and print the result.
    :return:
    """
    input_list = file_to_list("trebuchet_input.txt")
    # Replace all text numbers with integers
    for i in range(len(input_list)):
        input_list[i] = replace_textnumbers_with_ints(input_list[i])

    # Calculate the calibration value
    calibration_value = 0
    for line in input_list:
        calibration_value += calculate_calibration_value(line)

    print("The calibration value is: " + str(calibration_value))


if __name__ == "__main__":
    main()
