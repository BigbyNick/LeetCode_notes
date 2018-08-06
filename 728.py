left = 100
right = 102
llist = []

for i in range(left,right+1):
    flag = True
    cell = i
#    if (cell % 10 ==0):
#        flag = False
#        continue

    if ('0' in str(cell) ):
        continue
    
    while ( (cell % 10) != 0 ):
        print(cell)
        a = (cell % 10)
        print(a)
        if ((i % a) != 0 ):
            flag = False
            break
        cell = (cell // 10)

    if (flag == True):
        llist.append(i)

print(llist)
