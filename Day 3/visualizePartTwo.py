import curses
import time
from partOne_missingPart import file_to_list, list_of_strings_to_list_of_lists


def visualize(stdscr, list_of_lists):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    for i, row in enumerate(list_of_lists):
        for j, char in enumerate(row):
            stdscr.addstr(i, j, char)

    stdscr.refresh()

    for idl, lst in enumerate(list_of_lists):
        for idc, char in enumerate(lst):
            stdscr.addstr(idl, idc, char, curses.A_REVERSE)
            stdscr.refresh()
            time.sleep(0.1)  # Delay to visualize the cursor movement
            stdscr.addstr(idl, idc, char, curses.A_NORMAL)

            # Here you can add more logic to highlight numbers, symbols, etc.
            # And to display messages at the bottom of the screen

    stdscr.getch()


def main():
    list_of_strings = file_to_list("vparts.txt")
    list_of_lists = list_of_strings_to_list_of_lists(list_of_strings)

    curses.wrapper(visualize, list_of_lists)


if __name__ == "__main__":
    main()
