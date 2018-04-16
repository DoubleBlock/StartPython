import copy

s= [1,2,3,['a','b','c','d',['o','p','q']]]

def getItems(l):
    for i in l:
        if isinstance(i, list):
            getItems(i)
        else:
            print(i)
getItems(s)
print([id(x) for x in s])
y= s
print([id(a) for a in y])
m= copy.copy(s)
print([id(y) for y in m])
n= copy.deepcopy(s)
print([id(z) for z in n])
s.append(4)
s[3].append('f')
s[3][4].append('r')
print(s)
print(y)
print(m)
print(n)
