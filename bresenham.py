import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    # Step-01: Calculate dx and dy
    dx = x1 - x0
    dy = y1 - y0

    # Step-02: Initial decision parameter
    p = 2 * dy - dx

    # Lists to store points
    x_new = []
    y_new = []

    # Starting point
    x, y = x0, y0
    # Step-04: Loop through dx times
    for i in range(dx):
        if p < 0:
            # Case-01
            x = x + 1
            p = p + 2 * dy
        else:
            # Case-02
            x = x + 1
            y = y + 1
            p = p + 2 * dy - 2 * dx

        x_new.append(x)
        y_new.append(y)
    plt.plot(x_new, y_new)
    plt.grid()
    plt.show()

# Input
x0, y0 = map(int, input("Enter starting point (x0 y0): ").split())
x1, y1 = map(int, input("Enter ending point (x1 y1): ").split())

# Get points
bresenham(x0,y0,x1,y1)
