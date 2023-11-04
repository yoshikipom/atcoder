def main():
    A = []
    for _ in range(9):
        A.append(list(map(int, input().split())))
        
    for i in range(9):
        s = set()
        for j in range(9):
            s.add(A[i][j])
        if len(s) != 9:
            return 'No'
    
        
    for j in range(9):
        s = set()
        for i in range(9):
            s.add(A[i][j])
        if len(s) != 9:
            return 'No'
    
    D = [
        (0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6),
         ]
    for ii, jj in D:
        s = set()
        for i in range(3):
            for j in range(3):
                s.add(A[ii+i][jj+j])
        if len(s) != 9:
            return 'No'

    return 'Yes'

if __name__ == '__main__':
    result = main()
    print(result)
