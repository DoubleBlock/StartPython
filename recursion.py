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
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n- 1)+ fibonacci(n- 2))
fibonacci(10)


# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))