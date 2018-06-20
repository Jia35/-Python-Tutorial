a = [8,1,9,2,3,9,4,8,7,5,6,5,3,2,4,7]
# 1+6=7
s=0
'''
for i in range(len(a)):
    ff = 0
    for j in range(len(a)):
        if a[i]==a[j]:
            ff+=1
    if ff==1:
        print(a[i])
        s+=a[i]
'''
print('只出現了1次:',end='')
for n in a:
    if a.count(n)==1:
        print(n,end=',')
        s+=n
print()
print('兩數總和:',s)

# print(sum([n for n in a if a.count(n)==1]))
