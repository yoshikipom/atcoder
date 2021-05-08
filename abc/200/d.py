import sys
from io import StringIO
import unittest
from copy import copy


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    divs = [set() for i in range(200)]

    for i in range(n):
        a = A[i]
        if divs[a % 200] and list(divs[a % 200])[0] != i + 1:
            print('Yes')
            print(1, *divs[a % 200])
            print(1, i + 1)
            return
        divs[a % 200].add(i + 1)

    for i in range(200):
        if not divs[i]:
            continue

        for j in range(i+1, 200):
            if not divs[j]:
                continue

            value = copy(divs[i]) | copy(divs[j])
            target = 0
            for s in value:
                target += A[s-1]
            target %= 200
            if divs[target]:
                B = sorted(list(divs[target]))
                C = sorted(list(value))
                if len(B) != len(C) or B != C:
                    print('Yes')
                    print(len(B), *B)
                    print(len(C), *C)
                    return
                else:
                    continue

            divs[target] = value
            # print(*divs)

    print('No')


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[: -1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """5
180 186 189 191 218"""
        output = """Yes
1 1
2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
123 523"""
        output = """Yes
1 1
1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
2013 1012 2765 2021 508 6971"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
