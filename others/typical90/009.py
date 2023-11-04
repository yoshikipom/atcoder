import bisect
import math

# def calculate_angle_points(a, b, c):
#     ba = (a[0] - b[0], a[1] - b[1])  # Vector from point b to a
#     bc = (c[0] - b[0], c[1] - b[1])  # Vector from point b to c

#     cosine_angle = (ba[0] * bc[0] + ba[1] * bc[1]) / (math.sqrt(ba[0]**2 + ba[1]**2) * math.sqrt(bc[0]**2 + bc[1]**2))

#     angle = math.acos(cosine_angle)  # This will be in radian

#     return math.degrees(angle)

def calculate_angle_vecs(ba, bc):
    cosine_angle = (ba[0] * bc[0] + ba[1] * bc[1]) / (math.sqrt(ba[0]**2 + ba[1]**2) * math.sqrt(bc[0]**2 + bc[1]**2))

    angle = math.acos(cosine_angle)  # This will be in radian

    return math.degrees(angle)

def calculate_angle(vec):
    """Calculate the angle between the given vector and the x axis"""
    
    x, y = vec
    radian = math.atan2(y, x)
    
    # Convert the angle from radians to degrees
    degree = math.degrees(radian)
    
    return degree

def main():
    n = int(input())
    P = []
    for i in range(n):
        P.append(list(map(int, input().split())))
        
    P.sort()
    
    result = 0
    
    for mid in range(n):
        p_mid = P[mid]
        
        l_vecs = []
        for i in range(mid):
            p = P[i]
            vec = (p_mid[0]-p[0], p_mid[1]-p[1])
            l_vecs.append(vec)
        l_vecs.sort(key=lambda x:calculate_angle(x))
            
        r_vecs = []
        for i in range(mid+1, n):
            p = P[i]
            vec = (p[0]-p_mid[0], p[1]-p_mid[1])
            r_vecs.append(vec)
        r_vecs.sort(key=lambda x:calculate_angle(x))
        
        # print(mid, p_mid, l_vecs, r_vecs)
        
        if not r_vecs:
            continue
        
        for l_vec in l_vecs:
            l_angle = calculate_angle(l_vec)
            
            row = 0
            high = len(r_vecs)-1
            while high - row > 1:
                m = (row+high)//2
                if l_angle > calculate_angle(r_vecs[m]):
                    row = m
                else:
                    high = m
            l_vec_reverse = (-l_vec[0],-l_vec[1])
            tmp1 = calculate_angle_vecs(l_vec_reverse, r_vecs[row])
            tmp2 = calculate_angle_vecs(l_vec_reverse, r_vecs[high])
            result = max([result, tmp1, tmp2])
            # print(l_vec, r_vecs[row], tmp1, r_vecs[high], tmp2)
        
    print(result)

if __name__ == '__main__':
    main()
