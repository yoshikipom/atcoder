import sys
from io import StringIO
import unittest
import math


def resolve():
    s = input()

    if s == '<' or s == '>':
        print(1)
        return

    upDownList = []
    count = 1
    before = s[0]
    c = None
    for i in range(1, len(s)):
        c = s[i]

        if c != before:
            if c == '>':
                upDownList.append(count)
            elif c == '<':
                upDownList.append(-1 * count)
            else:
                raise Exception()
            count = 0

        count += 1
        before = c

    if c == '<':
        upDownList.append(count)
    elif c == '>':
        upDownList.append(-count)
    else:
        raise Exception()
    # print(upDownList)

    beforeIsUp = False
    before = 0
    count = 0
    for i in range(len(upDownList)):
        upDown = upDownList[i]

        for i in range(abs(upDown)+1):
            count += i

        if beforeIsUp:
            if before > abs(upDown):
                count -= abs(upDown)
            else:
                count -= before

        if upDown > 0:
            beforeIsUp = True
            before = upDown
        else:
            beforeIsUp = False
        # print(count)

    print(count)


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
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """<>>><<><<<<<>>><"""
        output = """28"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
