# backtrackで実装したが解説はbit全部探索だった
def main():
    n = int(input())
    results = []
    
    def backtrack(current, l, r):
        if l < r:
            return
        if l+r == n:
            if r==l:
                results.append(current)
                return
            else:
                return
        
        backtrack(current+'(', l+1, r)    
        backtrack(current+')', l, r+1)    
    
    backtrack('', 0, 0)
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()
