class Person:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def solve():
    N = int(input())

    A = [-1 for i in range(2*N)]
    B = [-1 for i in range(2*N)]
    P = {}
    not_start = set()
    not_end = set()

    for i in range(N):
        a, b = list(map(int, input().split()))

        if a != -1:
            A[a-1] = i
        else:
            not_start.add(i)
        if b != -1:
            B[b-1] = i
        else:
            not_end.add(i)
        P[i] = Person(a-1, b-1)

    for index, person in P.items():
        if person.start >= person.end:
            return False

    for i in range(N):
        p1 = P[i]
        for j in range(i + 1, N):
            p2 = P[j]
            if p1.start <= p2.start and p2.end <= p1.end:
                return False

    for i in range(N+2):
        if B[i] != -1:

    return True


if __name__ == "__main__":
    if solve():
        print('Yes')
    else:
        print('No')
