letters = 'abcdefghijklmnopqrstuvwxyz'

N = int(input())


def solve(n):
    result = ''
    while n > 0:
        letter_index = n % 26
        result = letters[letter_index-1] + result
        n //= 26
        if letter_index == 0:
            n -= 1

    print(result)


solve(N)
