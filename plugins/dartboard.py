from random import randint
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
import graphics.bar as graphics


# noinspection PyMethodMayBeStatic
class Plugin:
    def main(self):
        print("Welcome to the basic dart throwing simulator!")
        while True:
            try:
                times = input("How many darts do you want to throw?: ")
                if times == "exit" or times == "quit":
                    print("Exiting...")
                    break
                else:
                    times = int(times)
                if times <= 0:
                    raise ZeroDivisionError
                bar = Bar('Throwing {} dart(s)...'.format(times), max=times,
                          suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')

                center, non_center = 0, 0
                accuracy = []
                center_accuracy = []

                for time in range(times):
                    is_center = False
                    x, y = randint(0, 10), randint(0, 10)
                    if 3 <= x <= 7:
                        if 3 <= y <= 7:
                            center += 1
                            is_center = True
                        else:
                            non_center += 1
                    else:
                        non_center += 1
                    accuracy_x = abs(x-5)
                    accuracy_y = abs(y-5)
                    total_accuracy = (accuracy_x + accuracy_y)/2
                    if is_center:
                        center_accuracy.append(total_accuracy)
                        is_center = False
                    else:
                        accuracy.append(total_accuracy)
                    bar.next()
                bar.finish()
                table = PrettyTable(["Position", "Amount", "Percentage", "AVG Inaccuracy"])

                total_center = 0
                total_outer = 0
                for item in center_accuracy:
                    total_center += item
                for item in accuracy:
                    total_outer += item

                total_center /= len(center_accuracy)
                total_outer /= len(accuracy)

                rows = [["Bullseye", center, f"%{round((center / times * 100), 4)}", round(total_center, 4)],
                        ["Outer Ring", non_center, f"%{round((non_center / times * 100), 4)}", round(total_outer, 4)]]
                for row in rows:
                    table.add_row(row)
                print(table)

                graphics.data = [center, non_center]
                graphics.labels = ["Bullseye", "Outer Ring"]
                graphics.title = "Result of {} thrown darts".format(times)
                # Display a vertical bar graph
                print("Generating graph...")
                graphics.plox_x()

            except ValueError:
                print("Please only enter number")
            except ZeroDivisionError:
                print("You must throw at least 1 dart")
