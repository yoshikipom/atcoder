import sys
from io import StringIO
import unittest
from collections import deque


def resolve():
    n = int(input())
    d = {}
    for i in range(n):
        d[i] = []
    for i in range(n-1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        d[a].append(b)
        d[b].append(a)

    for i in range(n):
        tmp = d[i]
        tmp.sort()
        d[i] = deque(tmp)

    cur = 0
    results = [0]
    befores = {}
    befores[0] = True

    while True:
        # print('------')
        # print(cur)
        # print(d)
        # print(befores)
        # print(*results)

        if d[cur]:
            # while True:
                # if not d[cur]:
                #     cur = befores[cur]
                #     results.append(cur)
                #     continue
            tmp_cur = d[cur].popleft()
            if tmp_cur in befores:
                continue
                # if cur in befores:
                #     continue
                # else:
                #     break

            # 進める
            befores[tmp_cur] = cur
            cur = tmp_cur
            results.append(cur)
        else:
            if cur == 0:
                # 終了
                break
            else:
                # 戻る
                cur = befores[cur]
                results.append(cur)
                continue

    R = []
    for result in results:
        R.append(result+1)
    print(*R)

        


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
        input = """4
1 2
4 2
3 1"""
        output = """1 2 4 2 1 3 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2
1 3
1 4
1 5"""
        output = """1 2 1 3 1 4 1 5 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
