# Probability Simulator

![](https://img.shields.io/github/package-json/v/tman540/probability-simulator/master.svg?style=flat)

## Installation
1. Download the source code [here](https://github.com/tman540/probability-simulator)
2. cd into the directory
3. run `pip3 install -r requirements.txt`
4. run `python main.py`

## Important notes:
#### Heatmap:
* The heatmap uses the `jet` color mapping.
* The jet color mapping goes as follows:

![jet colormap](img/jet colormap.jpg)

* Red is where there are the most values
* Green is medium
* Blue is where the least are

When the dartboard simulation is run, if there are sufficient values, the pattern should be shaped like a square dartboard, red by the bullseye, green around it, and blue near the outside.

#### Marbles:
When a bar graph is generated for the marble simulator, all of the bars 
are the same color. The location of the bars/colors are also different
every run (this is because of the randomization). Make sure to read the
labels to ensure that you are analyzing the data properly.