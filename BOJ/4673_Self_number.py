def self_num(num):
    result_ = 0
    str_num = str(num)
    for i in range(len(str(num))):
        result_ += int(str_num[i])
    result_ += num
    return result_

def check_self_num(num, no_gen = True):
    check_range = 9*len(str(num))
    check_list = []
    for i in range(num-check_range,num):
        b = self_num(i)
        if b == num:
            no_gen = False
            break
    if no_gen == True:
        print(num)


under_100 = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]

for a in under_100:
    print(a)
for t in range(100,10001):
    check_self_num(t)
