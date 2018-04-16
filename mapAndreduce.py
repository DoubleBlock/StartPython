from functools import reduce
# map将传入的函数依次作用于序列的每个元素
def f(x):
    return x*x

r= map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


m=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(m)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
# 求和
def add(x, y):
    return x+ y
n= reduce(add, [1, 2, 3, 4])
print(n)



# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# capitalize()方法
list= ['adam', 'LISA', 'barT']
def normalize(m):
    for i in m:
        p= i.capitalize() # capitalize()方法
        print(p)
normalize(list)
l1= map(normalize, list)
# 循环遍历
# for i in list:
#     x= i[0].upper()+ i[1:].lower() # 此处等同于capitalize()方法
#     print(x)

