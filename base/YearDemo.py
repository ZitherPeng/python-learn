# coding=utf-8
def checkYear(year):
    if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
        print("%d是闰年" %year)
    else:
        print("%d是平年" %year)
checkYear(2000)   
    