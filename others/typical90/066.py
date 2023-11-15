def main():
    n = int(input())
    L = [0]
    R = [0]
    for _ in range(n):
        l, r = list(map(int, input().split()))
        L.append(l)
        R.append(r)
        
    result = 0
    for i in range(1,n+1):
        l1, r1 = L[i], R[i]
        for j in range(i+1,n+1):
            l2, r2 = L[j], R[j]
            cnt = 0
            all_cnt = 0
            for a in range(l1, r1+1):
                for b in range(l2, r2+1):
                    all_cnt += 1
                    if a > b:
                        cnt+=1
            result += cnt/all_cnt
    
    print(result)        

    


if __name__ == '__main__':
    main()
