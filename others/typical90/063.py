

from collections import defaultdict


def main():
    h, w = list(map(int, input().split()))
    A = []
    for _ in range(h):
        A.append(list(map(int, input().split())))
        
    result = 0
    for bit in range(1<<h):
        d = defaultdict(int)
        hight = bin(bit).count('1')
        for j in range(w):
            s = set()
            for i in range(h):
                if not 1 << i & bit:
                    continue
                s.add(A[i][j])
            if len(s) == 1:
                d[s.pop()] += 1
        
        for k, v in d.items():
            result = max(result, hight*v)
    
    print(result)
                


if __name__ == '__main__':
    main()
