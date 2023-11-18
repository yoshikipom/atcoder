from collections import defaultdict

def main():
    n, q = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(n):
        C[i] -= 1
    Q = []
    for i in range(q):
        Q.append(list(map(int, input().split())))
    
    S = [None] * n
    for i in range(n):
        S[i] = set()
        S[i].add(C[i])
        
    for a, b in Q:
        a-=1
        b-=1
        if len(S[b]) < len(S[a]):
            S[a], S[b] = S[b], S[a]
        for item in S[a]:
            S[b].add(item)
        S[a] = set()
        print(len(S[b]))
        
        


if __name__ == '__main__':
    main()
