n = int(input('enter your fibinauci'))
first, second = 0,1
for i in range(n):
    first, second = second, first+second
    if second == n:
        print('the given number is a fibinauci number')
        break