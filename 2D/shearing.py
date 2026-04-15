import matplotlib.pyplot as plt

x_old, y_old = map(int, input("Enter X_old Y_old: ").split())
print("1. X-axis  2. Y-axis")
choice = int(input("Enter choice: "))

if choice == 1: # Reflection over x direction
    shx= int(input("Enter shx: "))
    x_new = x_old+ shx*y_old
    y_new = y_old
elif choice == 2: #reflection over y direction
    shy = int(input("Enter shy: "))
    x_new = x_old
    y_new = y_old+ shy*x_old
else:
    print("Invalid choice")
    exit()

# Output
print("New Point:", (round(x_new, 2), round(y_new, 2)))
plt.scatter(x_old, y_old)
plt.scatter(x_new, y_new)
plt.axhline(0)
plt.axvline(0)
plt.show()
