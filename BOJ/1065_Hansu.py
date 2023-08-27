def hansu_checker(num):
    str_num = str(num)
    a = int(str_num[0])
    b = int(str_num[1])
    c = int(str_num[2])
    if (b-a) == (c-b):
        hansu = True
    else:
        hansu = False
    return hansu




in_ = int(input())
if 100 > in_ > 0:
    print(in_)
elif in_ <= 1000:
    result_ = 99
    for i in range(100, in_+1):
        if hansu_checker(i) == True:
            result_ += 1
    print(result_)
else:
    print("ERROR: 1이상 1000이하의 수를 입력해주세요.")
