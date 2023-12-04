"""
This is the solution for the first part problem of Advent of Code 2023 day 4.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-04
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

def game_to_points(game: str) -> int:
    """
    Calculate the points of a game.
    :param game:
    :return points:
    """
    # Split the string into the Game ID and the game data
    game_id, game_data = game.split(':')

    # Split the things i have and the winning numbers
    winning_numbers, things = game_data.split('|')

    # Split the things into words
    things = things.split()

    # Split the winning numbers into numbers
    winning_numbers = set(winning_numbers.split())


    # Loop over the things and check if they are in the winning numbers
    result = 0
    for thing in things:
        if thing in winning_numbers:
            if result == 0:
                result = 1
            else:
                result *= 2

    return result



def main():
    """
    Main function.
    """
    # Read the file and get a list of the games
    games = file_to_list('input.txt')

    # Loop over the games and calculate the points
    points = 0
    for game in games:
        points += game_to_points(game)

    print(points)

if __name__ == '__main__':
    main()