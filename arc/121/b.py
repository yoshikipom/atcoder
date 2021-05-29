import sys
from io import StringIO
import unittest
import bisect


def resolve():
    n = int(input())
    n_dog = 2 * n

    R = []
    G = []
    B = []
    for i in range(n_dog):
        a, c = input().split()
        a = int(a)

        if c == 'R':
            R.append(a)
        elif c == 'G':
            G.append(a)
        else:
            B.append(a)

    R.sort()
    G.sort()
    B.sort()

    if len(R) % 2 == 0 and len(G) % 2 == 0 and len(B) % 2 == 0:
        print(0)
        return

    # Rは偶数、GとBは奇数にする
    if len(G) % 2 == 0:
        R, G = G, R
    if len(B) % 2 == 0:
        R, B = B, R

    SCORE = []

    for i in range(len(G)):
        g = G[i]
        index = bisect.bisect_left(B, g)
        score = min(abs(B[index % len(B)]-g), abs(B[(index-1) % len(B)]-g))
        SCORE.append(score)

    if len(R) == 0:
        print(SCORE[0])
        return

    RG_SCORE = []
    RB_SCORE = []

    for i in range(len(R)):
        r = R[i]
        index = bisect.bisect_left(G, r)
        score = min(abs(G[index % len(G)]-r), abs(G[(index-1) % len(G)]-r))
        RG_SCORE.append((score, i))

        index = bisect.bisect_left(B, r)
        score = min(abs(B[index % len(B)]-r), abs(B[(index-1) % len(B)]-r))
        RB_SCORE.append((score, i))

    RG_SCORE.sort(key=lambda x: x[0])
    RB_SCORE.sort(key=lambda x: x[0])
    RG_SCORE = RG_SCORE[:2]
    RB_SCORE = RB_SCORE[:2]

    # print(RG_SCORE)
    # print(RB_SCORE)

    if RG_SCORE[0][1] != RB_SCORE[0][1]:
        SCORE.append(RG_SCORE[0][0] + RB_SCORE[0][0])
    else:
        tmp = min(
            RG_SCORE[0][0] + RB_SCORE[1][0],
            RG_SCORE[1][0] + RB_SCORE[0][0]
        )
        SCORE.append(tmp)

    SCORE.sort()
    print(SCORE[0])


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
1 R
2 G"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1 B
2 B"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
585 B
293 B
788 B
222 B
772 G
841 B
115 R
603 G
450 B
325 R
851 B
205 G
134 G
651 R
565 R
548 B
391 G
19 G
808 B
475 B"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
