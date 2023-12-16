from collections import defaultdict
import copy


def main():
    n = int(input())
    tx = []
    for _ in range(n):
        tx.append(list(map(int, input().split())))
        
    d = defaultdict(int)
    result = []
    for t, x in tx[::-1]:
        if t == 1:
            if d[x] > 0:
                d[x]-=1
                result.append(1)
            else:
                result.append(0)
        else:
            d[x]+=1
    
    if max(d.values()) != 0:
        print(-1)
        return
            
    arr = copy.copy(result)
    cnt = 0
    max_cnt = 0
    for t, x in tx:
        if t == 1:
            action = arr.pop()
            if action == 1:
                cnt+=1
        else:
            cnt-=1
        max_cnt = max(max_cnt, cnt)
        
    print(max_cnt)
    print(*result[::-1])
        
    


if __name__ == '__main__':
    main()
