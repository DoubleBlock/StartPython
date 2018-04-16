# 列表生成式
# 生成1到10的平方
a= []
for x in range(1,11):
    a.append(x*x)
print(a)

b= [y**2 for y in range(1,11)]
print(b)


s= {'A': '1', 'B': '2', 'C': '3'}
for k, v in s.items():
    print(k, v)


L = ['Hello', 'World', 18, 'Apple', None]
M= []
for s in L:
    if isinstance(s, str):
        M.append(s.lower())
print(M)

N= [p.lower() for p in L if isinstance(p, str)]
print(N)