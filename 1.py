def twoSum(list, sum):
    slen = len(list)
    for i in range (slen):
        for j in range (i+1,slen):
            if list[j] == (sum - list[i]):
                return i,j
                break

if __name__ == '__main__':
    list =[2,7,10,19]
    sum = 9
    print(twoSum(list,sum))
                
