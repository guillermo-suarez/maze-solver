import matplotlib
import genlab

import matplotlib.pyplot as plt
import numpy as np

from genlab import printMaze, maze

print(matplotlib.__version__)

printMaze(maze)

x_verde = np.array(None)
y_verde = np.array(None)
x_rojo = np.array(None)
y_rojo = np.array(None)
x_azul = np.array(None)
y_azul = np.array(None)

for y in range(0, 10):
    for x in range(0, 10):
        if (maze[y][x] == '0'):
            x_verde = np.append(x_verde, x + 1)
            y_verde = np.append(y_verde, y + 1)
        elif (maze[y][x] == 'x'):
            x_rojo = np.append(x_rojo, x + 1)
            y_rojo = np.append(y_rojo, y + 1)
        else:
            x_azul = np.append(x_azul, x + 1)
            y_azul = np.append(y_azul, y + 1)
        
plt.scatter(x_verde, y_verde, color = 'green')
# plt.scatter(x_rojo, y_rojo, color = 'red')
plt.scatter(x_azul, y_azul, color = 'blue')

plt.gca().invert_yaxis()

plt.title("Laberinto")

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)

plt.show()