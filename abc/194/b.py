import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    a_min = min(A)
    b_min = min(B)
    a_min_index = A.index(a_min)
    b_min_index = B.index(b_min)
    if a_min_index != b_min_index:
        # print('-----p1------')
        result = max(a_min, b_min)
    else:
        # print('-----p2------')
        A.pop(a_min_index)
        B.pop(b_min_index)
        a_min2 = min(A)
        b_min2 = min(B)
        result = min(max(a_min, b_min2), max(a_min2, b_min))
        result = min(result, a_min + b_min)

    print(result)


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
8 5
4 4
7 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
11 7
3 2
6 7"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
