from functools import lru_cache


@lru_cache(maxsize=100000)

def f(k):
    if k == 0:
        return 1
    return f(k//2) + f(k//3)

def main():
    n = int(input())

    print(f(n))

if __name__ == '__main__':
    main()
