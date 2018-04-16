s= [1,2,3,['a','b','c','d',['o','p','q']]]
# 普通的for循环只能取出1,2,3和嵌套列表['a', 'b', 'c', 'd', ['o', 'p', 'q']]
for i in s:
    print(i)
# 1
# 2
# 3
# ['a', 'b', 'c', 'd', ['o', 'p', 'q']]

# 使用isinstance()
for m in s:
    if isinstance(m, list):
        for n in m:
            if isinstance(n,list):
                for k in n:
                    print(k)
            else:
                print(n)
    else:
        print(m)
# 使用递归
def getItems(l):
    for i in l:
        if isinstance(i, list):
            getItems(i)
        else:
            print(i)
getItems(s)