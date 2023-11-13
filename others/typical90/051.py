import bisect
from collections import defaultdict


def main():
    n, k, p = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    mid = n//2
    A1 = A[:mid]
    A2 = A[mid:]
    d1 = defaultdict(list)
    for bit in range(1<<len(A1)):
        cnt = 0
        total = 0
        for i in range(len(A1)):
            if 1<<i&bit:
                cnt+=1
                total += A1[i]
        d1[cnt].append(total)
    d2 = defaultdict(list)
    for bit in range(1<<len(A2)):
        cnt = 0
        total = 0
        for i in range(len(A2)):
            if 1<<i&bit:
                cnt+=1
                total += A2[i]
        d2[cnt].append(total)
    
    for _, arr in d2.items():
        arr.sort()
        
    result = 0
    for num, arr in d1.items():
        if num > k:
            continue
        for a in arr:
            arr2 = d2[k-num]
            index = bisect.bisect_right(arr2, p-a)
            # print(num, a, arr2, index)
            result += index
            
    # print(d1)                
    # print(d2)                
    print(result)
        
        
if __name__ == '__main__':
    main()
