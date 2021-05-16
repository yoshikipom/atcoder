import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())

    data = []
    for _ in range(n):
        s, t = input().split()
        t = int(t)
        data.append((s, t))

    data.sort(key=lambda x: x[1], reverse=True)

    print(data[1][0])


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
Everest 8849
K2 8611
Kangchenjunga 8586"""
        output = """K2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
Kita 3193
Aino 3189
Fuji 3776
Okuhotaka 3190"""
        output = """Kita"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390"""
        output = """QCFium"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
