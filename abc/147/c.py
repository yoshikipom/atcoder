

N = int(input())
A = []
for i in range(N):
    xy = []
    for j in range(int(input())):
        x, y = map(int, input().split())
        xy.append([x, y])
    A.append(xy)

result = 0
# 試行
for i in range(2 ** N):
    proof = {}
    mismatch = False
    count = 0
    # if i != 3:
    #     continue
    # 各自の発言をチェックしてカウント
    for j in range(N):
        # 試行でビットが立っている人だけ本当のことをいったと仮定
        if (i >> j) & 1:
            for xy in A[j]:
                # Aの発言をproofにいれる。矛盾があったらmismatchをtrueに
                # 発言した人が今までの証拠と矛盾した場合
                if xy[0] in proof and xy[1] != proof[xy[0]]:
                    print("debug1")
                    mismatch = True
                    break
                # ほんとといった人が本当リストにいない場合
                if xy[1] == 1 and not (i >> (xy[0] - 1)) & 1:
                    print("debug2")
                    mismatch = True
                    break
                # うそといった人が本当リストにいる場合
                if xy[1] == 0 and (i >> (xy[0] - 1)) & 1:
                    print("debug3")
                    mismatch = True
                    break

                proof[xy[0]] = xy[1]

            # 全発言入れられたらカウント
            if mismatch:
                break
            # print(j)
            count += 1

    # if mismatch:
    #     break
    print('i:{}, count:{}'.format(bin(i), count))
    result = max(result, count)

print(result)
