from datetime import *
ldates = []

d1=date(2016,8,12)
d2=date(2017,8,12)
d3=date(2018,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for d in ldates:
    print(d)