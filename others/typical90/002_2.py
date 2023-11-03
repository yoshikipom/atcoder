def main():
    n = int(input())
    results = []
    
    if n % 2 == 1:
        return
    
    for bit in range(1<<n):
        s = ''
        for i in range(n)[::-1]:
            if bit  & 1 << i:
                s += ')'
            else:
                s += '('
        if check(s):
            results.append(s)
    
    # results.sort()
    print('\n'.join(results))
 
def check(s) -> bool:
    # TODO: scoreを +1 or -1 して 0以上か判定する方がベター
    l = 0
    r = 0
    for c in s:
        if c == '(':
            l += 1
        else:
            r += 1
        if l < r:
            return False
    return l == r
        
    

if __name__ == '__main__':
    main()
