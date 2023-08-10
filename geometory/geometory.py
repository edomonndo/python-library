import math


class Point:
    def __init__(self, x, y):
        self.EPS = 1e-10
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Point(self.x / k, self.y / k)

    def __floordiv__(self, k):
        return Point(self.x // k, self.y // k)

    def __eq__(self, other):
        return abs(self.x - other.x) < self.EPS and abs(self.y - other.y) < self.EPS

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __gt__(self, other):
        if self.x != other.x:
            return self.x > other.x
        return self.y > other.y

    def __str__(self):
        return "{} {}".format(self.x, self.y)

    def norm(self):
        return self.x**2 + self.y**2

    def abs(self):
        return self.norm() ** 0.5

    def dot(self, other):
        """内積"""
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """外積"""
        return self.x * other.y - self.y * other.x

    def dist_euclid(self, other):
        """ユークリッド距離"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def dist_manhattan(self, other):
        """マンハッタン距離"""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def dist_chebyshev(self, other):
        """チェビシェフ距離"""
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def is_orthogonal(self, other):
        """直交判定"""
        return abs(self.dot(other)) < self.EPS

    def is_parallel(self, other):
        """平行判定"""
        return abs(self.cross(other)) < self.EPS

    def ccw(self, other1, other2):
        """自身から点other1に向かうベクトルに対して，点other2の位置を返す.
        COUNTER_CLOCKWISE = 1
        CLOCKWISE = -1
        ONLINE_BACK = 2
        ONLINE_FRONT = -2
        ON_SEGMENT = 0
        """
        a = other1 - self
        b = other2 - self
        if a.cross(b) > self.EPS:
            return 1
        if a.cross(b) < -self.EPS:
            return -1
        if a.dot(b) < -self.EPS:
            return 2
        if a.norm() < b.norm():
            return -2
        return 0

    def arg(self):
        return math.atan2(self.y, self.x)


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.EPS = 1e-10
        self.s = p1
        self.t = p2
        self.vector = p2 - p1

    def __str__(self):
        return "{} {} {} {}".format(self.s.x, self.s.y, self.t.x, self.t.y)

    def is_orthogonal(self, other):
        return abs(self.vector.dot(other.vector)) < self.EPS

    def is_parallel(self, other):
        return abs(self.vector.cross(other.vector)) < self.EPS

    def project(self, point):
        """直線に点pointから垂線を引いたときの交点"""
        r = self.vector.dot(point - self.s) / self.vector.norm()
        return self.s + self.vector * r

    def refrection(self, point):
        """直線を対称軸として，点pointと線対称な点の座標"""
        return point + (self.project(point) - point) * 2

    def get_distance(self, point):
        """直線と点のユークリッド距離"""
        return abs(self.vector.cross(point - self.s) / self.vector.abs())

    def get_distance_segment(self, point):
        """線分と点のユークリッド距離"""
        if self.vector.dot(point - self.s) < 0:
            p = point - self.s
            return p.abs()
        if self.vector.dot(self.t - point) < 0:
            p = point - self.t
            return p.abs()
        return self.get_distance(point)

    def get_distance_seg_to_seg(self, other):
        """線分と線分のユークリッド距離"""
        if self.intersect(other):
            return 0
        return min(
            self.get_distance_segment(other.s),
            self.get_distance_segment(other.t),
            other.get_distance_segment(self.s),
            other.get_distance_segment(self.t),
        )

    def intersect(self, other):
        if isinstance(other, Line):
            return (
                self.s.ccw(self.t, other.s) * self.s.ccw(self.t, other.t) <= 0
                and other.s.ccw(other.t, self.s) * other.s.ccw(other.t, self.t) <= 0
            )
        if isinstance(other, Circle):
            return self.get_distance(other.center) <= other.r
        raise TypeError

    def get_cross_point(self, other):
        if isinstance(other, Line):
            if not self.intersect(other):
                return -1
            d1 = abs(other.vector.cross(self.s - other.t))
            d2 = abs(other.vector.cross(self.t - other.t))
            t = d1 / (d1 + d2)
            return self.s + (self.vector) * t
        if isinstance(other, Circle):
            if not self.intersect(other):
                return -1
            pr = self.project(other.center)
            e = self.vector / self.vector.abs()
            base = (other.r**2 - (pr - other.center).norm()) ** 0.5
            p1, p2 = pr + e * base, pr - e * base
            if p1.x == p2.x:
                return (p1, p2) if p1.y < p2.y else (p2, p1)
            if p1.x < p2.x:
                return (p1, p2)
            return (p2, p1)
        raise TypeError


class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self.r = radius

    def __str__(self):
        return "{} {} {}".format(self.center.x, self.center.y, self.r)

    def get_diameter(self):
        return self.r * 2

    def get_area(self):
        return math.pi * self.r * self.r

    def intersect(self, other):
        if isinstance(other, Line):
            return other.get_distance(self.center) <= self.r
        elif isinstance(other, Circle):
            return self.center.dist_euclid(other.center) <= (self.r + other.r)
        else:
            raise TypeError

    def get_cross_point(self, other):
        if isinstance(other, Line):
            if not other.intersect(self):
                return -1
            pr = other.project(self.center)
            e = other.vector / other.vector.abs()
            base = (self.r**2 - (pr - self.center).norm()) ** 0.5
            p1, p2 = pr + e * base, pr - e * base
            if p1.x == p2.x and p1.y > p2.y:
                p1, p2 = p2, p1
            elif p1.x > p2.x:
                p1, p2 = p2, p1
            return p1, p2
        elif isinstance(other, Circle):
            if not self.intersect(other):
                return -1
            d = (self.center - other.center).abs()
            a = math.acos((self.r**2 + d**2 - other.r**2) / (2 * self.r * d))
            t = (other.center - self.center).arg()
            p1, p2 = self.center + self._polar(
                self.r, t + a
            ), self.center + self._polar(self.r, t - a)
            if p1.x == p2.x and p1.y > p2.y:
                p1, p2 = p2, p1
            elif p1.x > p2.x:
                p1, p2 = p2, p1
            return p1, p2
        else:
            raise TypeError

    def _polar(self, a, r):
        return Point(math.cos(r) * a, math.sin(r) * a)


class Rectangle:
    def __init__(self, arr):
        """
        配列arrは，多角形の隣り合った点を反時計回りに訪問する順番であること．
        """
        self.arr = arr
        self.n = len(arr)

    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        return self.arr[idx]

    def contains(self, p):
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

    def convex_hull(self):
        """
        アンドリューのアルゴリズム．
        """
        if self.n < 3:
            return -1
        arr = sorted(self.arr)
        upper = [arr[0], arr[1]]  # xが小さいものから2つ追加
        # 凸包の上部を形成
        for p in arr[2:]:
            n = len(upper)
            while n >= 2 and upper[-2].ccw(upper[-1], p) == 1:
                upper.pop()
                n -= 1
            upper.append(p)

        lower = [arr[-1], arr[-2]]  # xが大きいものから２つ追加
        # 凸包の下部を形成
        for p in arr[::-1][2::]:
            n = len(lower)
            while n >= 2 and lower[-2].ccw(lower[-1], p) == 1:
                lower.pop()
                n -= 1
            lower.append(p)
        # 時計回りになるように凸包の点の列を形成
        res = upper[1:-1] + lower
        return res[::-1]
