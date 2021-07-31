import sys
from io import StringIO
import unittest
import copy


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    d = {}
    for b in B:
        if b not in d:
            d[b] = 0
        d[b] += 1

    nums = set()
    for b in B:
        nums.add(A[0] ^ b)
    nums = list(nums)
    nums.sort()

    result = []
    for x in nums:
        can = True
        d2 = copy.copy(d)
        for a in A:
            b = a ^ x
            if b not in d2:
                can = False
                break
            d2[b] -= 1
            if d2[b] == 0:
                d2[b]

        if can:
            result.append(x)

    print(len(result))
    for r in result:
        print(r)


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
1 2 3
6 4 7"""
        output = """1
5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 1
0 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """24
14911005 70152939 282809711 965900047 168465665 337027481 520073861 20800623 934711525 944543101 522277111 580736275 468493313 912814743 99651737 439502451 365446123 198473587 285587229 253330309 591640417 761745547 247947767 750367481
805343020 412569406 424258892 329301584 123050452 1042573510 1073384116 495212986 158432830 145726540 623594202 836660574 380872916 722447664 230460104 718360386 620079272 109804454 60321058 38178640 475708360 207775930 393038502 310271010"""
        output = """8
107543995
129376201
139205201
160626723
312334911
323172429
481902037
493346727"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
