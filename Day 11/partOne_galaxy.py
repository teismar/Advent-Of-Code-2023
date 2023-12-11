"""
This is the solution for the first part problem of Advent of Code 2023 day 11.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-11
"""

from tqdm import tqdm

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


def extend_data(data: list) -> list:
    """
    Extend the data by doubling the size of empty rows and columns.
    :param data: A 2D list of data.
    :return: A 2D list with extended data.
    """
    if not data or not data[0]:
        return data  # Return original data if it's empty or has no columns.

    row_count = len(data)
    col_count = len(data[0])

    # Identify empty rows and columns
    empty_rows = [i for i, row in enumerate(data) if all(cell == "." for cell in row)]
    empty_cols = [j for j in range(col_count) if all(data[i][j] == "." for i in range(row_count))]

    # Double the size of empty rows
    for i in reversed(empty_rows):
        data.insert(i, data[i][:])

    # Double the size of empty columns
    for j in reversed(empty_cols):
        for row in data:
            row.insert(j, row[j])

    return data


def number_galaxies(data: list) -> (list, int):
    """
    Number the galaxies in the data.
    :param data:
    :return:
    """
    galaxy_count = 1
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "#":
                data[i][j] = galaxy_count
                galaxy_count += 1
    return data, galaxy_count - 1


def shortest_path(galaxy_one: int, galaxy_two: int, data: list, cache: dict) -> (int, dict):
    """
    Find the shortest path between two galaxies.
    :param galaxy_one:
    :param galaxy_two:
    :param data:
    :return:
    """
    coords_one = None
    coords_two = None
    if galaxy_one in cache:
        coords_one = cache[galaxy_one]
    if galaxy_two in cache:
        coords_two = cache[galaxy_two]

    if not coords_one or not coords_two:
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                if cell == galaxy_one and not coords_one:
                    coords_one = (i, j)
                    cache[galaxy_one] = coords_one
                if cell == galaxy_two and not coords_two:
                    coords_two = (i, j)

    return abs(coords_one[0] - coords_two[0]) + abs(coords_one[1] - coords_two[1]), cache


def all_shortest_paths(data: list, galaxies: int) -> int:
    """
    Find the shortest path between all galaxies.
    :param data:
    :return:
    """
    # All galaxies
    all_galaxies = [i for i in range(1, galaxies + 1)]

    # All possible combinations of galaxies
    all_combinations = [(i, j) for i in all_galaxies for j in all_galaxies if i != j]

    # Remove duplicates
    all_combinations = [tuple(sorted(combination)) for combination in all_combinations]
    all_combinations = list(set(all_combinations))

    # Find the shortest path between all galaxies
    shortest_paths = []
    cache = {}
    for combination in tqdm(all_combinations):
        s_path, cache = shortest_path(combination[0], combination[1], data, cache)
        shortest_paths.append(s_path)

    return sum(shortest_paths)


def main():
    content = file_to_list("datasheet.txt")

    for i in range(len(content)):
        content[i] = [*content[i]]

    print("Starting extending data...")
    extended = extend_data(content)
    print("Data extended.")

    print("Starting numbering galaxies...")
    numbered, galaxy_count = number_galaxies(extended)
    print("Galaxies numbered.")

    print("Starting finding shortest paths...")
    summed_paths = all_shortest_paths(numbered, galaxy_count)
    print("All shortest paths found.")

    print("The sum of all shortest paths is: {}".format(summed_paths))


if __name__ == "__main__":
    main()
