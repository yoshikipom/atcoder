def main():
    n, l = list(map(int, input().split()))
    A = list(map(int, input().split()))
    result = 0
    for a in A:
        if a >= l:
            result+=1
            
    print(result)
        


if __name__ == '__main__':
    main()
