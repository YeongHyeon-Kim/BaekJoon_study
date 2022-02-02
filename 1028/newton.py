li = [0]*65536
# li[65536 - (256-30)] = 1
# li[0] = 1

ind = li.index(max(li))
i = ind // 256
location = 30 - (ind - (256*i))
print(location * 256 + i)
