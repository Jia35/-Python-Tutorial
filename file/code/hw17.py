isbn = input("ISBN碼:")
num=[]

for i in isbn:
    if i=='X':
        num.append(10)
    else:
        num.append(int(i))

for i in range(len(num)-1):
    num[i+1] = num[i] + num[i+1]
print("第一次累加和:" , num)

for i in range(len(num)-1):
    num[i+1] = num[i] + num[i+1]
print("第二次累加和:" , num)

if num[-1]%11 == 0:
    print("YES")
else:
    print("NO")
