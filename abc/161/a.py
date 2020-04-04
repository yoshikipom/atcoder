if __name__ == "__main__":
    x, y, z = list(map(int, input().split()))
    x, y = y, x
    x, z = z, x
    print('{} {} {}'.format(x, y, z))
