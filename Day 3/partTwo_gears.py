"""
This is the solution for the second gear problem of Advent of Code 2023 day 3.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-03
"""

from partOne_missingPart import file_to_list, list_of_strings_to_list_of_lists


def is_adjacent_to_symbol(list_of_lists, row, col) -> (bool, tuple):
    """
    Check if the character at the given row and column is adjacent to a symbol.
    Get the coordinates of the adjacent symbol.
    :param list_of_lists:
    :param row:
    :param col:
    :return:
    """
    # Directions to check: (row_change, col_change)
    directions = [(-1, -1), (-1, 0), (-1, 1),  # Up Left, Up, Up Right
                  (0, -1), (0, 1),  # Left, Right
                  (1, -1), (1, 0), (1, 1)]  # Down Left, Down, Down Right

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if new_row and new_col are within the bounds of the list
        if 0 <= new_row < len(list_of_lists) and 0 <= new_col < len(list_of_lists[0]):
            adjacent_char = list_of_lists[new_row][new_col]
            # Check if the adjacent character is a '*'
            if adjacent_char == "*":
                # Return True and the coordinates of the adjacent symbol
                return True, (new_row, new_col)

    return False, None


def find_valid_numbers(list_of_lists: list) -> int:
    """
    Find all valid numbers in the list of lists.
    :param list_of_lists:
    :return:
    """
    sum_of_partnumbers = 0
    numbers_with_symbols = []

    # Iterate over the list of lists
    for idl, lst in enumerate(list_of_lists):
        idc = 0
        while idc < len(lst):
            char = lst[idc]
            if char.isdigit():
                # Identify the full number
                number = char
                number_end_index = idc
                # Check if the next character is a digit to get the full number
                while number_end_index + 1 < len(lst) and lst[number_end_index + 1].isdigit():
                    number_end_index += 1
                    number += lst[number_end_index]

                # Check if the number is adjacent to a symbol
                for idx in range(idc, number_end_index + 1):
                    isIt, coords = is_adjacent_to_symbol(list_of_lists, idl, idx)
                    if isIt:
                        numbers_with_symbols.append((number, coords))
                        break

                # Update idc to skip the processed part of the number
                idc = number_end_index + 1
            else:
                idc += 1

    # Sort the list of numbers with symbols by the coordinates of the symbols
    numbers_with_symbols.sort(key=lambda x: x[1])

    # Iterate over the list of numbers with symbols
    for i in range(len(numbers_with_symbols) - 1):
        # Check if the symbols are the same for the current and the next number
        if numbers_with_symbols[i][1] == numbers_with_symbols[i + 1][1]:
            # Add the product of the two numbers to the sum
            sum_of_partnumbers += int(int(numbers_with_symbols[i][0]) * int(numbers_with_symbols[i + 1][0]))

    return sum_of_partnumbers


def main():
    """
    Main function.
    :return:
    """
    # Get the list of strings from the file
    list_of_strings = file_to_list("parts.txt")

    # Convert the list of strings to a list of lists
    list_of_lists = list_of_strings_to_list_of_lists(list_of_strings)

    # Find the valid numbers
    valid_numbers = find_valid_numbers(list_of_lists)

    # Print the result
    print(f"The sum of the valid numbers is {valid_numbers}.")


if __name__ == "__main__":
    main()
