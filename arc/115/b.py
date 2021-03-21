import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    C = []
    for _ in range(n):
        row = list(map(int, input().split()))
        C.append(row)

    if n == 1:
        print('Yes')
        print(C[0][0])
        print(0)
        return

    D_row = []
    for j in range(1, n):
        d = C[0][j] - C[0][j-1]
        D_row.append(d)

    for i in range(1, n):
        for j in range(1, n):
            d = C[i][j] - C[i][j-1]
            if d != D_row[j-1]:
                print('No')
                return

    D_col = []
    for i in range(1, n):
        d = C[i][0] - C[i-1][0]
        D_col.append(d)

    for j in range(1, n):
        for i in range(1, n):
            d = C[i][j] - C[i-1][j]
            if d != D_col[i-1]:
                print('No')
                return

    # print(D_row)
    # print(D_col)

    result_b = [0]
    for i in range(n-1):
        result_b.append(result_b[i] + D_row[i])

    result_a = [0]
    for i in range(n-1):
        result_a.append(result_a[i] + D_col[i])

    # print(result_a)
    # print(result_b)

    min_a = min(result_a)
    if min_a < 0:
        for i in range(n):
            result_a[i] -= min_a

    min_b = min(result_b)
    if min_b < 0:
        for i in range(n):
            result_b[i] -= min_b

    # print(result_a)
    # print(result_b)

    if result_a[0] + result_b[0] > C[0][0]:
        print('No')
        return

    diff = C[0][0] - result_a[0] - result_b[0]
    for i in range(n):
        result_b[i] += diff

    print('Yes')
    print(*result_a)
    print(*result_b)
    return


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
        input = """3
4 3 5
2 1 3
3 2 4"""
        output = """Yes
2 0 1
2 1 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
4 3 5
2 2 3
3 2 4"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
