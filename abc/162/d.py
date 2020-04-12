if __name__ == "__main__":
    N = int(input())
    S = input()

    R = set()
    G = set()
    B = set()
    for i in range(N):
        if S[i] == 'R':
            R.add(i)
        elif S[i] == 'G':
            G.add(i)
        elif S[i] == 'B':
            B.add(i)

    except_cnt = 0
    for w in range(1, N//2 + 1):
        for i in range(N):
            j = i + w
            k = j + w
            if i in R and j in G and k in B:
                except_cnt += 1
            if i in R and j in B and k in G:
                except_cnt += 1
            if i in B and j in R and k in G:
                except_cnt += 1
            if i in B and j in G and k in R:
                except_cnt += 1
            if i in G and j in B and k in R:
                except_cnt += 1
            if i in G and j in R and k in B:
                except_cnt += 1

    print(len(R) * len(G) * len(B) - except_cnt)
