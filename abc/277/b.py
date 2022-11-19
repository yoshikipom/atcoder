def main():
    n = int(input())
    S = [None] * n
    for i in range(n):
        S[i] = input()
    
    if len(set(S)) != n:
        print('No')
        return
    
    for i in range(n):
        if S[i][0] not in ['H', 'D', 'C', 'S']:
            print('No')
            return
        if S[i][1] not in ['A', '2', '3', '4', '5', '6','7', '8', '9', 'T', 'J', 'Q', 'K']:
            print('No')
            return
    
    print('Yes')
    return



if __name__ == '__main__':
    main()
