a = input("輸入:")
offset = int(input("偏移量:"))

out = []
for i in a:
    num = ord(i)+offset
    if num>122:
        num = num-122+96
    out.append(chr(num))

print(out)
