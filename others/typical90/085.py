import collections

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    k = int(input())
    s = set()
    for a in make_divisors(k):
        rem = k//a
        for b in make_divisors(rem):
            c = rem // b
            s.add(tuple(sorted([a,b,c])))
            
    print(len(s))


if __name__ == '__main__':
    main()
