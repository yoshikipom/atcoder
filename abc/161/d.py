from collections import deque

if __name__ == "__main__":
    K = int(input())
    runruns = []

    queue = deque()
    for i in range(1, 10):
        queue.appendleft(str(i))
        runruns.append(str(i))

    while len(runruns) < K:
        cur = queue.pop()
        for diff in [-1, 0, 1]:
            right = cur[-1]
            if (right == '0' and diff == -1) or (right == '9' and diff == 1):
                continue
            next_right = str(int(right) + diff)
            next_cur = cur + next_right
            runruns.append(next_cur)
            queue.appendleft(next_cur)

    runruns = list(map(int, runruns))
    # runruns.sort()
    # print(runruns)
    print(runruns[K-1])
