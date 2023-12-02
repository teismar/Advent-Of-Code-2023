"""
This is the solution for the first game problem of Advent of Code 2023 day 2.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-02
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

def get_game_metadata(input_str: str) -> dict:
    """
    Parse a input string for one game.
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    It will return a dictionary with the metadata of the game.
    So the max number of one color per round.
    :param input_str:
    :return metadata:
    """
    # Remove the "Game X: " part
    input_str = input_str.split(": ")[1]

    # Split the string into the rounds
    rounds = input_str.split("; ")

    # Initialize the metadata dictionary
    metadata = {
        "blue": 0,
        "red": 0,
        "green": 0
    }

    # Iterate over the rounds
    for round in rounds:
        # Split the round into the colors
        colors = round.split(", ")

        # Iterate over the colors
        for color in colors:
            # Split the color into the number and the color
            number, color = color.split(" ")

            # Update the metadata
            metadata[color] = max(metadata[color], int(number))

    return metadata


def main(maxRed: int, maxGreen: int, maxBlue: int):
    """
    Parse the input file and calculate the individual calibration values of each line.
    Then sum them up and print the result.
    :param maxRed:
    :param maxBlue:
    :param maxGreen:
    :return:
    """
    input_list = file_to_list("game_input.txt")
    game_list = []
    for line in input_list:
        meta = {"gameID": int(line.split(": ")[0].split(" ")[1]), "metadata": get_game_metadata(line)}
        game_list.append(meta)

    added_games = 0
    for game in game_list:
        if game["metadata"]["red"] <= maxRed and game["metadata"]["green"] <= maxGreen and game["metadata"]["blue"] <= maxBlue:
            added_games += game["gameID"]

    print("The sum of the game IDs is: " + str(added_games))

if __name__ == "__main__":
    main(12, 13, 14)
