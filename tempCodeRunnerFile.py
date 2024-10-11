import datetime

str1 = "2020/07/22"
str2 = "07/22/2020 PM 1:37:4:33217"
str3 = "July 22,2020 13:37:4:33217+09:00"

dt1 = datetime.datetime.strptime(str1, "%Y/%m/%d")
dt2 = datetime.datetime.strptime(str2, "%m/%d/%Y %p %I:%M:%S:%f")
dt3 = datetime.datetime.strptime(str3, "%B %d,%Y %H:%M:%S:%f%z")

print(dt1)
#>> 2020-07-22 13:37:04.332170
print(dt2)
#>> 2020-07-22 13:37:04.332170
print(dt3)
#>> 2020-07-22 13:37:04.332170+09:00
