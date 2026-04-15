# DDA line drawing algorithm
from matplotlib import pyplot as plt
def DDA(x0, y0, x1, y1):
    # find absolute differences
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    steps = max(dx, dy) #jeta  boro oita steps

    # calculate the increment in x and y
    xinc = dx/steps
    yinc = dy/steps
    # start with 1st point
    x = x0
    y= y0
    # make a list for coordinates
    x_new = []
    y_new = []
    for i in range(steps):
        x_new.append(x)
        y_new.append(y)
        # increment the values
        x = x + xinc
        y = y + yinc

    # plot the line with coordinates list
    plt.plot(x_new, y_new)
    plt.title("dda")
    plt.show()
DDA(20,40,60,50)


