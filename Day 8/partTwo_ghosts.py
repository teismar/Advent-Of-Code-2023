"""
This is the solution for the second part problem of Advent of Code 2023 day 8.
author: Tim Eismar
github: https://github.com/teismar
date: 2023-12-08
"""

from partOne_network import file_to_list, inputList_to_list_and_dict


def find_starting_poinzs(nodes: dict) -> list:
    """
    Find the starting points of the network.
    :param nodes:
    :return:
    """
    starting_points = []
    for node in nodes:
        if node[-1] == 'A':
            starting_points.append(node)
    return starting_points


def walk_tree(instructions: list, nodes: dict, start: str) -> (str, list):
    """
    Walk the tree and return the value we end up with.
    :param instructions:
    :param nodes:
    :param start:
    :return:
    """
    current = start
    for instruction in instructions:
        # Add the current node to the step_list.
        if instruction == "L":
            current = nodes[current][0]
        elif instruction == "R":
            current = nodes[current][1]
        else:
            print("Error")
    return current


def z_in_all(currents: list) -> bool:
    """
    Check if all currents contain a Z.
    :param currents:
    :return:
    """
    for current in currents:
        # Check if the last letter is a Z.
        if current[-1] != "Z":
            return False
    return True


def get_list_of_z_its(instructions: list, nodes: dict, start: str, limit: int) -> (list, str):
    """
    Get the list iteration where we find the Z.
    :param instructions:
    :param nodes:
    :param start:
    :return:
    """
    iter_list = []
    current = start
    for i in range(limit):
        current = walk_tree(instructions, nodes, current)
        if current[-1] == "Z":
            iter_list.append(i)
    return iter_list, current


def find_cm(a: list, b: list) -> list:
    """
    Find the cm's of two lists.
    :param a:
    :param b:
    :return:
    """
    returnlist = []
    for i in a:
        if i in b:
            returnlist.append(i)
    return returnlist


def find_lcm_of_lists(lists: list) -> list:
    """
    Find the lcm of a list of lists.
    :param lists:
    :return:
    """
    # Find the lcm of the first two lists.
    cm = find_cm(lists[0], lists[1])
    # Loop through the rest of the lists.
    if len(lists) == 2:
        return cm
    for i in range(2, len(lists)):
        cm = find_cm(cm, lists[i])
    return cm

def finde_gemeinsamen_punkt_effizient(tupel_liste):
    # Sortiere die Tupel nach dem Startwert 'a', beginne mit dem größten
    tupel_liste.sort(key=lambda x: -x[0])
    print(tupel_liste)

    # Starte die Suche beim größten Startwert
    punkt = tupel_liste[0][0]
    while True:
        # Überprüfe, ob der aktuelle Punkt in allen anderen Sequenzen gültig ist
        if all((punkt - a) % b == 0 for a, b in tupel_liste):
            return punkt  # Der erste gemeinsame Punkt

        # Finde den nächsten Punkt, der potentiell für alle Sequenzen gültig sein könnte
        # Dies wird erreicht, indem der aktuelle Punkt um das kleinste Vielfache von 'b'
        # erhöht wird, das größer als der aktuelle Punkt ist
        punkt = max(punkt + b - (punkt - a) % b for a, b in tupel_liste)

def find_path(instructions: list, nodes: dict, start_nodes: list) -> int:
    """
    Find the path from start to end.
    :param instructions:
    :param nodes:
    :param start:
    :return:
    """
    result_list = []
    offset = 0
    for start in start_nodes:
        iter_list, current = get_list_of_z_its(instructions, nodes, start, 10000)
        # Create the start entry in the result_dict.
        result_list.append((start, iter_list, current))
    offset = 10000
    lcm = find_lcm_of_lists([i[1] for i in result_list])
    if lcm == []:
        cycle_list = []
        while lcm == []:
            # Check if we have a cycle
            popcounter = 0
            for i in range(len(result_list)):
                # Check if we have a cycle.
                cycle_can = result_list[i][1][-1] - result_list[i][1][-2]
                cycle_can_two = result_list[i][1][-5] - result_list[i][1][-6]
                if cycle_can == cycle_can_two:
                    cycle_list.append((result_list[i][1][-1], cycle_can))
                    print("Cycle found")
                    # Remove from the result_list.
                    popcounter += 1
            for i in range(popcounter):
                result_list.pop()

            if len(cycle_list) == len(start_nodes):
                print("All are cycles")
                print(cycle_list)


                print(lcm)
                print(lcm + 1)
                print((lcm + 1) * len(start_nodes))
                return lcm

            for i in range(len(result_list)):
                iter_list, current = get_list_of_z_its(instructions, nodes, result_list[i][2], 10000)
                for j in range(len(iter_list)):
                    iter_list[j] += offset
                result_list[i] = (result_list[i][0], result_list[i][1] + iter_list, current)

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple of a and b."""
    return a * b // gcd(a, b)

def lcm_list(numbers):
    """Compute the LCM of a list of numbers."""
    current_lcm = 1
    for number in numbers:
        current_lcm = lcm(current_lcm, number)
    return current_lcm

def deniz(instructions: list, nodes: dict, start_nodes: list) -> int:
    """
    Find the path from start to end.
    :param instructions:
    :param nodes:
    :param start_nodes:
    :return:
    """
    result_list = []
    for start in start_nodes:
        iter_list, current = get_list_of_z_its(instructions, nodes, start, 10000)
        # Create the start entry in the result_dict.
        result_list.append((start, iter_list, current))

    firsts = [(i[1][0]+1)*len(instructions) for i in result_list]
    print(firsts)
    lcm = lcm_list(firsts)
    print(lcm)



    return 1



    print(lcm)
    lcm = lcm[0]
    lcm += 1
    lcm = lcm * len(start_nodes)
    print(lcm)

    return 1


def main():
    """
    Main function.
    """
    content = file_to_list("ghost.txt")
    instructions, nodes = inputList_to_list_and_dict(content)
    starting_points = find_starting_poinzs(nodes)
    den = deniz(instructions, nodes, starting_points)
    # find_path(instructions, nodes, starting_points)


if __name__ == "__main__":
    main()
