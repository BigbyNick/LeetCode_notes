def change(x):
    flag = 0
    if (x >= 0):
        flag = 1
    else:
        flag = -1
        x = flag * x
    res = 0
    while (x > 0) :
        mid_res = x % 10
        res = res*10 + mid_res
        x = x // 10
        print (res)
    if (abs(res) > 0x7fffffff):
        return 0
    else:
        return res*flag

if __name__ == '__main__':
    x = -1230885858584848
    y = change(x)
    print (y)
