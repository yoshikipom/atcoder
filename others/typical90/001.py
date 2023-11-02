def main():
    n, l = list(map(int, input().split()))
    k = int(input())
    A = list(map(int, input().split()))
    A += [l]

    allowed = 0
    deneid = l

    while deneid - allowed > 1:
        mid = (allowed + deneid) // 2
        # print(f'mid: {mid}')
        if achievable(n, k, A, mid):
            # print('True')
            allowed = mid
        else:
            # print('False')
            deneid = mid
    print(allowed)
    

def achievable(n, k, A, score) -> bool:
    prev_cut = 0
    cut_cnt = 0
    for i in range(n+1):
        if A[i] - prev_cut >= score:
            # print(f'cut {i}')
            prev_cut = A[i]
            cut_cnt += 1
    
    return k+1 <= cut_cnt 
        
            
if __name__ == '__main__':
    main()
