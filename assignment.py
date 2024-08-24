import turtle

turtle.colormode(1.0)

def triangle(pt1, pt2, pt3, pen, fill):
    """ First, pen up and start filling color, and move pen to c_h.
and draw triangle, and move to c_h again."""
    turtle.pencolor(pen)
    turtle.fillcolor(fill)
    turtle.penup()
    turtle.goto(pt1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(pt2)
    turtle.goto(pt3)
    turtle.goto(pt1)
    turtle.end_fill()

def poly(pts, cols):
    """ First, I divided the problem to two situations since drawing triangle and
 changing color needs different unknown numbers(like for i in range).
 One is length of the pts
 is equal or shorter than length of the cols, and the other is the length of the
  cols is shorter than length of the pts. And I used lots of time to find out the
  way to determine the triangle that is drawn last. I found out the way by using
  for, quotient, and remainder. """
    c = (0,0)
    for i in range(len(pts)):
        c=tuple(sum(elem) for elem in zip(c,pts[i]))
    c_h = (c[0]/len(pts),c[1]/len(pts))
    if len(cols) >= len(pts):
        for i in range(len(pts)-1):
            triangle(c_h,pts[i],pts[i+1],(0,0,0),cols[i])
        triangle(c_h,pts[len(pts)-1],pts[0],(0,0,0),cols[len(pts)-1])
    else :
        q = len(pts)/len(cols)
        r = len(pts)%len(cols)
        q = int(q)
        j = 0
        for i in range(len(cols)*q):
            if j < len(cols):
                triangle(c_h,pts[i],pts[i+1],(0,0,0),cols[j])
                j += 1
            else :
                j = 0
                triangle(c_h,pts[i],pts[i+1],(0,0,0),cols[j])
                j += 1
        for i in range(r-1):
            triangle(c_h,pts[q*len(cols)+i],pts[q*len(cols)+1+i],(0,0,0),cols[i])
        triangle(c_h,pts[len(pts)-1],pts[0],(0,0,0),cols[r-1])

    
def hsv2rgb(h, s, v):
    """Converts a colour from the HSV space to the RGB space.
    'hue', 'saturation' and 'value' are all floats from 0.0 to 1.0.
    Returns a (red, green, blue) triplet, where 'red', 'green' and 'blue' are all floats ranging from 0.0 to 1.0.
    E.g., if hue=0.0, saturation=1.0, value=1.0, returns (1.0, 0.0, 0.0)."""
    
    to_centre = 1.0 - abs((h * 3) % 1.0)
    mx = v * to_centre**(1/2) * s + (1.0 - s)
    md = (1.0 - to_centre)**(1/2) * s + (1.0 - s)
    mn = 1.0 - s
    if h < 1 / 3:
        return (mx, md, mn)
    elif h < 2 / 3:
        return (mn, mx, md)
    else:
        return (md, mn, mx)

def rainbow(saturation, value, n):
    """ Divide i by n, I can determine hue of the function hsv2rgb.)
"""
    new_rainbow = []
    for i in range(n):
        new_rainbow.append(hsv2rgb(i/n,saturation,value))
        print(hsv2rgb(i/n,saturation,value))
    return new_rainbow
    

def transform(pts, x_sc, x_diff, y_sc, y_diff):
    """Performs an affine transform on a list of 2D points.
    'pts' is a list of (x,y) coordinates.
    'x_sc', 'x_diff', 'y_sc' and 'y_diff' are all floats.
    'x_sc' and 'y_sc' are scaling factors (multiplying coefficient).
    'x_diff' and 'y_diff' are constant offsets (additive constants).
    Returns a list of transformed points.
    E.g., if pts=[(0,0),(2,2)], x_sc=2, x_diff=100, y_sc=-1, y_diff=-1, returns [(100, -1), (104, -3)]."""
    new_pts = []
    for x, y in pts:
        new_pts.append((x * x_sc + x_diff, y * y_sc + y_diff))
    return new_pts

def draw_heart():
    """Draws a heart."""
    
    heart = [(513, 918), (111, 534), (49, 418), (40, 346), (54, 256), (145, 141), (244, 109), (333, 112), (441, 148), (513, 211),
        (595, 150), (696, 109), (840, 121), (924, 172), (957, 258), (984, 375), (946, 493), (811, 640)]

    heart = transform(heart, 0.6, -307, -0.6, 200)
    poly(heart, rainbow(1.0, 1.0, 8))


def draw_girls_head():
    """Draws a girl's head."""
    head = [(497, 2382), (642, 2040), (567, 1686), (525, 1599), (207, 1575), (156, 1554), (141, 1503), (156, 1416), (108, 1332), (90, 1176),
        (12, 1116), (3, 1065), (36, 1023), (123, 837), (114, 627), (150, 456), (252, 303), (390, 147), (585, 60), (762, 12), (960, 3), (1110, 12),
        (1275, 75), (1374, 213), (1470, 345), (1530, 573), (1506, 807), (1461, 981), (1368, 1125), (1302, 1254), (1296, 1386), (1332, 1566),
        (1425, 1746), (1575, 1983), (1827, 2307), (1518, 2394), (1209, 2394), (798, 2340), (519, 2346)]
    head = transform(head, 0.3, -240, -0.3, 420)
    ponytail = [(1413, 345), (1515, 384), (1596, 414), (1686, 399), (1845, 336), (1824, 375), (1953, 411), (1917, 453), (2004, 597), (2049, 747),
        (1992, 894), (1893, 1104), (1893, 1200), (1980, 1278), (1917, 1326), (1761, 1617), (1695, 1746), (1575, 1791), (1497, 1830),
        (1485, 1713), (1440, 1767), (1323, 1500), (1377, 1473), (1503, 1233), (1569, 885), (1542, 765), (1512, 759)]
    ponytail = transform(ponytail, 0.3, -240, -0.3, 420)
    poly(head, rainbow(0.6, 1.0, 20))
    poly(ponytail, rainbow(0.3, 0.6, 12))

print("if you enter 1, it will draw heart. If yoy enter 2, it will draw girls head.")

number = input()

if number == "1":
    draw_heart()

if number == "2":
    draw_girls_head()
