# 找出最大最小值
list= [1, 3, 5, 7, 9]
max= list[0]
for i in list:
    if i> max:
        max= i
print(max)
min= list[0]
for j in list:
    if j<min:
        min= j
print(min)