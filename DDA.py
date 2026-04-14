# DDA line drawing algorithm
from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):

    # find absolute differences
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    count = max(dx, dy) #jeta  boro oita steps

    # calculate the increment in x and y
    xinc = dx/count
    yinc = dy/count

    # start with 1st point
    xp = float(x0)
    yp= float(y0)

    # make a list for coordinates
    x_new = []
    y_new = []

    for i in range(count+1):
        x_new.append(xp)
        y_new.append(yp)
        # increment the values
        xp = xp + xinc
        yp = yp + yinc

    # plot the line with coordinates list
    plt.plot(x_new, y_new)
    plt.show()

DDA(20,40,60,50)


