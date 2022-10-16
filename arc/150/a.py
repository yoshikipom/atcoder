def create_can_be_list(s,k):
    if '0' not in s:
        return [s]

    ss = s.split('0')
    return list(filter(lambda x: x != '' and len(x) >= k, ss))


def has_valid_1(s):
    if '0' not in s:
        return True

    ss = s.split('0')
    count_devided_1 = 0
    # print(ss)
    for splited in ss:
        if '1' in splited:
            count_devided_1 += 1
    
    return count_devided_1 == 1 or count_devided_1 == 0

def valid_questions(s, k):
    ss = s.split('0')
    applicable_count = 0
    for splited in ss:
        if len(splited) >= k:
            return False
        if len(splited) == k:
            applicable_count += 1
    return applicable_count == 1
        
def fetch_main_part(s):
    ss = s.split('0')
    for splited in ss:
        if '1' in splited:
            return splited


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
        

def solve(n, k, s):
    can_be_list = create_can_be_list(s, k)
    # print(can_be_list)
    if len(can_be_list) >= 2:
        return False

    if not has_valid_1(s):
        return False

    main_part = fetch_main_part(s)
    # print(main_part)

    if not main_part:
        return valid_questions(s, k)

    if len(main_part) == k:
        return True
    if len(main_part) < k:
        return False

    l = left_1_index(main_part)
    r = right_1_index(main_part)
    if l == None or r == None:
        return False
    
    if r - l >= k:
        return False

    return l == 0 or r == len(main_part) - 1

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
