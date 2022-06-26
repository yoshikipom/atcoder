from pydoc import resolve
import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    LRs = []
    for i in range(n):
        LRs.append(list(map(int, input().split())))

    LRs.sort(key=lambda x:x[0])

    count = 1
    cur_l = LRs[0][0]
    cur_r = LRs[0][1]
    for (l, r) in LRs[1:]:
        # print(cur_r, l, r)
        if cur_r >= l:
            # join
            # print("option 1")
            cur_r = max(cur_r, r)
        else:
            # create new section
            # print("option 2")
            count += 1
            print(cur_l, cur_r)
            cur_l = l
            cur_r = r
    
    print(cur_l, cur_r)
    # print(count)
        


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
10 20
20 30
40 50"""
        output = """10 30
40 50"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 40
30 60
20 50"""
        output = """10 60"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
