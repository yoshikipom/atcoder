def left_1_index(s):
    for i in range(len(s)):
        if s[i] == '1':
            return i
    return None


def right_1_index(s):
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            return i
    return None


def solve_contain_1(k, s):
    count_1 = 0
    target = None
    for item in s.split('0'):
        if '1' in item:
            target = item
            count_1 +=1
    if count_1 != 1:
        return False
    # print('debug a')

    
    if len(target) == k:
        return True
    # print('debug b')
    
    l = left_1_index(target)
    r = right_1_index(target)
    if r - l + 1 > k:
        return False

    # print('debug c')
    return l == 0 or r == len(target) - 1


def solve_no_1(k, s):
    if s.count('?'*k) !=1:
        return False
    
    item = list(filter(lambda x: x != '', s.split('0')))[0]
    return item == '?'*k


def solve(n, k, s):
    if '1' in s:
        # print('debug case 1')
        return solve_contain_1(k, s)
    else:
        # print('debug case 2')
        return solve_no_1(k, s)


def main():
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().split()))
        # n, k = 5, 3
        s = input()
        if solve(n, k, s):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
