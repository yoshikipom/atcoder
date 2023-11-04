from collections import deque


def c_index(c):
    return ord(c) - ord('a')


def c_chr(i):
    return chr(i+ord('a'))


def main():
    n, k = list(map(int, input().split()))
    s = input()
    
    m = [[None for _ in range(n)] for _ in range(26)]
    
    for j in range(n)[::-1]:
        c = s[j]
        for i in range(26):
            if c_index(c) == i:
                m[i][j] = j
            else:
                if j == n-1:
                    continue
                m[i][j] = m[i][j+1]
                
    # for row in m:
    #     print(*row)
    
    # greedy
    s = ''
    last_index = -1
    while len(s) < k:
        for chr_i in range(26):
            next_found = m[chr_i][last_index+1]
            # print(chr_i, next_found, s)
            if next_found == None:
                continue
            if n-next_found >= k-len(s):
                s += c_chr(chr_i)
                last_index = next_found
                break
    
    print(s)
    
        

if __name__ == '__main__':
    main()
