import random
from atcoder.dsu import DSU
n = random.randint(4, 10)

uf = DSU(n)
edges = []
seen = set()
while True:
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    
    if a == b:
        continue
    if (a,b) in seen or (b, a) in seen:
        continue
    seen.add((a,b))
    uf.merge(a,b)
    edges.append((a,b))
    
    if len(uf.groups()) == 1:
        break
        
print(n)
for edge in edges:
    # 0-index to 1-index
    edge = [val+1 for val in edge]
    
    print(*edge)
