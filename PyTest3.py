# -*- coding: utf-8 -*-



list = ['0','1','2','3']

print list

for index,item in enumerate(list):
    list[index] = float(item)

'''
enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
enumerate多用于在for循环中得到计数
'''
print list

print "---------我是分割线---------"



list1 = ['1','-1','1']
list2 = ['2','-2','2']
lists = [list1,list2]



print lists

for index,item in enumerate(lists):
    for index1,item1 in enumerate(lists[index]):
        lists[index][index1] = float(item1)


print lists



