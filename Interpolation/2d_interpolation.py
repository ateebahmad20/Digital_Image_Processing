from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

# array containing values like [0.0,0.2,0.4....10]
x = np.arange(-5.01, 5.01, 0.5)
y = np.arange(-5.01, 5.01, 0.5)

# Creating MeshGrid
xx, yy = np.meshgrid(x, y)

# finding z using Cos
z = np.cos(xx*2+2*yy)

# 2d interpolating
f = interpolate.interp2d(x, y, z, kind="cubic")

# Creating new points
x_new = np.arange(-5.01, 5.01, 1e-2)
y_new = np.arange(-5.01, 5.01, 1e-2)
z_new = f(x_new, y_new)

# Plotting values
plt.plot(x, z[0, :], 'b--', x_new, z_new[0, :], 'r--')
plt.show()

