# Region codes
INSIDE = 0   # 0000
LEFT   = 1   # 0001
RIGHT  = 2   # 0010
BOTTOM = 4   # 0100
TOP    = 8   # 1000

# Window boundaries
xmin, ymin, xmax, ymax = 10, 20, 150, 80

# Compute region code
def window(x, y):
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


# Cohen-Sutherland Line Clipping
def clip_line(x1, y1, x2, y2):
    code1 = window(x1, y1)
    code2 = window(x2, y2)

    accept = False

    while True:
        # Case 1: Both points inside
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Case 2: Both points share outside region
        elif code1 & code2:
            break

        # Case 3: Partial clipping
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

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

            # Replace outside point
            if code_out == code1:
                x1, y1 = x, y
                code1 = window(x1, y1)
            else:
                x2, y2 = x, y
                code2 = window(x2, y2)

    if accept:
        print(f"Clipped Line: ({x1}, {y1}) to ({x2}, {y2})")
    else:
        print("Line is outside")

# Main
x1, y1 = 5, 5
x2, y2 = 120, 120
clip_line(x1, y1, x2, y2)
