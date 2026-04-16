# # DDA line drawing algorithm
# from matplotlib import pyplot as plt
# def DDA(x0, y0, x1, y1):
#     # find absolute differences
#     dx = abs(x0 - x1)
#     dy = abs(y0 - y1)
#     steps = max(dx, dy) #jeta  boro oita steps
#
#     # calculate the increment in x and y
#     xinc = dx/steps
#     yinc = dy/steps
#     # start with 1st point
#     x = x0
#     y= y0
#     # make a list for coordinates
#     x_new = []
#     y_new = []
#     for i in range(steps):
#         x_new.append(x)
#         y_new.append(y)
#         # increment the values
#         x = x + xinc
#         y = y + yinc
#
#     # plot the line with coordinates list
#     plt.plot(x_new, y_new)
#     plt.title("dda")
#     plt.show()
# DDA(20,40,60,50)
from nbformat.sign import algorithms

#bresenham line drawing algorithms
# import matplotlib.pyplot as plt
# def bresenham(x0, y0, x1, y1):
#     # Step-01: Calculate dx and dy
#     dx = x1 - x0
#     dy = y1 - y0
#     p = 2 * dy - dx # Step-02: Initial decision parameter
#     x_new ,y_new = [],[] # Lists to store points
#
#     # Starting point
#     x, y = x0, y0
#     # Step-04: Loop through dx times
#     for i in range(dx):
#         if p < 0:
#             # Case-01
#             x = x + 1
#             p = p + 2 * dy
#         else:
#             # Case-02
#             x = x + 1
#             y = y + 1
#             p = p + 2 * dy - 2 * dx
#
#         x_new.append(x)
#         y_new.append(y)
#     plt.plot(x_new, y_new)
#     plt.grid()
#     plt.show()
#
#
# # Input
# x0, y0 = map(int, input("Enter starting point (x0 y0): ").split())
# x1, y1 = map(int, input("Enter ending point (x1 y1): ").split())
# bresenham(x0,y0,x1,y1)

#mid point circle
# import matplotlib.pyplot as plt
# def midpoint_circle(xc, yc, r):
#     x = 0
#     y = r
#     p = 1 - r
#
#     x_new = []
#     y_new = []
#
#     # Function to store all 8 symmetric points
#     def points(xc, yc, x, y):
#         x_new.extend([xc + x, xc - x, xc + x, xc - x,
#                       xc + y, xc - y, xc + y, xc - y])
#         y_new.extend([yc + y, yc + y, yc - y, yc - y,
#                       yc + x, yc + x, yc - x, yc - x])
#     points(xc, yc, x, y) #call
#     # Loop
#     while x < y:
#         if p < 0:
#             x += 1
#             p = p + 2 * x + 1
#         else:
#             x += 1
#             y -= 1
#             p = p + 2 * x + 1 - 2 * y
#         points(xc, yc, x, y)
#     return x_new, y_new
#
# # Input
# x,y=midpoint_circle(10,20,10)
# plt.scatter(x, y)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()

#bresenham circle
# import matplotlib.pyplot as plt
# def bresenham_circle(xc, yc, r):
#     x = 0
#     y = r
#     p = 3 - 2 * r     # decision parameter=p
#
#     x_new, y_new = [], []
#     # Function for 8-way symmetry
#     def plot_points(xc, yc, x, y):
#         x_new.extend([xc + x, xc - x, xc + x, xc - x,
#                       xc + y, xc - y, xc + y, xc - y])
#         y_new.extend([yc + y, yc + y, yc - y, yc - y,
#                       yc + x, yc + x, yc - x, yc - x])
#
#     plot_points(xc, yc, x, y)
#     # Loop
#     while x < y:
#         if p < 0:
#             x += 1
#             p = p + 4 * x + 6
#         else:
#             x += 1
#             y -= 1
#             p= p + 4 * (x - y) + 10
#         plot_points(xc, yc, x, y)
#     return x_new, y_new
#
# # Input
# x, y = bresenham_circle(10,15,7)
# # Plot
# plt.scatter(x, y)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.title("Bresenham Circle Drawing Algorithm")
# plt.show()

# # curve clipping
# import numpy as np
# import matplotlib.pyplot as plt
# # Clipping window
# xmin, xmax = -5, 5
# ymin, ymax = -5, 5
#
# # Generate curve (parabola)
# x = np.linspace(-10, 10, 400)
# y = x**2 / 5
#
# # Separate inside and outside points
# x_in, y_in = [], []
# x_out, y_out = [], []
#
# for xi, yi in zip(x, y):
#     if xmin <= xi <= xmax and ymin <= yi <= ymax:
#         x_in.append(xi)
#         y_in.append(yi)
#     else:
#         x_out.append(xi)
#         y_out.append(yi)
#
# # Plot
# plt.figure()
# plt.title("Curve Clipping (Parabola)")
# # Clipping window
# plt.plot([xmin, xmax, xmax, xmin, xmin],
#          [ymin, ymin, ymax, ymax, ymin], 'k-')
# plt.plot(x_out, y_out, 'r--')
# plt.plot(x_in, y_in, 'g')
# plt.show()

#exterior curve
# import numpy as np
# import matplotlib.pyplot as plt
# # Clipping window
# xmin, xmax = -5, 5
# ymin, ymax = -5, 5
#
# # Generate curve (parabola)
# x = np.linspace(-10, 10, 400)
# y = x**2 / 5
#
# # Separate inside and outside points
# x_in, y_in = [], []
# x_out, y_out = [], []
#
# for xi, yi in zip(x, y):
#     if xmin> xi or xi> xmax or ymin>yi or yi> ymax:
#         x_in.append(xi)
#         y_in.append(yi)
#     else:
#         x_out.append(xi)
#         y_out.append(yi)
#
# # Plot
# plt.figure()
# plt.title("exterior Curve Clipping (Parabola)")
# # Clipping window
# plt.plot([xmin, xmax, xmax, xmin, xmin],
#          [ymin, ymin, ymax, ymax, ymin], 'k-')
# plt.plot(x_out, y_out, 'r--')
# plt.plot(x_in, y_in, 'g')
# plt.show()

# polygon

import matplotlib.pyplot as plt

# Region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

# Clipping window
xmin, xmax = -5, 5
ymin, ymax = -5, 5

# Compute region code
# def compute_code(x, y):
#     code = INSIDE
#     if x < xmin:
#         code |= LEFT
#     elif x > xmax:
#         code |= RIGHT
#     if y < ymin:
#         code |= BOTTOM
#     elif y > ymax:
#         code |= TOP
#
#     return code
#
# # Cohen-Sutherland algorithm
# def cohen_sutherland(x1, y1, x2, y2):
#     code1 = compute_code(x1, y1)
#     code2 = compute_code(x2, y2)
#
#     count=0
#
#     while True:
#         if code1 == 0 and code2 == 0:
#             count=1
#             break
#         elif (code1 & code2) != 0:
#             break
#         else:
#             x, y = 0, 0
#             code_out = code1 if code1 != 0 else code2
#
#             if code_out & TOP:
#                 x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
#                 y = ymax
#
#             elif code_out & BOTTOM:
#                 x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
#                 y = ymin
#
#             elif code_out & RIGHT:
#                 y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
#                 x = xmax
#
#             elif code_out & LEFT:
#                 y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
#                 x = xmin
#
#             if code_out == code1:
#                 x1, y1 = x, y
#                 code1 = compute_code(x1, y1)
#             else:
#                 x2, y2 = x, y
#                 code2 = compute_code(x2, y2)
#
#     if count:
#         return x1, y1, x2, y2
#     else:
#         return None
#
# # Example line
# x1, y1 = -8, -3
# x2, y2 = 6, 7
# result = cohen_sutherland(x1, y1, x2, y2)
# # Plot
# plt.plot([xmin, xmax, xmax, xmin, xmin],
#          [ymin, ymin, ymax, ymax, ymin], 'k-')  # window
#
# plt.plot([x1, x2], [y1, y2], 'r--', label="Original")
#
# if result:
#     x1_c, y1_c, x2_c, y2_c = result
#     plt.plot([x1_c, x2_c], [y1_c, y2_c], 'g', label="Clipped")
#
# plt.legend()
# plt.axhline(0)
# plt.axvline(0)
# plt.title("Cohen-Sutherland Line Clipping")
# plt.show()

#lineclip
# # Region codes
# INSIDE = 0   # 0000
# LEFT   = 1   # 0001
# RIGHT  = 2   # 0010
# BOTTOM = 4   # 0100
# TOP    = 8   # 1000

# # Window boundaries
# xmin, ymin, xmax, ymax = 10, 20, 150, 80

# # Compute region code
# def window(x, y):
#     code = INSIDE
#     if x < xmin:
#         code |= LEFT
#     elif x > xmax:
#         code |= RIGHT

#     if y < ymin:
#         code |= BOTTOM
#     elif y > ymax:
#         code |= TOP

#     return code


# # Cohen-Sutherland Line Clipping
# def clip_line(x1, y1, x2, y2):
#     code1 = window(x1, y1)
#     code2 = window(x2, y2)

#     accept = False

#     while True:
#         # Case 1: Both points inside
#         if code1 == 0 and code2 == 0:
#             accept = True
#             break

#         # Case 2: Both points share outside region
#         elif code1 & code2:
#             break

#         # Case 3: Partial clipping
#         else:
#             if code1 != 0:
#                 code_out = code1
#             else:
#                 code_out = code2

#             if code_out & TOP:
#                 x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
#                 y = ymax

#             elif code_out & BOTTOM:
#                 x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
#                 y = ymin

#             elif code_out & RIGHT:
#                 y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
#                 x = xmax

#             elif code_out & LEFT:
#                 y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
#                 x = xmin

#             # Replace outside point
#             if code_out == code1:
#                 x1, y1 = x, y
#                 code1 = window(x1, y1)
#             else:
#                 x2, y2 = x, y
#                 code2 = window(x2, y2)

#     if accept:
#         print(f"Clipped Line: ({x1}, {y1}) to ({x2}, {y2})")
#     else:
#         print("Line is outside")

# # Main
# x1, y1 = 5, 5
# x2, y2 = 120, 120
# clip_line(x1, y1, x2, y2)
