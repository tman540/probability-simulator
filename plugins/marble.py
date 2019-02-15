from random import choice
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
import graphics.bar as graphics
from collections import defaultdict


class Plugin:
    def main(self):
        marbles = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
        while True:
            try:
                times = input("How many marbles do you want to pull?: ")
                # Check if user entered `exit` or `quit` before converting to int
                # (So exception wouldn't trigger)
                if times == "exit" or times == "quit":
                    print("Exiting...")
                    # Exit the loop which quits the program
                    break
                else:
                    times = int(times)
                if times <= 0:
                    raise ZeroDivisionError
                # Create progress bar for counting flips
                bar = Bar('Pulling {} marble(s)...'.format(times), max=times,
                          suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')

                chosen_marbles = defaultdict(int)

                for x in range(times):
                    marble_from_bag = choice(marbles)
                    if marble_from_bag in chosen_marbles:
                        chosen_marbles[marble_from_bag] += 1
                    else:
                        chosen_marbles[marble_from_bag] = 1
                    # Progress bar next
                    bar.next()
                # Finish the progress bar
                bar.finish()
                # Output results
                table = PrettyTable(["Card", "Amount", "Percentage"])
                for marble in chosen_marbles:
                    # Loop over the rows instead of calling `add_row()` multiple times
                    # Allows for easy expandability
                    table.add_row(
                        [marble, chosen_marbles[marble], f"%{round((chosen_marbles[marble] / times * 100), 4)}"])

                # Output the table
                print(table)

                # Convert the dictionary into a list
                chosen_marbles_list = chosen_marbles.items()

                # Set the config vars for the table
                graphics.data = [i[1] for i in chosen_marbles_list]
                graphics.labels = [i[0] for i in chosen_marbles_list]
                graphics.title = "Result of {} pulled marble(s)".format(times)
                # Display a vertical bar graph
                print("Generating graph...")
                graphics.plot_x()

            except ValueError:
                print("Please only enter numbers")
            except ZeroDivisionError:
                print("You must pull at least 1 marble")
