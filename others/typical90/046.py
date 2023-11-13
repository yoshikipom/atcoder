from collections import defaultdict


def main():
    n = int(input())
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(n):
        a = A[i]
        b = B[i]
        c = C[i]
        d1[a%46] += 1
        d2[b%46] += 1
        d3[c%46] += 1
        
    result = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i+j+k)%46 != 0:
                    continue
                # print("result", i, j, k)
                result += d1[i]*d2[j]*d3[k]
    
    print(result)
    # print(d1)
    # print(d2)
    # print(d3)
    

if __name__ == '__main__':
    main()
