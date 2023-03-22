import tkinter
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

import genlab

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

from genlab import printMaze, maze

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#printMaze(maze)