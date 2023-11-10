def segfunc(x,y):
    return max(x,y)

IDE_ELE = -1

class SegTree:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def add(self,k,x):
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def update(self,k,x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def query(self,l,r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

def main():
    w, n = list(map(int, input().split()))
    LRV = [None]
    for _ in range(n):
        LRV.append(list(map(int, input().split())))
        
    dp = [-1 for _ in range(w+1)] # value = sum of v at maximum
    for i in range(n+1):
        dp[0] = 0
    
    A = [-1] * (w+1)
    A[0] = 0
    seg = SegTree(A, segfunc, IDE_ELE)
    
    for i in range(1,n+1):
        l, r, v = LRV[i]
        for j in range(1,w+1)[::-1]:
            if j-l<0:
                break
            max_val = seg.query(max(0,j-r), j-l+1)
            # print(j, j-r, j-l, max_val)
            if max_val == -1:
                continue
            next_v = max_val+v
            if dp[j] < next_v:
                dp[j] = next_v
                seg.update(j, next_v)
                
        # print(*dp)
        # print(Counter(dp))
        # print()
    
    # for row in dp:
    #     # print(*row)
    #     print(Counter(row))
    #     print()
        
    result = dp[-1]
    if result == -1:
        print(-1)
    else:
        print(result)
        

if __name__ == '__main__':
    main()
