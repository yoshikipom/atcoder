import math


def main():
    h, w = list(map(int, input().split()))
    if h == 1:
        print(w)
    elif w == 1:
        print(h)
    else:
        print(math.ceil(h/2) * math.ceil(w/2))


if __name__ == '__main__':
    main()
