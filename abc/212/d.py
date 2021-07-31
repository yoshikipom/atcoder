import sys
from io import StringIO
import unittest
import itertools
import heapq

def resolve():
    Q = int(input())

    # A = [0 for i in range(Q)]
    # B = [0 for i in range(Q)]
    # RECORD = []

    # for i in range(Q):
    #     s = input()
    #     if s.startswith('1') or s.startswith('2'):
    #         op, x = s.split()
    #         x = int(x)
    #         if op == '1':
    #             A[i] = x
    #         elif op == '2':
    #             B[i] = x
    #     else:
    #         RECORD.append(i)


    # C = list(itertools.accumulate(reversed(B)))
    # C.reverse()
    # D = [0 for i in range(Q)]

    # for i in range(Q):
    #     if A[i] != 0:
    #         A[i] += C[i]

    # diff = C[-1]
    # for i in range(Q):
    #     if A[i] == 0:
    #         continue

    # print(A)
    # print(B)
    # print(C)

    A = []

    diff = 0
    for i in range(Q):
        s = input()
        if s.startswith('1') or s.startswith('2'):
            op, x = s.split()
            x = int(x)
            if op == '1':
                heapq.heappush(A, x-diff)
            elif op == '2':
                diff += x
        else:
            a = heapq.heappop(A)
            print(a+diff)
        
        # print(i, diff, A)




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
        input = """5
1 3
1 5
3
2 2
3"""
        output = """3
7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 1000000000
2 1000000000
2 1000000000
2 1000000000
2 1000000000
3"""
        output = """5000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
