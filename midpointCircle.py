import matplotlib.pyplot as plt
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    x_new = []
    y_new = []

    # Function to store all 8 symmetric points
    def points(xc, yc, x, y):
        x_new.extend([xc + x, xc - x, xc + x, xc - x,
                         xc + y, xc - y, xc + y, xc - y])
        y_new.extend([yc + y, yc + y, yc - y, yc - y,
                         yc + x, yc + x, yc - x, yc - x])
    # Initial points
    points(xc, yc, x, y)

    # Loop
    while x < y:
        if p < 0:
            x += 1
            p = p + 2 * x + 1
        else:
            x += 1
            y -= 1
            p = p + 2 * x - 2 * y + 1
        points(xc, yc, x, y)

    return x_new, y_new

# Input
x,y=midpoint_circle(10,20,10)
# Plot
plt.scatter(x, y)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.show()