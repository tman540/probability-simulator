# Imports
import matplotlib.pyplot as plt
import numpy as np

title = ""
labels = []
data = []
x_label = ""
y_label = ""


def plox_x():
    index = np.arange(len(labels))
    plt.bar(index, data)
    plt.xlabel(x_label, fontsize=5)
    plt.ylabel(y_label, fontsize=5)
    plt.xticks(index, labels, fontsize=5, rotation=30)
    plt.title(title)
    plt.show()


def plox_y():
    index = np.arange(len(labels))
    plt.barh(index, data)
    plt.xlabel(x_label, fontsize=5)
    plt.ylabel(y_label, fontsize=5)
    plt.xticks(index, labels, fontsize=5, rotation=30)
    plt.title(title)
    plt.show()
