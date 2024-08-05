from typing import TypeVar

T = TypeVar("T")

from geometory.basic.point import Point


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def from_int(self, x1: T, y1: T, x2: T, y2: T) -> "Rectangle":
        return Rectangle(Point(x1, y1), Point(x2, y2))

    def __str__(self):
        return f"<Rect({self.top_left}, {self.bottom_right})>"

    def sub(self, other: "Rectangle"):
        xs1, ys1 = self.top_left.get()
        xs2, ys2 = self.bottom_right.get()
        xo1, yo1 = other.top_left.get()
        xo2, yo2 = other.bottom_right.get()

        if xs1 < xo1:
            yield Rectangle(Point(xs1, ys1), Point(xo1, ys2))
        if xs2 > xo2:
            yield Rectangle(Point(xo2, ys1), Point(xs2, ys2))
        if ys1 < yo1:
            yield Rectangle(Point(max(xs1, xo1), ys1), Point(min(xs2, xo2), yo1))
        if ys2 > yo2:
            yield Rectangle(Point(max(xs1, xo1), yo2), Point(min(xs2, xo2), ys2))

    def intersect(self, other: "Rectangle") -> bool:
        xs1, ys1 = self.top_left.get()
        xs2, ys2 = self.bottom_right.get()
        xo1, yo1 = other.top_left.get()
        xo2, yo2 = other.bottom_right.get()

        if xs1 >= xo2:
            return False
        elif xs2 <= xo1:
            return False

        if ys1 >= yo2:
            return False
        elif ys2 <= yo1:
            return False
        return True

    def get_area(self) -> T:
        return (self.bottom_right.x - self.top_left.x) * (
            self.bottom_right.y - self.top_left.y
        )


class Rectangles:
    def __init__(self):
        self.rects = []

    def __str__(self):
        return "<Rects(" + "\n ".join(str(r) for r in self.rects) + ")>"

    def add(self, rect: Rectangle) -> None:
        rects = []
        for r in self.rects:
            if rect.intersect(r):
                rects.extend(r.sub(rect))
            else:
                rects.append(r)
        rects.append(rect)
        self.rects = rects

    def area(self) -> T:
        """O(n^2)"""
        return sum(r.get_area() for r in self.rects)

    def not_intersect(self) -> bool:
        n = len(self.rects)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.rects[i].intersect(self.rects[j]):
                    return False
        return True
