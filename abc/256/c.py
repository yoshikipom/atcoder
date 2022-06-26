import sys
from io import StringIO
import unittest
from itertools import combinations_with_replacement

def candidate_rows(sum):
    rows = []
    for x in combinations_with_replacement(range(sum+1), 2):
        st = 0
        seq = []
        for i in x:
            seq.append(i - st)
            st = i
        seq.append(sum - i)
        if 0 not in seq:
            rows.append(seq)
    # print('sum', sum, 'rows', rows)
    return rows

def resolve():

    A = list(map(int, input().split()))
    H = A[:3]
    W = A[3:]

    # print(H, W)

    result = 0
    M = []

    R1_list = candidate_rows(H[0])
    R2_list = candidate_rows(H[1])
    R3_list = candidate_rows(H[2])

    # prepare the matrix
    for R1 in R1_list:
        for R2 in R2_list:
            for R3 in R3_list:
                # test
                sum1 = R1[0] + R2[0] + R3[0]
                sum2 = R1[1] + R2[1] + R3[1]
                sum3 = R1[2] + R2[2] + R3[2]
                if sum1 == W[0] and sum2 == W[1] and sum3 == W[2]:
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
        input = """3 4 6 3 3 7"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 5 6 7 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 13 10 6 13 9"""
        output = """120"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 25 30 22 29 24"""
        output = """30613"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
