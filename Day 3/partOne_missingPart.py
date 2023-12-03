"""
This is the solution for the first gear problem of Advent of Code 2023 day 3.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-03
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


def list_of_strings_to_list_of_lists(list_of_strings: list) -> list:
    """
    Convert a list of strings to a list of lists.
    :param list_of_strings:
    :return list_of_lists:
    """
    list_of_lists = []
    for string in list_of_strings:
        list_of_lists.append([x for x in string])
    return list_of_lists

def is_adjacent_to_symbol(list_of_lists, row, col):
    # Directions to check: (row_change, col_change)
    directions = [(-1, -1), (-1, 0), (-1, 1),  # Up Left, Up, Up Right
                  (0, -1), (0, 1),            # Left, Right
                  (1, -1), (1, 0), (1, 1)]    # Down Left, Down, Down Right

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if new_row and new_col are within the bounds of the list
        if 0 <= new_row < len(list_of_lists) and 0 <= new_col < len(list_of_lists[0]):
            adjacent_char = list_of_lists[new_row][new_col]
            # Check if the adjacent character is a symbol (not a digit and not a '.')
            if not adjacent_char.isdigit() and adjacent_char != ".":
                return True

    return False


def find_valid_numbers(list_of_lists: list) -> int:
    sum_of_partnumbers = 0

    # Iterate over the list of lists
    for idl, lst in enumerate(list_of_lists):
        idc = 0
        while idc < len(lst):
            char = lst[idc]
            if char.isdigit():
                # Identify the full number
                number = char
                number_end_index = idc
                while number_end_index + 1 < len(lst) and lst[number_end_index + 1].isdigit():
                    number_end_index += 1
                    number += lst[number_end_index]

                # Check if the number is adjacent to a symbol
                if any(is_adjacent_to_symbol(list_of_lists, idl, idx) for idx in range(idc, number_end_index + 1)):
                    sum_of_partnumbers += int(number)

                # Update idc to skip the processed part of the number
                idc = number_end_index + 1
            else:
                idc += 1

    return sum_of_partnumbers




def main():
    """
    Main function of the program.
    :return:
    """
    filename = "parts.txt"
    list_of_strings = file_to_list(filename)
    list_of_lists = list_of_strings_to_list_of_lists(list_of_strings)
    print(list_of_lists)
    sum_of_partnumbers = find_valid_numbers(list_of_lists)
    print("The sum of the partnumbers is: " + str(sum_of_partnumbers))


if __name__ == "__main__":
    main()
