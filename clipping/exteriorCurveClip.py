import numpy as np
import matplotlib.pyplot as plt
# Clipping window
xmin, xmax = -5, 5
ymin, ymax = -5, 5

# Generate curve (parabola)
x = np.linspace(-10, 10, 400)
y = x**2 / 5

# Separate inside and outside points
x_in, y_in = [], []
x_out, y_out = [], []

for xi, yi in zip(x, y):
    if xmin> xi or xi> xmax or ymin>yi or yi> ymax:
        x_in.append(xi)
        y_in.append(yi)
    else:
        x_out.append(xi)
        y_out.append(yi)

# Plot
plt.figure()
plt.title("exterior Curve Clipping (Parabola)")
# Clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'k-')
plt.plot(x_out, y_out, 'r--')
plt.plot(x_in, y_in, 'g')
plt.show()