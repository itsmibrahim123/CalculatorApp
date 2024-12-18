import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

Z = np.sqrt((X**2 + Y**2) - 1)
