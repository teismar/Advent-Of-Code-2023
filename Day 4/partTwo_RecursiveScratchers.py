"""
This is the solution for the first part problem of Advent of Code 2023 day 4.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-04
"""

from partOne_Scratch import file_to_list
import sys


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
            result += 1

    return result


def game_to_games_recursive(origlist: list, gamelist: list, cache: dict, counter: int = 0) -> int:
    """
    Calculate amount of games played. Tried to do it recursive but with the big input file it takes to many recursions.
    :param origlist:
    :param gamelist:
    :param cache:
    :param counter:
    :return:
    """

    if len(gamelist) == 0:
        return counter
    else:
        # Get the first game data
        game = gamelist[0]
        game_id, game_data = game.split(':')
        game_id = int(game_id.strip('Card '))
        if game_id in cache:
            gamelist += cache[game_id]
        else:
            points = game_to_points(game)
            temp = []
            # Add games according to the points
            for i in range(points):
                temp.append(origlist[game_id + i])
            cache[game_id] = temp
            gamelist += temp

        # Remove the game from the list
        gamelist.pop(0)

        # Add recursive call
        return game_to_games_recursive(origlist, gamelist, cache, counter + 1)


def game_to_games_iterative(gamelist: list) -> int:
    """
    Calculate amount of games played. This is the iterative version.
    :param gamelist:
    :return points:
    """
    # Create a cache
    cache = {}

    # Create a counter
    counter = 0

    # Loop over the games
    for game in gamelist:
        # Get the game id
        game_id, game_data = game.split(':')
        game_id = int(game_id.strip('Card '))

        # Check if the game id is in the cache
        if game_id in cache:
            # Add the games to the list
            gamelist += cache[game_id]
        else:
            # Calculate the points
            points = game_to_points(game)

            # Create a temp list
            temp = []

            # Add games according to the points
            for i in range(points):
                temp.append(gamelist[game_id + i])

            # Add the games to the cache
            cache[game_id] = temp

            # Add the games to the list
            gamelist += temp

        # Increase the counter
        counter += 1

    return counter

def main():
    """
    Main function.
    """
    # Read the file and get a list of the games
    start_games = file_to_list('input.txt')

    points = game_to_games_iterative(start_games)

    print(f"Points: {points}")


if __name__ == '__main__':
    main()
