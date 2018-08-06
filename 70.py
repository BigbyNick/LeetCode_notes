n = 3
a = 0
b = 0
for i in range(1,n+1):
    if i == 1:
        a = 1
        print(1)
    if i == 2:
        a = b = 1
        print(2)
    if i >= 3:
        a , b = a + b, a 
print(a)
