import calendar

dd,mm,yy = map(int,input().split())
print(calendar.day_name[calendar.weekday(yy,dd,mm)].upper())

