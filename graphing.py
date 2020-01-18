#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Matplotlib-Demo-Graph - A simple demo graph used with python code                                                   #
# Copyright (C) 2019 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Plotting data with matplotlib while creating a simple graph

from matplotlib import pylab as plt

# - X-Axis is the age of a developer. Y-Axis is the money earned in a year in US Dollars.
dev_x_axis = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
dev_y_axis = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232, 78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# - X-Axis is the age of a Python developer. Y-Axis is the money earned in a year in US Dollars
py_dev_x_axis = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
py_dev_y_axis = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# - X-Axis is the age of a Javascript developer. Y-Axis is the money earned in a year in US Dollars
js_dev_x_axis = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
js_dev_y_axis = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000, 78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

# - Plotting Python data inside the graph (You can also add markers too)
plt.plot(py_dev_x_axis, py_dev_y_axis, color="#3470a2", linestyle="-", linewidth=3, label="Python developers")
# - Plotting Javascript data inside the graph (You can also add markers too)
plt.plot(js_dev_x_axis, js_dev_y_axis, color="#f0db4f", linestyle="-", linewidth=3, label="Javascript developers")
# - Plotting developer data inside the graph (You can also add markers too)
plt.plot(dev_x_axis, dev_y_axis, color="#585858", linestyle="--", linewidth=3, label="Other developers")

# - Putting info inside the graph to tell users what our data is
plt.title(" Average Salary (USD) for a developer by age")
plt.xlabel("Age Range")
plt.ylabel("Median Salary")

# - Creating a legend in the graph
plt.legend()

# - Adding a grid inside the graph
plt.grid(True)

# - Fix some of the padding issues on smaller screens
plt.tight_layout()

"""
# - Save the file to a png when ran
plt.savefig("graphing.png")
"""

# - Using a theme inside the plot
plt.style.use("seaborn-dark")

# - Making the graph show when the Python file is run
plt.show()
