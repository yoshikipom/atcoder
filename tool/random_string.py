import string
import random

def rand_alphabet(n):
    s = []
    for _ in range(n):
        c = random.choice(string.ascii_lowercase)
        s.append(c)
    return ''.join(s)

n = random.randint(4, 10)
s = rand_alphabet(n)
print(n)
print(s)
