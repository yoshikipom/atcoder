import collections

def main():
    q = int(input())
    
    queue = collections.deque()
    for _ in range(q):
        t, x = list(map(int, input().split()))
        if t == 1:
            queue.appendleft(x)
        elif t == 2:
            queue.append(x)
        elif t == 3:
            print(queue[x-1])
        else:
            raise Exception('error')
    


if __name__ == '__main__':
    main()
