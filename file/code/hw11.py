x = []
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

x.append(a)
x.append(b)
x.append(c)

x.sort()

if x[2] < x[0]+x[1]:
    print('O')
else:
    print('X')
    
