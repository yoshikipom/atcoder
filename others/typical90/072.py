dirs = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
)

def main():
    h, w = list(map(int, input().split()))
    A = []
    for _ in range(h):
        A.append(input())
    
    seen = set()
    result = -1
    
    def backtrack(i,j,si,sj):
        nonlocal result
        seen.add((i,j))
        for di, dj in dirs:
            next_i = i + di
            next_j = j + dj
            if next_i==si and next_j==sj and len(seen)>2:
                result = max(result, len(seen))
            if not 0<=next_i<h or not 0<=next_j<w:
                continue
            if A[next_i][next_j] == '#':
                continue
            if (next_i, next_j) in seen:
                continue
            backtrack(next_i, next_j, si, sj)
        seen.remove((i,j))
    
    for i in range(h):
        for j in range(w):
            if A[i][j] == '#':
                continue
            backtrack(i,j,i,j)
    
    print(result)


if __name__ == '__main__':
    main()
