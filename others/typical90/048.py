import heapq


def main():
    n, k = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    
    Q = []
    for i in range(n):
        heapq.heappush(Q, (-B[i], i, False))
        
    result = 0
    for _ in range(k):
        # print(Q)
        minus_point, index, half_solved = heapq.heappop(Q)
        result += -minus_point
        if not half_solved:
            heapq.heappush(Q, (-(A[index]-B[index]), index, True))
    
    print(result)

if __name__ == '__main__':
    main()
