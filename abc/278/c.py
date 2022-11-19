def main():
    n, q = list(map(int, input().split()))
    follower_map = {}
    for i in range(q):
        t, a, b = list(map(int, input().split()))  
        if t == 1:
            if a not in follower_map:
                follower_map[a] = set()
            follower_map[a].add(b)
        if t == 2:
            if a in follower_map and b in follower_map[a]:
                follower_map[a].remove(b)
        if t == 3:
            if a in follower_map and b in follower_map and b in follower_map[a] and a in follower_map[b]:
                print('Yes')
            else:
                print('No')

    


if __name__ == '__main__':
    main()
