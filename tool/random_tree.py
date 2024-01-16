import random
from atcoder.dsu import DSU
n = random.randint(4, 10)

uf = DSU(n+1)
edges = []
for edge_index in range(n-1):
    while True:
        # 0-index
        # a = random.randint(0, n-1)
        # b = random.randint(0, n-1)
        
        # 1-index
        a = random.randint(1, n)
        b = random.randint(1, n) 
        
        if a == b or uf.same(a,b):
            continue
        uf.merge(a,b)
        edges.append((a,b))
        break
        
print(n)
for edge in edges:
    print(*edge)
