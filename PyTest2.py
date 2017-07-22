# -*- coding: utf-8 -*-

import pandas as pd

print "strat..."

df = pd.DataFrame({'one':['0','2','3'],'two':['2','3','4'],'three':['3','4','5']})

print df
print df.dtypes

# df['one'] = df['one'].astype("float64")
#
# print df['one']


df = df.astype('float64')

print df
print df.dtypes
