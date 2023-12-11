"""
This is the solution for the second part problem of Advent of Code 2023 day 11.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-11
"""

from partOne_galaxy import file_to_list, number_galaxies, all_shortest_paths, tqdm

def extend_data(data: list, times: int) -> list:
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
    empty_rows = [i for i, row in enumerate(data)if all(cell == "." for cell in row)]
    empty_cols = [j for j in range(col_count) if all(data[i][j] == "." for i in range(row_count))]

    # Double the size of empty rows
    for i in reversed(empty_rows):
        for _ in tqdm(range(times-1)):
            data.insert(i, data[i][:])

    # Double the size of empty columns
    for j in reversed(empty_cols):
        for row in data:
            for _ in tqdm(range(times-1)):
                row.insert(j, row[j])

    return data

def main():
    content = file_to_list("datasheet.txt")

    for i in range(len(content)):
        content[i] = [*content[i]]

    print("Starting extending data...")
    extended = extend_data(content, 1000000)
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
