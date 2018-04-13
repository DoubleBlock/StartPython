import copy

s= ['a','b','c','d']
m= copy.copy(s)
n= copy.deepcopy(s)
m.append('e')
n.append('f')
print(m)
print(n)
print(s)
