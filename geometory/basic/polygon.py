from geometory.basic.point import Point
from geometory.basic.line import Line


class Polygon:
    def __init__(self, arr: list[Point]):
        """
        配列arrは，多角形の隣り合った点を反時計回りに訪問する順番であること．
        """
        self.arr = arr
        self.n = len(arr)

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, idx: int) -> Point:
        return self.arr[idx]

    def contains(self, p: Point) -> int:
        """
        点pが多角形に内包されているか判定
        IN 2
        ON 1
        OUT 0
        """
        x = False
        for i in range(self.n):
            a = self.arr[i] - p
            b = self.arr[(i + 1) % self.n] - p
            if abs(a.cross(b)) < p.EPS and a.dot(b) < p.EPS:
                return 1
            if a.y > b.y:
                a, b = b, a
            if a.y < p.EPS and p.EPS < b.y and a.cross(b) > p.EPS:
                x = True
        return 2 if x else 0

    def divide_by_segment(self, seg: Line) -> int:
        lines = [Line(self.arr[i], self.arr[(i + 1) % self.n]) for i in range(self.n)]
        cnt = sum(1 for line in lines if line.intersect(seg))
        return (cnt >> 1) + 1
