import sys
from io import StringIO
import unittest


def resolve():
    n, x = list(map(int, input().split()))
    x *= 100
    result = float('inf')
    done = 0
    for i in range(n):
        v, p = list(map(int, input().split()))
        done += v * p
        if done > x:
            result = min(result, i+1)
        # print(i+1, done, result)
    if result == float('inf'):
        print(-1)
    else:
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
        input = """2 15
200 5
350 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10
200 5
350 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1000000
1000 100
1000 100
1000 100"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
