import matplotlib.pyplot as plt
# Input
x_old, y_old = map(int, input("Enter X_old Y_old: ").split())
sx, sy = map(int, input("Enter Tx Ty: ").split())

# Translation
x_new = x_old*sx
y_new = y_old*sy

# Output
print("New Point:", (x_new, y_new))
plt.scatter(x_old, y_old)
plt.scatter(x_new, y_new)
plt.plot([x_old, x_new], [y_old, y_new])
plt.grid()
plt.show()