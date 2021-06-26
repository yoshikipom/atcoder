import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    TLRS = []
    for i in range(n):
        tlr = list(map(int, input().split()))
        TLRS.append(tlr)

    result = 0
    for i in range(n):
        l_t, l_l, l_r = TLRS[i]
        if l_t == 1:
            l_min = l_l
            l_max = l_r
        elif l_t == 2:
            l_min = l_l
            l_max = l_r - 0.1
        elif l_t == 3:
            l_min = l_l + 0.1
            l_max = l_r
        elif l_t == 4:
            l_min = l_l + 0.1
            l_max = l_r - 0.1

        if l_min > l_max:
            continue

        for j in range(i+1, n):
            r_t, r_l, r_r = TLRS[j]
            if r_t == 1:
                r_min = r_l
                r_max = r_r
            elif r_t == 2:
                r_min = r_l
                r_max = r_r - 0.1
            elif r_t == 3:
                r_min = r_l + 0.1
                r_max = r_r
            elif r_t == 4:
                r_min = r_l + 0.1
                r_max = r_r - 0.1
            if r_min > r_max:
                continue

            if (l_min <= r_max and r_max <= l_max) or (l_min <= r_min and r_min <= l_max) or (r_min <= l_max and l_max <= r_max) or (r_min <= l_min and l_min <= r_max):
                # print(i, j, l_min, l_max, r_min, r_max)
                result += 1

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
        input = """3
1 1 2
2 2 3
3 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817"""
        output = """102"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
