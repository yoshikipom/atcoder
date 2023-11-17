import itertools


def main():
    n = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    if total % 10 != 0:
        print('No')
        return
    goal = total // 10
    
    B = A + A
    
    current_sum = 0
    l = 0
    r = 0
    
    while l < len(B) and r < len(B):
        if current_sum > goal:
            current_sum-=B[l]
            l+=1
        elif current_sum == goal:
            print('Yes')
            return
        else:
            current_sum+=B[r]
            r+=1
    
    print('No')
        
    

if __name__ == '__main__':
    main()
