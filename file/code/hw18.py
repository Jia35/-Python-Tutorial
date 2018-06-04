f = open('problem.txt', 'r')
s = f.read()
f.close()

for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        print(i)
