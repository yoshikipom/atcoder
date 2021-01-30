import sys
from io import StringIO
import unittest


def resolve():
    n, m = list(map(int, input().split()))
    ab = []
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        ab.append((a, b))
    k = int(input())
    cd = []
    for _ in range(k):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        cd.append((c, d))

    result = 0
    for bit in range(2**k):
        condition = [False for _ in range(n)]
        for i in range(k):
            if bit >> i & 1:
                condition[cd[i][1]] = True
            else:
                condition[cd[i][0]] = True

        tmp_result = 0
        for a, b in ab:
            if condition[a] and condition[b]:
                tmp_result += 1
        result = max(result, tmp_result)

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
        input = """4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
