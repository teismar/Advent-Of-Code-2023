"""
This is the solution for the first part problem of Advent of Code 2023 day 5.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-06
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


def input_to_tuple_list(input_lists: list) -> list:
    """
    Convert the input list to a list of tuples.
    :param input_lists:
    :return:
    """
    output = []
    # Split the input lists into two lists
    times = input_lists[0].split()
    distances = input_lists[1].split()

    for i in range(len(times[1:])):
        output.append((int(times[i + 1]), int(distances[i + 1])))

    return output


def possible_distances_in_time(time_in_question: int) -> list:
    """
    For a given time, return a list of possible distances.
    :param time_in_question:
    :return:
    """
    distances = []
    for i in range(time_in_question + 1):
        speed = i
        distance = speed * (time_in_question - i)
        distances.append(distance)
    return distances


def calculate_record_beating_times(tuple_list: list) -> list:
    """
    Calculate the times the record is beaten.
    :param tuple_list:
    :return:
    """
    record_beating_times = []
    for this_tuple in tuple_list:
        distances_possible = possible_distances_in_time(int(this_tuple[0]))
        # Remove distances that are shorter than the record
        longer_distances = [x for x in distances_possible if x > this_tuple[1]]
        record_beating_times.append(len(longer_distances))
    return record_beating_times


def main():
    """
    Main function of the program.
    """
    input_list = file_to_list("records.txt")
    tuple_list = input_to_tuple_list(input_list)
    records = calculate_record_beating_times(tuple_list)

    # Multiply all the numbers in the list
    result = 1
    for x in records:
        result *= x

    print(f"The result is {result}.")


if __name__ == "__main__":
    main()
