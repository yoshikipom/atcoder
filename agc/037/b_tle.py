import sys
from io import StringIO
import unittest
from operator import itemgetter


class Problem():
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "l:{}, r:{}, diff:{}".format(
            self.l, self.r, self.r-self.l
        )


def calc_joy(problems):
    r = min(problems, key=lambda p: p.r).r
    l = max(problems, key=lambda p: p.l).l
    return max(r-l + 1, 0)


def resolve():
    N = int(input())

    problems = []
    for i in range(N):
        l, r = map(int, input().split())
        problems.append(Problem(l, r))

    problems = sorted(problems, reverse=True, key=lambda p: p.l)
    problems = sorted(problems, key=lambda p: p.r)

    # for p in problems:
    # print(p)

    joy_max = 0
    others = []
    for i in range(len(problems) - 1):
        others.append(problems.pop())
        joy1 = calc_joy(problems)
        joy2 = calc_joy(others)
        joy_max = max(joy_max, joy1+joy2)
        # print('-------')
        # print(len(problems))
        # print(len(others))
        # print(joy1)
        # print(joy2)
        # print('-------')

    print(joy_max)


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
        input = """4
4 7
1 4
5 8
2 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 20
2 19
3 18
4 17"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
457835016 996058008
456475528 529149798
455108441 512701454
455817105 523506955
457368248 814532746
455073228 459494089
456651538 774276744
457667152 974637457
457293701 800549465
456580262 636471526"""
        output = """540049931"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
