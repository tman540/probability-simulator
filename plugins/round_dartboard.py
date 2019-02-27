# Imports
from random import randint
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
import graphics.bar as graphics
from colorama import init, Fore, Style

# Initialize colorama
init()

# Title string
title = Fore.MAGENTA + """
______           _   _                         _   _____ _                 _       _
|  _  \         | | | |                       | | /  ___(_)               | |     | |
| | | |__ _ _ __| |_| |__   ___   __ _ _ __ __| | \ `--. _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
| | | / _` | '__| __| '_ \ / _ \ / _` | '__/ _` |  `--. \ | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |/ / (_| | |  | |_| |_) | (_) | (_| | | | (_| | /\__/ / | | | | | | |_| | | (_| | || (_) | |
|___/ \__,_|_|   \__|_.__/ \___/ \__,_|_|  \__,_| \____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|
""" + Style.RESET_ALL

# Define vars for printing the board
R = Fore.RED + "◼" + Style.RESET_ALL
Y = Fore.YELLOW + "◼" + Style.RESET_ALL
B = Fore.BLUE + "◼" + Style.RESET_ALL

# noinspection PyMethodMayBeStatic
# DARTBOARD
test_list = [
            [" ", " ", B, B, B, B, B, B, " ", " "],
            [" ", B, B, B, B, B, B, B, B, " "],
            [B, B, Y, Y, Y, Y, Y, Y, B, B],
            [B, B, Y, Y, Y, Y, Y, Y, B, B],
            [B, B, Y, Y, R, R, Y, Y, B, B],
            [B, B, Y, Y, R, R, Y, Y, B, B],
            [B, B, Y, Y, Y, Y, Y, Y, B, B],
            [B, B, Y, Y, Y, Y, Y, Y, B, B],
            [" ", B, B, B, B, B, B, B, B, " "],
            [" ", " ", B, B, B, B, B, B, " ", " "]
            ]


class Plugin:
    def main(self):

        # Print the title
        print(title)
        # Print the dartboard
        for row in test_list:
            for item in row:
                print(item, end="")
            print("\n", end="")
        print("\n", end="")
        while True:
            try:
                # Ask user for throw amount
                times = input("How many darts do you want to throw?: ")
                # Check if user entered exit or quit
                if times == "exit" or times == "quit":
                    print("Exiting...")
                    break
                else:
                    times = int(times)
                # Check if user entered something below zero
                if times <= 0:
                    raise ZeroDivisionError
                # Initialize loading bar
                bar = Bar('Throwing {} dart(s)...'.format(times), max=times,
                          suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')

                # Define the coords for each location

                miss_coords = [(1, 1), (2, 1), (9, 1), (10, 1), (1, 2), (10, 2), (1, 9), (1, 10), (2, 10), (9, 10), (10, 10)]
                outer_ring_coords = [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
                              (2, 2), (3, 2), (3, 8), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2),
                              (1, 3), (2, 3), (9, 3), (10, 3),
                              (1, 4), (2, 4), (3, 3), (8, 3), (9, 4), (10, 4),
                              (1, 5), (2, 5), (9, 5), (10, 5),
                              (1, 6), (2, 6), (9, 6), (10, 6),
                              (1, 7), (2, 7), (9, 7), (10, 7),
                              (1, 8), (2, 8), (9, 8), (10, 8),
                              (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9),
                              (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 8), (8, 10)
                              ]
                inner_ring_coords = [(4, 3), (5, 3), (6, 3), (7, 3),
                                     (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                                     (3, 5), (4, 5), (7, 5), (8, 5),
                                     (3, 6), (4, 6), (7, 6), (8, 6),
                                     (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                                     (4, 8), (5, 8), (6, 8), (7, 8)]
                center_coords = [(5, 5), (5, 6), (6, 5), (6, 6)]

                # Create empty lists for the hits
                miss, outer, inner, center = [], [], [], []

                # Loop
                for time in range(times):
                    x = randint(1, 10)
                    y = randint(1, 10)

                    # Check the locations of the coords
                    if (x, y) in miss_coords:
                        # Add it to the list
                        miss.append((x, y))
                    elif (x, y) in outer_ring_coords:
                        outer.append((x, y))
                    elif (x, y) in inner_ring_coords:
                        inner.append((x, y))
                    else:
                        center.append((x, y))
                    bar.next()
                bar.finish()
                # Create the table with headers
                table = PrettyTable(["Location", "Amount", "Percentage"])

                # Define the rows for the table
                rows = [["Miss", len(miss), f"%{round((len(miss) / times * 100), 4)}"],
                        ["Outer Ring", len(outer), f"%{round((len(outer) / times * 100), 4)}"],
                        ["Inner Ring", len(inner), f"%{round((len(inner) / times * 100), 4)}"],
                        ["Bullseye", len(center), f"%{round((len(center) / times * 100), 4)}"]]

                # Iterate over all the rows
                for row in rows:
                    # add it to the table
                    table.add_row(row)
                # Output the table
                print(table)

                # Data to populate the graph
                graphics.data = [len(miss), len(outer), len(inner), len(center)]
                # Define the labels for the axes
                graphics.labels = ["Miss", "Outer Ring", "Inner Ring", "Bullseye"]
                # Define the title for the graph
                graphics.title = "Result of {} thrown dart(s)".format(times)
                # Display a vertical bar graph
                print("Generating graph...")
                graphics.plot_x()

            except ValueError:
                print("Please only enter numbers")
            except ZeroDivisionError:
                print("You must throw at least 1 dart")
