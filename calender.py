import calendar

n = int(input('enter the month'))
y = int(input('enter the year'))
data = calendar.month(y,n)
print(data)