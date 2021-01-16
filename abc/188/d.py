import sys
from io import StringIO
import unittest
import collections


def resolve():
    n, C = list(map(int, input().split()))
    events = []  # (happen_date, service_id, 'start' or 'end')
    service_costs = []

    for i in range(n):
        a, b, c = list(map(int, input().split()))
        events.append((a, i, 'start'))
        events.append((b+1, i, 'end'))
        service_costs.append(c)

    events.sort(key=lambda x: x[0])

    od = collections.OrderedDict()

    cost = 0
    cur_date = 0
    for date, service_id, se in events:
        if date not in od:
            od[date] = 0

        if se == 'start':
            od[date] += service_costs[service_id]
        elif se == 'end':
            od[date] -= service_costs[service_id]
        else:
            raise Exception('error')

    accum = 0
    result = 0
    prev_date = 0
    for k, v in od.items():
        pass_date = k - prev_date
        if accum < C:
            result += accum * pass_date
        else:
            result += C * pass_date
        accum += v
        prev_date = k
        # print(k, accum)
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
        input = """2 6
1 2 4
2 2 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """163089627821228"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """88206004785464"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
