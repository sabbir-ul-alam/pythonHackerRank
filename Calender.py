import  calendar

line=list(map(int,input().split()))
mon=line[0]
day=line[1]
yr=line[2]


a=calendar.weekday(yr, mon, day)
print(calendar.day_name[a].upper())