from random import randint


class Plugin:
    # noinspection PyMethodMayBeStatic
    def main(self):
        center = 0
        non_center = 0

        runs = 10000

        for run in range(runs):
            x = randint(0, 10)
            y = randint(0, 10)
            if x > 3 and x < 7:
                if y > 3 and y < 7:
                    center += 1
                else:
                    non_center += 1
            else:
                non_center += 1

        print(f"Center hits: {center}, non center: {non_center}")
        print(f"Center percent: %{(center/runs)*100}, non center: %{(non_center/runs)*100}")
