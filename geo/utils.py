import math
from typing import Tuple

Point = Tuple[float, float]

def _as_point(p) -> Point:
    if (
        isinstance(p, (tuple, list))
        and len(p) == 2
        and all(isinstance(x, (int, float)) for x in p)
    ):
        return float(p[0]), float(p[1])
    raise TypeError("Point must be a (x, y) pair of numbers.")

def distance(p1: Point, p2: Point) -> float:
    x1, y1 = _as_point(p1)
    x2, y2 = _as_point(p2)
    return math.hypot(x2 - x1, y2 - y1)

def midpoint(p1: Point, p2: Point) -> Point:
    x1, y1 = _as_point(p1)
    x2, y2 = _as_point(p2)
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

def slope(p1: Point, p2: Point) -> float:
    x1, y1 = _as_point(p1)
    x2, y2 = _as_point(p2)
    dx = x2 - x1
    if dx == 0:
        raise ZeroDivisionError("Vertical line has undefined slope.")
    return (y2 - y1) / dx

def triangle_area(a: Point, b: Point, c: Point) -> float:
    ax, ay = _as_point(a)
    bx, by = _as_point(b)
    cx, cy = _as_point(c)
    # shoelace formula
    return abs(ax*(by - cy) + bx*(cy - ay) + cx*(ay - by)) / 2.0

def rectangle_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("width and height must be numbers.")
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative.")
    return float(width) * float(height)
