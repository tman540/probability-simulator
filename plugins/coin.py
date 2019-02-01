# Imports
from random import randint
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
import graphics.bar as graphics


class Plugin:
    # noinspection PyMethodMayBeStatic
    def main(self):
        print("Welcome to the coin flipping simulator!")
        # Infinite loop
        while True:
            # Catch exception if user enters letters or nothing
            try:
                times = input("How many coins do you want to flip?: ")
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
                bar = Bar('Flipping {} coin(s)...'.format(times), max=times,
                          suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
                # Define vars for possible options

                heads, tails = 0, 0
                # Loop for the amount of times
                for x in range(times):
                    # Random flip
                    flip = randint(0, 1)
                    # Check results
                    if flip == 0:
                        heads += 1
                    else:
                        tails += 1
                    # Progress bar next
                    bar.next()
                # Finish the progress bar
                bar.finish()
                # Output results
                table = PrettyTable(["Side", "Amount", "Percent"])
                # Define the rows
                rows = [["Heads", heads, f"%{round((heads / times * 100), 4)}"],
                        ["Tails", tails, f"%{round((tails / times * 100), 4)}"]]
                # Loop over the rows instead of calling `add_row()` multiple times
                # Allows for easy expandability
                for row in rows:
                    table.add_row(row)
                # Output the Table
                print(table)
                # Set the config vars for the table
                graphics.data = [heads, tails]
                graphics.labels = ["Heads", "Tails"]
                graphics.title = "Result of {} flipped coins".format(times)
                # Display a vertical bar graph
                print("Generating graph...")
                graphics.plox_x()
            except ValueError:
                print("Please only enter number")
            except ZeroDivisionError:
                print("You must flip at least 1 coin")
