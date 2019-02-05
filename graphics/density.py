import matplotlib.pyplot as plt


def heatmap(data):
    # Define separate lists for x and y
    x, y = [], []

    # Separate the x and the y
    for point in data:
        x.append(point[0])
        y.append(point[1])

    # Define the color map
    jet = plt.get_cmap('jet')

    # Set the x and the y label
    plt.xlabel("x", fontsize=5)
    plt.ylabel("y", fontsize=5)
    # Set the title and the window title of the graph
    plt.title("Heatmap of thrown darts")
    plt.gcf().canvas.set_window_title("Heatmap of thrown darts")
    # Define the 2d histogram using the the x,y as arguments.
    # THe bins are the size blocks, cmap is the color mapping
    plt.hist2d(x, y, bins=(10, 10), cmap=jet)
    # Display the graph
    plt.show()
    # todo: Return plot for saving command in shell
