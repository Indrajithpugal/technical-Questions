
#basic approach
'''
l = [98,76,45,23,12,21,43,56,78]
count = len(l)
total = 0
for i in l:
    total += i
    print(total)
print(total/count)
'''

#using sum approach dynamic way

n = int(input('enter the number of value need to find the average'))
number_list = []
for i in range(n):
    values = int(input('enter the values'))
    number_list.append(values)

ans = sum(number_list)/len(number_list)
print(ans)