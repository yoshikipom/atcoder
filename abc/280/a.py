def main():
    h, w = list(map(int, input().split()))
    M = []
    for i in range(h):
        M.append(input())
        
    result = 0
    for s in M:
        for c in s:
            if c == '#':
                result += 1
                
    print(result)
            

if __name__ == '__main__':
    main()
