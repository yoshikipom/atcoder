import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = list(map(int, input().split()))

    d = {}
    d[0] = [0]
    d[1] = [1]
    d[2] = [2, 4, 8, 6]
    d[3] = [3, 9, 7, 1]
    d[4] = [4, 6]
    d[5] = [5]
    d[6] = [6]
    d[7] = [7, 9, 3, 1]
    d[8] = [8, 4, 2, 6]
    d[9] = [9, 1]

    tmp = pow(b, c, len(d[a % 10]))
    # print(tmp)
    print(d[a % 10][tmp-1])


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
        input = """4 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3141592 6535897 9323846"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
