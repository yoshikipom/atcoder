if __name__ == "__main__":

    X, Y, A, B, C = map(int, input().split())

    Red = list(map(int, input().split()))
    Red.sort()
    Red = Red[::-1]
    Red = Red[:X]
    Green = list(map(int, input().split()))
    Green.sort()
    Green = Green[::-1]
    Green = Green[:Y]
    NoColor = list(map(int, input().split()))

    A = Red + Green + NoColor
    # print(A)
    A.sort(reverse=True)

    eaten = A[:X+Y]

    print(sum(eaten))
