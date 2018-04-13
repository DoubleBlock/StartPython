import re

# # 利用括号分组
# phoneNumReg=re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo=phoneNumReg.search('abc445-333-3333')
# mo.group(1) #参数1输出前半部分445
# mo.group(2)# 参数2输出后半部分333-3333 0或者是无参数输出完整匹配的结果
#
# # 管道匹配多个分组
# heroRegex=re.compile(r'Batman|Tina Fey|AA') # 匹配一个或多个
# mo1=heroRegex.search('Tina Fey and Batman  ')
# print(mo1.group()) # 如果两个都出现则选择前一个Tina Fey


# bat=re.compile(r'Bat(man|mobile|copter|bat)')
# mo2=bat.search('Batmobile lost a wheel')
# print(mo2.group()) # 打印Batmobile 参数是1 打印mobile

# ?实现可选匹配
# batRegex= re.compile(r'Bat(wo)?man') #匹配Batwoman或者Batman 字符wo出现0次或者一次模式wo可选
# mo= batRegex.search('The Adventures of Batman')
# print(mo.group()) #输出Batman
# mo1= batRegex.search('The Adventures of Batwoman')
# print(mo1.group()) #输出Batwoman

# # 星号（*）匹配0次或多次
# batRegex= re.compile(r'Bat(wo)*man')
# mo= batRegex.search('The Adventures of Batman')
# mo.group() #匹配Batman
# mo1=batRegex.search('The Adventures of Batman')
# mo1.group() # 匹配Batwoman

# 加号（+）至少匹配一次
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# mo1.group() # 'Batwoman'
# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# mo2.group() # 'Batwowowowoman' 贪心匹配匹配最长的字符串
# mo3 = batRegex.search('The Adventures of Batman')
# mo3 == None # True

# 花括号匹配特定次数
# （ha）{3}   匹配'hahaha'
#  (ha){3,5}  匹配'hahaha' 'hahahaha' ''hahahahaha
#  (ha){3,}   3次和三次以上
#  (ha){,5}   0到5次

# 贪心和非贪心匹配
