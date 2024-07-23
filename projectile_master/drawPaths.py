import point
import numpy as np

import matplotlib.pyplot as plt

class drawPaths:
    
    def __init__(self, path, projected, mx, my):
        self.paths = [path, projected]  # Initialize paths list with given path and projected path
        self.maxX = mx  # Store maximum X value
        self.maxY = my  # Store maximum Y value

    def addList(self, points):
        self.paths.append(points)  # Add additional points to the paths list
        
    def draw(self):
        x1 = []  # Initialize empty list for x-coordinates of path 1
        y1 = []  # Initialize empty list for y-coordinates of path 1
        x2 = []  # Initialize empty list for x-coordinates of path 2
        y2 = []  # Initialize empty list for y-coordinates of path 2
        
        for p in self.paths[0]:  # Iterate over points in path 1
            x1.append(p.x)  # Add x-coordinate of each point to x1 list
            y1.append(self.maxY - p.y)  # Add (maxY - y-coordinate) of each point to y1 list
            
        for p in self.paths[1]:  # Iterate over points in path 2
            x2.append(p.x)  # Add x-coordinate of each point to x2 list
            y2.append(self.maxY - p.y)  # Add (maxY - y-coordinate) of each point to y2 list

        plt.figure(1)  # Create a new figure
        plt.subplot(211)  # Create a subplot with 2 rows, 1 column, and index 1
        plt.plot(x1, y1)  # Plot path 1
        plt.plot(x2, y2)  # Plot path 2
        plt.show()  # Display the plot
