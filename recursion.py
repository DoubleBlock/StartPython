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
#
# 斐波那契数列
def fib(n):
    # 数列的前两项是1
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return (fib(n- 1)+ fib(n- 2))
x= int(input("你要输出的项数？"))

if x<= 0:
    print("请重新输入")
else:
    print("斐波那契数列：")
    for i in range(1,x+1):
        # 注意参数否则会报错超过最大递归深度 RecursionError: maximum recursion depth exceeded in comparison
        print(fib(i))


