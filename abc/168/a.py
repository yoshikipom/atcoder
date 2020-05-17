N = input()
last = int(N[-1])

hon_list = (2, 4, 5, 7, 9)
pon_list = (0, 1, 6, 8)
bon_list = [3]

if last in hon_list:
    print('hon')
elif last in pon_list:
    print('pon')
elif last in bon_list:
    print('bon')
else:
    raise Exception
