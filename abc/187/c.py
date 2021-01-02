import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    S = [input() for _ in range(n)]

    done1 = set()
    done2 = set()
    for s in S:
        if s.startswith('!'):
            done1.add(s[1:])
        else:
            done2.add(s)

    done = done1 & done2
    # print(done1)
    # print(done2)
    # print(done)
    if done:
        print(list(done)[0])
    else:
        print('satisfiable')


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
        input = """6
a
!a
b
!c
d
!d"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray"""
        output = """satisfiable"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
