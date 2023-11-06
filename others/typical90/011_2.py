from itertools import product


def main():
    n = int(input())
    DCS = []
    d_max = 0
    for i in range(n):
        DCS.append(list(map(int, input().split())))
        d_max = max(d_max, DCS[-1][0])
        
    DCS.sort(key=lambda x:x[0]) # order by deadline asc
    
    # print(DCS)
    
    dp = [-1 for _ in range(d_max+1)]
    dp[0] = 0
    
    for i in range(n):
        d,c,s = DCS[i]
        # print(d,s,c)
        for booked_last_day in range(d_max+1)[::-1]:
            if dp[booked_last_day] == -1:
                continue
            if booked_last_day + c > d:
                continue
            dp[booked_last_day+c] = max(dp[booked_last_day+c],dp[booked_last_day]+s)
        # print(dp)
                
    print(max(dp))
    
if __name__ == '__main__':
    main()
