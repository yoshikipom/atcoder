import collections


def main():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))    
    
    result = 0
    l = 0
    r = 0
    num_of_type = 1
    d = collections.defaultdict(int)
    d[A[l]] += 1
    
    while True:
        # print(l, r, num_of_type, result, d)
        if num_of_type > k:
            # print('l++')
            d[A[l]]-=1
            if d[A[l]]==0:
                num_of_type-=1
                del d[A[l]]
            l+=1
            if l == n:
                break
            continue
        
        else:
            # print('r++')
            result = max(result, r-l+1)
            
            r+=1
            if r == n:
                break
            if d[A[r]] == 0:
                num_of_type+=1
            d[A[r]]+=1
        
        
    print(result)        

if __name__ == '__main__':
    main()
