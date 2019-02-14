# Imports
from random import choice
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
import graphics.bar as graphics
from graphics.density import heatmap


# noinspection PyMethodMayBeStatic
class Plugin:
    def main(self):
        print("Welcome to the basic dart throwing simulator!")
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

                # Initialize vars
                center, non_center = 0, 0
                accuracy = []
                center_accuracy = []
                coords = []

                for time in range(times):
                    # Initialize vars that change every iteration
                    is_center = False
                    x, y = 4, 4
                    inst = [0, 0, 0, 0, 1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, -2, -2, -2, 3, 3, -3, -3,  4, 4, -4, -4, 5, -5]
                    # add some instability to each coord
                    x += choice(inst)
                    y += choice(inst)
                    # add the current coord to the list of coords
                    coords.append((x, y))
                    # Check if it is in the center in the x coord
                    if 3 <= x <= 7:
                        # Check in the y
                        if 3 <= y <= 7:
                            # add one to the center counter
                            center += 1
                            is_center = True
                        else:
                            # Add one to the non center counter
                            non_center += 1
                    else:
                        non_center += 1
                    # calculate the difference between the center and its actual location (always positive)
                    accuracy_x = abs(x-4)
                    accuracy_y = abs(y-4)
                    # Calculate the final average accuracy
                    total_accuracy = (accuracy_x + accuracy_y)/2
                    # Check if it is in the center
                    if is_center:
                        # add it the center accuracy list
                        center_accuracy.append(total_accuracy)
                        # Reset the center var
                        is_center = False
                    else:
                        # add it the non-center accuracy list
                        accuracy.append(total_accuracy)
                    # Continue the bar
                    bar.next()
                # Finish the bar after the list
                bar.finish()
                # Initialize table
                table = PrettyTable(["Position", "Amount", "Percentage", "AVG Inaccuracy"])

                # Initialize vars
                total_center = 0
                total_outer = 0
                # create total count
                for item in center_accuracy:
                    total_center += item
                for item in accuracy:
                    total_outer += item

                # get difference
                total_center /= len(center_accuracy)
                total_outer /= len(accuracy)

                # Create rows for table
                rows = [["Bullseye", center, f"%{round((center / times * 100), 4)}", round(total_center, 4)],
                        ["Outer Ring", non_center, f"%{round((non_center / times * 100), 4)}", round(total_outer, 4)]]
                # Iterate over all rows
                for row in rows:
                    # add it to the table
                    table.add_row(row)
                # Output the table
                print(table)

                # Define data for the bar graph
                graphics.data = [center, non_center]
                # Define the labels for the axes
                graphics.labels = ["Bullseye", "Outer Ring"]
                # Define the title for the graph
                graphics.title = "Result of {} thrown darts".format(times)
                # Display a vertical bar graph
                print("Generating graph...")
                graphics.plox_x()
                # Generate a heatmap with the list of coords as an argument
                heatmap(coords)

            except ValueError:
                print("Please only enter number")
            except ZeroDivisionError:
                print("You must throw at least 1 dart")
