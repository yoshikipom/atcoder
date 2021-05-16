import sys
from io import StringIO
import unittest
import math
import itertools
import copy


def count(nums):
    d = {}
    for i in range(10):
        d[i] = 0

    for num in nums:
        d[num] += 1

    div = 1
    for i in range(10):
        if d[i] != 0:
            div *= math.factorial(d[i])

    return math.factorial(4)//div


def resolve():
    s = input()
    required = []
    option = []

    for i in range(len(s)):
        c = s[i]
        if c == 'o':
            required.append(i)
        elif c == '?':
            option.append(i)

    ro = required + option

    n_required = len(required)
    n_option = len(option)
    n_ro = len(ro)

    if n_required >= 5:
        result = 0
    elif n_required == 4:
        result = math.factorial(4)
    elif n_required == 3:
        result = 0
        for i in range(n_ro):
            nums = copy.copy(required) + [ro[i]]
            result += count(nums)
    elif n_required == 2:
        result = 0
        for i in range(n_ro):
            for j in range(i, n_ro):
                nums = copy.copy(required) + [ro[i], ro[j]]
                result += count(nums)
                # print(nums, result)
    elif n_required == 1:
        result = 0
        for i in range(n_ro):
            for j in range(i, n_ro):
                for k in range(j, n_ro):
                    nums = copy.copy(required) + [ro[i], ro[j], ro[k]]
                    result += count(nums)
                    # print(nums, result)
    elif n_required == 0:
        result = 0
        for i in range(n_ro):
            for j in range(i, n_ro):
                for k in range(j, n_ro):
                    for l in range(k, n_ro):
                        nums = copy.copy(required) + \
                            [ro[i], ro[j], ro[k], ro[l]]
                        result += count(nums)
                        # print(nums, result)

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
        input = """ooo???xxxx"""
        output = """108"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o?oo?oxoxo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """xxxxx?xxxo"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
