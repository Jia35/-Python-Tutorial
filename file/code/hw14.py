h = 100
s = 0
for i in range(9):
    s += 2*h
    h /= 2

s += h
print("總共經過",s,"米")
print("最後一次高度為",h,"米")
