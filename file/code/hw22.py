import time

box = [False] *10
print(box)
tstart = time.time()

for i in range(len(box)):
    for j in range(len(box)):
        if (j+1)%(i+1)==0:
            box[j] = not box[j]
    print('第{:2d}次：{}'.format(i+1, box))

tend = time.time() 

print("花費時間:",tend-tstart,"s")
