#basic way of reversing a list without using reverse keyword
'''
l=[98,56,34,12,23]
n = len(l)
reverse_l = []
for i in range(n):
    ind = n-1-i
    reverse_l.append(l[ind])
print(reverse_l)


#enhanced way
l=[98,56,34,12,23]

#range,-1 will do the reverse
for i in range(len(l)-1,-1,-1):
    print(l[i], end=',')
'''
#reversing without reverse keyword
l=[98,56,34,12,23]
print(l[::-1])
