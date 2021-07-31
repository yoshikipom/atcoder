import sys
from io import StringIO
import unittest


def resolve():
    strong = True
    X = input()

    s = set()
    for c in X:
        s.add(c)

    if len(s) == 1:
        strong = False

    d = 0
    for i in range(3):
        # print(int(X[i+1]), (int(X[i]) + 1) % 10)
        if int(X[i+1]) == (int(X[i]) + 1) % 10:
            d += 1
    if d == 3:
        strong = False

    if strong:
        print('Strong')
    else:
        print('Weak')


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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
