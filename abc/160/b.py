if __name__ == "__main__":
    X = int(input())
    U = 0
    U += (X // 500) * 1000
    X = X % 500
    U += (X // 5) * 5

    print(U)
