result = []
result2 = []
def main():
    
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    Q = []
    for i in range(q):
        Q.append(list(map(int, input().split())))

    updated = set()        

    last_all_update_number = None
    for query in Q:
        if query[0] == 1:
            last_all_update_number = query[1]
            updated = set()
        elif query[0] == 2:
            if not last_all_update_number:
                A[query[1]-1] += query[2]
            elif query[1]-1 in updated:
                A[query[1]-1] += query[2]
            else:
                updated.add(query[1]-1)
                A[query[1]-1] = last_all_update_number + query[2]
        else:
            if not last_all_update_number:
                result.append(A[query[1]-1])
            elif query[1]-1 in updated:
                result.append(A[query[1]-1])
            else:
                result.append(last_all_update_number)
        # print(query, A, last_all_update_number)


def main2():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    Q = []
    for i in range(q):
        Q.append(list(map(int, input().split())))

    for query in Q:
        if query[0] == 1:
            for i in range(n):
                A[i] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        else:
            result2.append(A[query[1]-1])


if __name__ == '__main__':
    main()
    for r in result:
        print(r)

    # main2()
    # print(result)
    # print(result2)
