import sys
from io import StringIO
import unittest
import bisect


def resolve():
    n, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = list(set(A))

    K = [int(input()) for i in range(q)]

    A.sort()
    # print(A)

    count = 0
    B = [(0, 0, 0)]
    for i in range(n):
        a = A[i]
        count += 1
        B.append((a, count, a-count))

    keys = [r[2] for r in B]

    # print(B)

    for k in K:
        index = bisect.bisect_left(keys, k)
        # print(k, index)

        if index >= len(keys):
            # print('debug')
            print(A[-1] + k - B[-1][2])
        else:
            print(B[index][0] - 1 - (B[index][2] - k))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[: -1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 3
3 5 6 7
2
5
3"""
        output = """2
9
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 2 3 4 5
1
10"""
        output = """6
15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
