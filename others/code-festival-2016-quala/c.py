def char_to_num(char):
    return ord(char) - ord('a')


def num_to_char(num):
    return chr(num + ord('a'))


def main():
    s = input()
    k = int(input())
    
    result = []
    
    for i in range(len(s)):
        if i == len(s)-1:
            num = (char_to_num(s[i])+k)%26
            result.append(num_to_char(num))
            # print(num)
            break
            
        lenth_to_a = 26 - char_to_num(s[i])
        # print(lenth_to_a, k)
        if s[i] != 'a' and lenth_to_a <= k:
            result.append('a')
            k-=lenth_to_a
        else:
            result.append(s[i])
    
    print(''.join(result))
    

if __name__ == '__main__':
    main()
