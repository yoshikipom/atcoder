import sys
from io import StringIO
import unittest


def resolve():
    h, w, x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    S = []
    for _ in range(h):
        S.append(input())

    result = 0

    for i in range(x, -1, -1):
        if S[i][y] == '.':
            result += 1
        else:
            break

    # print(result)

    for i in range(x+1, h):
        if S[i][y] == '.':
            result += 1
        else:
            break
    # print(result)

    for j in range(y-1, -1, -1):
        if S[x][j] == '.':
            result += 1
        else:
            break
    # print(result)

    for j in range(y+1, w):
        if S[x][j] == '.':
            result += 1
        else:
            break

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
        input = """4 4 2 2
# ..
...#
# .#.
.#.#"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5 1 4
# ....
#####
....#"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 4 2
.#..#
#.###
# ...
# ..#.
# .###"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
