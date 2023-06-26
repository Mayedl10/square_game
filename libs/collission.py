import math

def rectCollission(aX, aY, aWidth, aHeight, bX, bY, bWidth, bHeight):
    """Checks if two rectangles with the upper left corner (aX,aY), (bX,bY),
    the width aHeight, bHeight and the width aWidth, bWidth collide. In this imaginary
    coordinates-grid (0,0) is the top left, moving right increases the X-coordinate and moving down
    increases the Y-coordinate."""
    return (aX + aWidth > bX) and (aX < bX + bWidth) and (aY + aHeight > bY) and (aY < bY + bHeight)

def pointInCircle(pointX, pointY, circleCenterX, circleCenterY, rad):
    """Checks if a point (pointX, pointY) is inside a circle with center (circleCenterX, circleCenterY) and radius rad.
    Returns True if the point is inside the circle, returns False if the point is on or outside the circle."""
    return (math.pow((pointX - circleCenterX),2) + math.pow((pointY - circleCenterY),2)) < rad

def pointOnCircle(pointX, pointY, circleCenterX, circleCenterY, rad):
    """Checks if a point (pointX, pointY) is on a circle with center (circleCenterX, circleCenterY) and radius rad.
    Returns True if the point is on the circle, returns False if the point inside or outside the circle."""
    return (math.pow((pointX - circleCenterX),2) + math.pow((pointY - circleCenterY),2)) == rad

def pointOutCircle(pointX, pointY, circleCenterX, circleCenterY, rad):
    """Checks if a point (pointX, pointY) is on a circle with center (circleCenterX, circleCenterY) and radius rad.
    Returns True if the point is outside the circle, returns False if the point inside or on the circle."""
    return (math.pow((pointX - circleCenterX),2) + math.pow((pointY - circleCenterY),2)) > rad

def circleCollission(x1, y1, rad1, x2, y2, rad2):
    """checks if two circles with the radii rad1, rad2 and the center points (x1,y1), (x2,y2) collide.
    Returns True if the circles intersect or touch each other, otherwise returns False"""
    return math.hypot(x1-x2, y1-y2) <= (rad1 + rad2)

def pointDstFlt(x1,y1,x2,y2):
    "Returns the distance between two points as float"
    return math.dist((x1,y1),(x2,y2))

def pointDstTpl(x1,y1,x2,y2):
    "Returns the distance between two points as tuple"
    return (x2-x1,y2-y1)

if __name__ == "__main__": print(help(rectCollission))





























        
