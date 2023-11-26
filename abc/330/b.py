def main():
    n, l, r = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    result = []
    for a in A:
        if a <= l:
            result.append(l)
        elif l < a and a < r:
            result.append(a)
        else:
            result.append(r)
    
    print(*result)
        


if __name__ == '__main__':
    main()
