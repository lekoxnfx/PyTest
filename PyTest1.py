# -*- coding: utf-8 -*-

import pandas as pd

print "strat..."

print "开始"

df2 = pd.read_csv('/Users/lekoxnfx/Documents/PyCsvTest1.csv', encoding='gb2312', )

print df2


print "--------------1--------------"

pf = df2.xs(u"栏目2", 1)

print pf

print type(pf[0])

print "--------------2--------------"


df2 = df2[u'栏目2'].replace(u"高", 3).replace(u"低", 1)

print df2

# for cell in pf:
#     if(cell==u"高"):
#         cell = 3
#         print "好高啊"
#     elif(cell==u"低"):
#         cell = 1
#         print "好低啊"
#
#     else:
#         cell = 2
#
# print pf

print "-------------3--------------"







# for row in df.values:
#     for cell in row:
#
#         if(str(cell).decode("GB2312") == "高"):
#             cell = 3
#         elif(str(cell).decode("GB2312") == "低"):
#             cell = 1
#         else:
#             cell = 2
#
# print df




print "end"

