import math

def main():
    T = int(input())
    L, X, Y = list(map(int, input().split()))
    Q = int(input())
    E = []
    for _ in range(Q):
        # E.append(int(input()))
        e = int(input())
        
        e %= T
        raddian = 2 * math.pi * (e/T)
        y = L/2*(-math.sin(raddian))
        z = L/2*(math.sin(raddian-math.pi/2)) + L/2

        length = (X**2 + (Y-y)**2 + z**2) ** (1/2)
        distance = (X**2 + (Y-y)**2) ** (1/2)
        rad = math.acos(distance/length)
        
        # print(math.degrees(raddian),y,z , length, distance)
        print(math.degrees(rad))
        

if __name__ == '__main__':
    main()
