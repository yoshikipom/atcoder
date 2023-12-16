def main():
    s = input()
    t = input()
    
    arr = ['A', 'B', 'C', 'D', 'E']
    
    def dist(a, b):
        index = arr.index(a)
        r_dist = 0
        tmp = index
        while True:
            tmp+=1
            r_dist+=1
            if arr[tmp%5] == b:
                break
            
        l_dist = 0
        tmp = index
        while True:
            tmp-=1
            l_dist+=1
            if arr[tmp%5]==b:
                break
    
        return min(r_dist, l_dist)
    
    if dist(s[0], s[1]) == dist(t[0], t[1]):
        print('Yes')
    else:
        print('No')
    
    
    
    


if __name__ == '__main__':
    main()
