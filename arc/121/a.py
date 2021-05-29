import sys
from io import StringIO
import unittest
import copy


def resolve():
    n = int(input())
    X = []
    Y = []
    XY = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        XY.append((x, y, i))

    XY2 = copy.copy(XY)

    XY.sort(key=lambda x: x[0])
    XY2.sort(key=lambda x: x[1])

    C = []

    C.append((XY[-1][0]-XY[0][0], sorted([XY[-1][2], XY[0][2]])))
    C.append((XY[-2][0]-XY[0][0], sorted([XY[-2][2], XY[0][2]])))
    C.append((XY[-1][0]-XY[1][0], sorted([XY[-1][2], XY[1][2]])))

    C.append((XY2[-1][1]-XY2[0][1], sorted([XY2[-1][2], XY2[0][2]])))
    C.append((XY2[-2][1]-XY2[0][1], sorted([XY2[-2][2], XY2[0][2]])))
    C.append((XY2[-1][1]-XY2[1][1], sorted([XY2[-1][2], XY2[1][2]])))
    C.sort(key=lambda x: x[0], reverse=True)
    # print(C)

    used = set()
    count = 0
    for c in C:
        if tuple(c[1]) in used:
            continue
        used.add(tuple(c[1]))
        count += 1
        if count == 2:
            print(c[0])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
0 0
1 2
4 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
0 0
0 0
1 0
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
407 361
167 433
756 388
-551 -47
306 -471
36 928
338 -355
911 852
288 70
-961 -769
-668 -386
-690 -378
182 -609
-677 401
-458 -112
184 -131
-243 888
-163 471
-11 997
119 544"""
        output = """1766"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
