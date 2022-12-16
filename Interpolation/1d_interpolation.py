from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

# For values of x and y
x = np.linspace(0, 10, num=10, endpoint=True)
y = [5, 3, 7, 10, 5, 7, 10, 10, 7, 8]

# Linear Interpolation
linear = interpolate.interp1d(x, y, kind="linear")

# Quadratic Interpolation
quadratic = interpolate.interp1d(x, y, kind="quadratic")

# Cubic Interpolation
cubic = interpolate.interp1d(x, y, kind="cubic")

# 100 new values of x
xnew = np.arange(0, 9, 0.1)

# Plotting and Displaying
plt.plot(x, y, 'o', x, linear(x), 'red', xnew, quadratic(xnew), 'b--', xnew, cubic(xnew), 'g--')
plt.legend(['data', 'linear', 'quadratic', 'cubic'])
plt.show()
