from collections import defaultdict


def main():
    n = int(input())
    s = input()
    prev = None
    cnt = 0
    d = defaultdict(int)
    
    for c in s:
        if prev != c:
            cnt = 1
            prev = c
        else:
            cnt += 1
        d[c] = max(d[c], cnt)
        
    result = 0
    for k, v in d.items():
        result += v
            
    print(result)
        


if __name__ == '__main__':
    main()
