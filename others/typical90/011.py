# 小課題1,2のみ達成

from itertools import product


def main():
    n = int(input())
    DCS = []
    for i in range(n):
        DCS.append(list(map(int, input().split())))
        
    DCS.sort(key=lambda x:x[0]) # order by deadline asc
    
    # print(DCS)
    result = 0
        
    for p in product([True, False], repeat=n):
        free_day = 1
        total_s = 0
        possible = True
        for i in range(n):
            if p[i]:
                d, c, s = DCS[i]
                if free_day + c > d:
                    possible = False
                    break
                free_day += c
                total_s += s
        if possible:
            result = max(result, total_s)  
            # print(p, total_s)
        
    print(result)
                
        


if __name__ == '__main__':
    main()
