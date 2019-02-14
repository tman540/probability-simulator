# Imports
import matplotlib.pyplot as plt
import numpy as np

# Initials vars
title = ""
labels = []
data = []
x_label = ""
y_label = ""


# Function for vertical bar graphs
def plox_x():
    # Create an array from length of labels
    index = np.arange(len(labels))
    # Define the bar
    plt.bar(index, data)
    # Define the labels for the axes
    plt.xlabel(x_label, fontsize=5)
    plt.ylabel(y_label, fontsize=5)
    # Define the intervals for the graph
    plt.xticks(index, labels, fontsize=5, rotation=30)
    # Set the title and window title for the graph
    plt.title(title)
    plt.gcf().canvas.set_window_title(title)
    # Show the graph
    plt.show()
    # todo: Return plot for saving command in shell


# Function for horizontal bar graphs
def plox_y():
    # Create an array from length of labels
    index = np.arange(len(labels))
    # Define the bar
    plt.barh(index, data)
    # Define the labels for the axes
    plt.xlabel(x_label, fontsize=5)
    plt.ylabel(y_label, fontsize=5)
    # Define the intervals for the graph
    plt.xticks(index, labels, fontsize=5, rotation=30)
    # Set the title and window title for the graph
    plt.title(title)
    plt.gcf().canvas.set_window_title(title)
    # Show the graph
    plt.show()
    # todo: Return plot for saving command in shell
