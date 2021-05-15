import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())

    li = [15]
    for i in range(1, 10001):
        if i == 15:
            continue
        if i % 6 == 0 or i % 10 == 0 or i % 15 == 0:
            li.append(i)

    print(*li[:n])
    # print(len(li))


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
        input = """4"""
        output = """84 60 105 70"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
