MOD = 10**9+7


def main():
    n, q = list(map(int, input().split()))
    xyzw = [list(map(int, input().split())) for _ in range(q)]
    result = 1

    for i in range(60):
        cnt = 0
        for bit in range(1 << n): # bit to decide which items in A can be used.
            for x, y, z, w in xyzw:
                x -= 1
                y -= 1
                z -= 1
                if (bit>>x)&1 | (bit>>y)&1 | (bit>>z)&1 == (w>>i)&1:
                    continue
                break
            else:
                cnt+=1
    
        result *= cnt
        result %= MOD

    print(result)

if __name__ == '__main__':
    main()
