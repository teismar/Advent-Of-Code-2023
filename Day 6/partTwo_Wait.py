"""
This is the solution for the second part problem of Advent of Code 2023 day 5.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-06
"""

from partOne_Wait import file_to_list, possible_distances_in_time


def input_to_tuple(input_list: list) -> tuple:
    """
    Convert the input list to a tuple.
    :param input_list:
    :return:
    """
    times = input_list[0].split()[1:]
    distances = input_list[1].split()[1:]

    time = "".join(times)
    distances = "".join(distances)

    return (int(time), int(distances))


def main():
    """
    Main function.
    :return:
    """
    input_list = file_to_list("records.txt")
    this_tuple = input_to_tuple(input_list)

    # Calculate the possible distances for the time in question
    distances_possible = possible_distances_in_time(this_tuple[0])

    # Remove distances that are shorter than the record
    longer_distances = [x for x in distances_possible if x > this_tuple[1]]

    # Calculate the times the record is beaten
    time_record_beaten = len(longer_distances)

    # Print the result
    print(f"The record is beaten {time_record_beaten} times.")


if __name__ == "__main__":
    main()
