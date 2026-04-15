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
def compute_code(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Cohen-Sutherland algorithm
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    count=0

    while True:
        if code1 == 0 and code2 == 0:
            count=1
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if count:
        return x1, y1, x2, y2
    else:
        return None

# Example line
x1, y1 = -8, -3
x2, y2 = 6, 7
result = cohen_sutherland(x1, y1, x2, y2)
# Plot
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'k-')  # window

plt.plot([x1, x2], [y1, y2], 'r--', label="Original")

if result:
    x1_c, y1_c, x2_c, y2_c = result
    plt.plot([x1_c, x2_c], [y1_c, y2_c], 'g', label="Clipped")

plt.legend()
plt.axhline(0)
plt.axvline(0)
plt.title("Cohen-Sutherland Line Clipping")
plt.show()