import matplotlib.pyplot as plt

x_old, y_old = map(int, input("Enter X_old Y_old: ").split())
print("1. X-axis  2. Y-axis")
choice = int(input("Enter choice: "))

if choice == 1: # Reflection over x axis
    x_new = x_old
    y_new = -y_old
elif choice == 2: #reflection over y axis
    x_new = -x_old
    y_new = y_old
else:
    print("Invalid choice")
    exit()

# Output
print("New Point:", (round(x_new, 2), round(y_new, 2)))
# Plot
plt.scatter(x_old, y_old)
plt.scatter(x_new, y_new)
plt.axhline(0)
plt.axvline(0)
plt.show()

# 1. plt.axhline(0)
# একটি horizontal line (আড়াআড়ি লাইন) আঁকে
# y = 0 লাইনে
# অর্থাৎ X-axis draw করে
#
# 2. plt.axvline(0)
# একটি vertical line (লম্বা লাইন) আঁকে
# x = 0 লাইনে
# অর্থাৎ Y-axis draw করে