import sys
from io import StringIO
import unittest


def base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out  # int out


def resolve():
    x = input()
    m = int(input())

    if int(x) < 10:
        if int(x) <= m:
            print(1)
            return
        else:
            print(0)
            return

    d = 0
    for c in x:
        d = max(d, int(c))

    left = d + 1
    right = 10**19

    while left < right:
        # print(left, right)
        mid = (left + right) // 2
        if base_n_to_10(x, mid) > m:
            right = mid
        else:
            left = mid+1

    # print('d: ', d)
    # print('left', 'right: ', left, right)
    # print(base_n_to_10(x, right-1))
    # print(base_n_to_10(x, right))
    if right-1 >= d:
        print(right-1-d)
    else:
        print(0)


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
        input = """22
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999
1500"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000000000000000000000000000000000000000000000000000
1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
