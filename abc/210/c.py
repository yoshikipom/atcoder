import sys
from io import StringIO
import unittest


def resolve():
    n, k = list(map(int, input().split()))
    C = list(map(int, input().split()))

    D = {}
    for i in range(k):
        if C[i] not in D:
            D[C[i]] = 0
        D[C[i]] += 1
    result = len(D)

    for r in range(k, n):
        l = r-k
        if C[l] in D:
            D[C[l]] -= 1
            if D[C[l]] == 0:
                del D[C[l]]
        if C[r] not in D:
            D[C[r]] = 0
        D[C[r]] += 1
        result = max(result, len(D))
        # print(r, l, D)

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
        input = """7 3
1 2 1 2 3 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
4 4 4 4 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 6
304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
