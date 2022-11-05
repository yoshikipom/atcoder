def main():
    S = input()
    result = -1
    for i in range(len(S)):
        if S[i] == 'a':
            result = i + 1
    print(result)



if __name__ == '__main__':
    main()
