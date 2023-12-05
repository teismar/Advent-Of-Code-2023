"""
This is the solution for the second part problem of Advent of Code 2023 day 5.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-05
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


def input_list_to_list_of_lists(input_list: list) -> list:
    """
    Split the list of lines into a list of lists.
    :param input_list:
    :return:
    """
    split_data = []
    temp = []

    for item in input_list:
        if item == '':
            split_data.append(temp)
            temp = []
        else:
            temp.append(item)

    if temp:
        split_data.append(temp)

    return split_data


def list_to_map(lists: list) -> dict:
    """
    Read the list of lines and return a dictionary with the maps as hashmaps.
    :param lines:
    :return:
    """
    maps = {}
    for list in lists:
        # Check if the first line is the seeds
        if list[0].startswith('seeds:'):
            # Split the seeds and add them to the map
            seeds = list[0].split(':')[1].split()
            # Make the seeds integers
            seeds = [int(seed) for seed in seeds]
            # Split in pairs of two
            seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
            # Calculate the seeds based on the pairs as range
            new_seeds = []
            for seed in seeds:
                new_seeds.append(range(seed[0], seed[0] + seed[1] + 1))
            maps['seeds'] = new_seeds
        else:
            # Make a new map of source to destination
            key = list[0].split(' ')[0].strip()
            this_list = []
            for item in list[1:]:
                split_item = item.split(' ')
                thisrange = int(split_item[2])
                thissource = int(split_item[1])
                thisdest = int(split_item[0])
                this_list.append({'range': thisrange, 'source': thissource, 'dest': thisdest})

            maps[key] = this_list

    return maps


def get_value_from_map(key: int, map_name: str, maps: dict) -> int:
    """
    Get the value of a key from a map. Handle if the key is not in the map.
    :param key:
    :param maps:
    :return:
    """
    map = maps[map_name]
    value = key
    for item in map:
        if item['source'] <= key <= item['source'] + item['range']:
            value = item['dest'] + (key - item['source'])
            break

    return value


def get_location_of_seed(seed: int, maps: dict) -> int:
    """
    Get the location of a seed.
    :param seed:
    :param maps:
    :return:
    """
    # Get the soil of the seed
    soil = get_value_from_map(seed, 'seed-to-soil', maps)

    # Get the fertilizer of the soil
    fertilizer = get_value_from_map(soil, 'soil-to-fertilizer', maps)

    # Get the water of the fertilizer
    water = get_value_from_map(fertilizer, 'fertilizer-to-water', maps)

    # Get the light of the water
    light = get_value_from_map(water, 'water-to-light', maps)

    # Get the temperature of the light
    temperature = get_value_from_map(light, 'light-to-temperature', maps)

    # Get the humidity of the temperature
    humidity = get_value_from_map(temperature, 'temperature-to-humidity', maps)

    # Get the location of the humidity
    location = get_value_from_map(humidity, 'humidity-to-location', maps)

    return location


def main():
    """
    Main function.
    """
    # Start Time
    import time
    start_time = time.time()
    # Read the maps and get a list of the lines
    maps = file_to_list('maps.txt')
    splitted_maps = input_list_to_list_of_lists(maps)
    hashmap = list_to_map(splitted_maps)

    # Read the seeds and get a list of the seeds
    seeds = hashmap['seeds']

    # Check if there are seeds in the list
    if seeds:
        # Initialize loc with the location of the first seed
        loc = None

        # Loop over List or range of seeds
        for seed in seeds:
            # loop over the range of the seed
            for seed_value in seed:
                location = get_location_of_seed(seed_value, hashmap)
                if loc is None:
                    loc = location
                if location < loc:
                    loc = location
    else:
        # Handle the case where there are no seeds
        loc = "No seeds found."

    # Print the result
    took = time.time() - start_time
    print(f"Took {took} seconds to run.")
    print(f"Thats {took / 60} minutes.")
    print(f"Thats {took / 60 / 60} hours.")

    print(f'The lowest location is {loc}')


if __name__ == '__main__':
    main()
