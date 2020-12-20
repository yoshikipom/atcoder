n = int(input())


def is_valid(num):
    if '7' in str(num):
        return False
    if '7' in oct(num):
        return False
    return True


count = 0
for i in range(1, n+1):
    if is_valid(i):
        count += 1

print(count)
