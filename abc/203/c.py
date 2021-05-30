import sys
from io import StringIO
import unittest


def resolve():
    n, k = list(map(int, input().split()))
    AB = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        AB.append((a, b))

    AB.sort(key=lambda x: x[0])

    cur = 0
    money = k
    # print('----------')
    # print(AB)
    # print('----------')
    for ab in AB:
        # print(cur, money)
        a = ab[0]
        b = ab[1]

        if cur + money < a:
            print(cur + money)
            return

        money -= (a-cur)
        cur = a
        money += b

    print(cur + money)


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
        input = """2 3
2 1
5 10"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000"""
        output = """6000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
5 5
2 1
2 2"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
