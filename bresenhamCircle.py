import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    x = 0
    y = r

    # Initial decision parameter
    p = 3 - 2 * r

    x_new, y_new = [], []
    # Function for 8-way symmetry
    def plot_points(xc, yc, x, y):
        x_new.extend([xc + x, xc - x, xc + x, xc - x,
                      xc + y, xc - y, xc + y, xc - y])
        y_new.extend([yc + y, yc + y, yc - y, yc - y,
                      yc + x, yc + x, yc - x, yc - x])

    plot_points(xc, yc, x, y)
    # Loop
    while x < y:
        if p < 0:
            x += 1
            p = p + 4 * x + 6
        else:
            x += 1
            y -= 1
            p= p + 4 * (x - y) + 10
        plot_points(xc, yc, x, y)
    return x_new, y_new

# Input
x, y = bresenham_circle(10,15,7)
# Plot
plt.scatter(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.show()