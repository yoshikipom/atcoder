import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    s = input()
    q = int(input())

    s_l = list(s[:n])
    s_r = list(s[n:])

    l = s_l
    r = s_r

    for _ in range(q):
        t, a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        if t == 1:
            if a < n:
                char_a = l[a]
            else:
                char_a = r[a-n]
            if b < n:
                char_b = l[b]
            else:
                char_b = r[b-n]

            if a < n:
                l[a] = char_b
            else:
                r[a-n] = char_b
            if b < n:
                l[b] = char_a
            else:
                r[b-n] = char_a
        else:
            l, r = r, l

        # print(l+r)

    print("".join(l+r))


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
        input = """2
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
