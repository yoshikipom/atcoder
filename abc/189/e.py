import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    ops = [list(map(int, input().split())) for _ in range(m)]
    q = int(input())
    ab = [list(map(int, input().split())) for _ in range(q)]

    memo = []
    p1 = 'x'
    sign1 = 1
    diff1 = 0
    p2 = 'y'
    sign2 = 1
    diff2 = 0
    memo.append((p1, sign1, diff1, p2, sign2, diff2))
    for op in ops:
        if op[0] == 1:
            p1, p2 = p2, p1
            sign1, sign2 = sign2, sign1
            diff1, diff2 = diff2, diff1
            sign2 *= -1
            diff2 *= -1
            memo.append((p1, sign1, diff1, p2, sign2, diff2))
        elif op[0] == 2:
            p1, p2 = p2, p1
            sign1, sign2 = sign2, sign1
            diff1, diff2 = diff2, diff1
            sign1 *= -1
            diff1 *= -1
            memo.append((p1, sign1, diff1, p2, sign2, diff2))
        elif op[0] == 3:
            sign1 *= -1
            diff1 = -1 * diff1 + 2 * op[1]
            memo.append((p1, sign1, diff1, p2, sign2, diff2))
        elif op[0] == 4:
            sign2 *= -1
            diff2 = -1 * diff2 + 2 * op[1]
            memo.append((p1, sign1, diff1, p2, sign2, diff2))

    # print(*memo, sep='\n')

    for a, b in ab:
        b -= 1
        x, y = xy[b]

        p1, sign1, diff1, p2, sign2, diff2 = memo[a]
        if p1 == 'x':
            result1 = x * sign1 + diff1
            result2 = y * sign2 + diff2
            print(result1, result2)
        else:
            result1 = y * sign1 + diff1
            result2 = x * sign2 + diff2
            print(result1, result2)


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
        input = """1
1 2
4
1
3 3
2
4 2
5
0 1
1 1
2 1
3 1
4 1"""
        output = """1 2
2 -1
4 -1
1 4
1 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1000000000 0
0 1000000000
4
3 -1000000000
4 -1000000000
3 1000000000
4 1000000000
2
4 1
4 2"""
        output = """5000000000 4000000000
4000000000 5000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
