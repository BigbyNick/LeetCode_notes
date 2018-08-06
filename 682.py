ops =["5","-2","4","C","D","9","+","+"]

a = []
b = []
"""
for i in range(len(ops)):
    if ops[i] == "C":
        a[i] = a[i-1]
        b[i] = 0
        b[i-1] = 0
    elif ops[i] == "D":
        for j in range(0, i+1)[::-1]:
            if b[j] == 1 :
                a[i] = a[j] * 2
                b[i] = 1
    elif ops[i] == "+":
        count = 0
        for j in range(0, i+1)[::-1]:
            if count < 2 :
                if b[j] == 1 :
                    a[i] = a[i] + a[j] 
                    count = count + 1
            else:
                b[i] = 1
                break
            
        
    else:
        a[i] = int(ops[i])
        b[i] = 1

for i in range(len(ops)):
    if b[i] == 1:
        tol = tol + a[i]

print(tol)
"""
point_list = []  
for op in ops:  
    if op == '+':  
        point_list.append(sum(point_list[-2:]))  
    elif op == 'C':  
        if point_list:  
            del point_list[-1]  
    elif op == 'D':  
        if point_list:  
            point_list.append(point_list[-1] * 2)  
    else:  
        point_list.append(int(op))  
  
print( sum(point_list) )
