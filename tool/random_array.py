import itertools
import string
import random
n = random.randint(4, 10)
A = [random.randint(1, 20) for i in range(n)]

# unique
# A = []
# seen = set()
# while len(A) < n:
#     num = random.randint(1, n*10)
#     if num in seen:
#         continue
#     seen.add(num)
#     A.append(num)

print(n)
print(*A)
