import pprint
# s= 0
# while s < 5:
#     print('sss')
#     s = s + 1

# s = 2
# if(s == 1):
#     print('hello')
# elif(s == 2):
#     print('world')
# else:
#     print('hello world')




# for i in range(1, 11):
#     print(i)


# i= 1
# while i< 11:
#     print(i)
#     i+=1
#
#
# def printName(name):
#     print('hello '+ name)
# printName('haha')



# def sp():
#     global egg
#     egg= 66
#     return 33
#
# egg= 77
# sp()
# print(egg)
# print(sp())


#Collatz(考拉次猜想)
# def collatz(number):
#     print(number)
#     if number%2== 0:
#         collatz(number//2)
#     elif number%2==1 and number> 1:
#         collatz(3*number+ 1)
#
#
# if __name__== '__main__':
#     try:
#         number= int(input('please enter a number'))
#         collatz(number)
#     except:
#         print('请输入一个整数')


# 切片可以获取部分列表
# s=['a', 'b', 'c']
# s.append('d')
# s.insert(1,'e')
# s.sort()
# print(s)
# print(s[:2])
# print(s.index('d'))
#
# s= [1, 2, 3]
# size, color, dis= s
# print(color)


# y=(1, 2, 3)
# x= [4, 5, 6]
# print(list(y))
# print(tuple(x))



# spam = ['apples', 'bananas', 'tofu', 'cats']
# def outStr(s):
#     s[len(spam)-1]= 'and '+s[len(spam)-1]
#     n=','.join(s).split('/')
#     for i in n:
#         print(i)
#
# outStr(spam)



# s= ','.join(spam)
# n=s.split(',')
# print(str(s))


# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]
# def printgrid(a):
#     for i in a:
#         if isinstance(i,list):
#             printgrid(i)
#         else:
#             print(i)
#
# printgrid(grid)


# 统计字符串出现的次数
# message= ['a', 'b', 'c', 'A', 'a']
# count= {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character]= count[character]+ 1
#
# print(count)



# allGuests= {'Alice': {'apples': 5,'pretzels': 12},
#             'Bob': {'ham sandwiches': 3,'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}
#             }
#
# def totalBrought(guests, item):
#     numBrought= 0
#     for k, v in guests.items():
#         numBrought= numBrought+ v.get(item, 0)
#     return numBrought
# pprint.pprint((totalBrought(allGuests, 'pretzels')))



# 好玩的物品清单
# stuff= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv= {'gold': 42,'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(invs,addedItems):
    newItems = {}
    for k in addedItems:
        newItems.setdefault(k, 0)
        newItems[k]= newItems[k]+ 1
    newInv= dict(invs, **newItems)
    print(newInv)
invens= addToInventory(inv, dragonLoot)
print(invens)
#
# newInv= {'gold': 42, 'rope': 1, 'gold coin': 3, 'dagger': 1, 'ruby': 1}
# def displayInventory(inventory):
#     num= 0
#     for k, v in inventory.items():
#         num= num+ v
#         print(str(k) + ' ' + str(v))
#     print('total items are ' + str(num))
#
# displayInventory(invens)

#
# inv= {'gold': 42,'rope': 1}
# dragonLoot = {'dagger': 20, 'ruby': 40}
# def addToInventory(invs,addedItems):
#     newInv= dict(**invs, **addedItems)
#     return newInv
# print(addToInventory(inv, dragonLoot))


