import sys
from io import StringIO
import unittest


def resolve():
    n, m = list(map(int, input().split()))
    S = []
    for _ in range(n):
        s = input()
        S.append(s)

    set_a = set()  # 奇数
    set_b = set()  # 偶数

    # result = 0
    # for i in range(n):
    #     for j in range(i+1, n):
    #         match_cnt = 0
    #         for k in range(m):
    #             if int(S[i][k]) ^ int(S[j][k]) == 1:
    #                 match_cnt += 1
    #         if match_cnt % 2 == 1:
    #             print(S[i], S[j])
    #             result += 1

    result = 0
    for i in range(n):
        if S[i].count('1') % 2 == 1:
            set_a.add(i)
        else:
            set_b.add(i)
    # print(set_a)
    # print(set_b)

    print(len(set_a) * len(set_b))


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
        input = """3 2
00
01
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 5
10101
00001
00110
11110
00100
11111
10000"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
