import math
import matplotlib.pyplot as plt
pi=math.pi
# Input
x_old, y_old = map(int, input("Enter X_old Y_old: ").split())
deg = float(input("Enter angle (in degrees): "))
theta= deg*180/pi # Convert degree to radian
# Rotation
x_new = x_old * math.cos(theta) - y_old * math.sin(theta)
y_new = x_old * math.sin(theta) + y_old * math.cos(theta)

# Output
print("New Point:", (round(x_new, 2), round(y_new, 2)))
# Plot
plt.scatter(x_old, y_old)
plt.scatter(x_new, y_new)
plt.plot([x_old, x_new], [y_old, y_new])
plt.show()