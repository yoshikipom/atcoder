import sys
from io import StringIO
import unittest


def resolve():
    b, c = list(map(int, input().split()))
    if b >= 0:
        l1 = -b - (c-1) // 2
        r1 = -b + (c-1) // 2
        l2 = b - c // 2
        if c >= 2:
            r2 = b + (c-2) // 2
        else:
            r2 = b
    else:
        l1 = b - c // 2
        if c >= 2:
            r1 = b + (c-2) // 2
        else:
            r1 = b
        l2 = -b - (c-1) // 2
        r2 = -b + (c-1) // 2

    # print(l1, r1, l2, r2)
    if r1 < l2:
        print(r1-l1+1 + r2-l2+1)
    else:
        min_num = min([l1, r1, l2, r2])
        max_num = max([l1, r1, l2, r2])
        print(max_num-min_num+1)


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
        input = """11 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """112 20210213"""
        output = """20210436"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """-211 1000000000000000000"""
        output = """1000000000000000422"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
