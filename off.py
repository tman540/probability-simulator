# Display heatmap for a range of coordinates
# @python_programming_snippets

import matplotlib.pyplot as plt
from dataset import data


def heatmap(data):
    x, y = [], []

    for point in data:
        x.append(point[0])
        y.append(point[1])

    jet = plt.get_cmap('jet')

    plt.xlabel("x", fontsize=5)
    plt.ylabel("y", fontsize=5)
    plt.title("Heatmap of thrown darts")
    plt.gcf().canvas.set_window_title("Heatmap of thrown darts")
    plt.hist2d(x, y, bins=(30, 30), cmap=jet)
    plt.show()

heatmap(data)