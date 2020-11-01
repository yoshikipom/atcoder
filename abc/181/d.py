s = input()

nums = {}
for i in range(10):
    nums[i] = 0
for c in s:
    num = int(c)
    nums[num] += 1

result = False
if len(s) == 1:
    if nums[8] == 1:
        result = True
elif len(s) == 2:
    for i in range(10//8+1, 100//8+1):
        tmp_nums = {}
        tmp_num_s = str(8*i)
        tmp_result = True
        for c in tmp_num_s:
            tmp_c_num = int(c)
            if tmp_c_num not in tmp_nums:
                tmp_nums[tmp_c_num] = 0
            tmp_nums[tmp_c_num] += 1
        for k, v in tmp_nums.items():
            if nums[k] >= v:
                continue
            else:
                tmp_result = False
                break
        if tmp_result:
            # print(tmp_num_s)
            result = True
            break
else:
    for i in range(100//8+1, 1000//8+1):
        tmp_nums = {}
        tmp_num_s = str(8*i)
        tmp_result = True
        for c in tmp_num_s:
            tmp_c_num = int(c)
            if tmp_c_num not in tmp_nums:
                tmp_nums[tmp_c_num] = 0
            tmp_nums[tmp_c_num] += 1
        for k, v in tmp_nums.items():
            if nums[k] >= v:
                continue
            else:
                tmp_result = False
                break
        if tmp_result:
            # print(tmp_num_s)
            result = True
            break

if result:
    print('Yes')
else:
    print('No')
