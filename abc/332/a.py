def main():
    n, s, k = list(map(int, input().split()))
    total = 0
    for _ in range(n):
        p, q = list(map(int, input().split()))
        total += p*q
        
    if total < s:
        total+=k
    
    print(total)


if __name__ == '__main__':
    main()
