import self as self


class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


box = Rectangle((0, 0), 100, 200)
bomb = Rectangle((100, 80), 5, 10)  # In my video game
print("box: ", box)
print("bomb: ", bomb)

def create_rectangle(x, y, width, height):
    return Rectangle((x, y), width, height);

def str_rectangle(rect):
    return str(rect);

def shift_rectangle(rect, dx, dy):
    rect.corner = (dx, dy);

def offset_rectangle(rect, dx, dy):
    return Rectangle((rect.corner [0] + dx, rect.corner[1] + dy), rect.width, rect.height);

r1 =create_rectangle(10, 20, 30, 40)
print (str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print (str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print (str_rectangle(r1)) # should be same as previous
print (str_rectangle(r2))
