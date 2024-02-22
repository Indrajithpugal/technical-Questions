#basic yield
'''
def month():
    yield 1
    yield 2

m=month()
print(m.__next__())
print(m.__next__())


#yield with for loop
def loo():
    month = ['jan', 'feb', 'mar', 'apr']
    for i in range(len(month)):
        yield month[i]
l=loo()
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
'''

#yield with parameters
l=['mon','tue','wed']
def para_yield(a):
    yield l[a]
    yield l[a+1]
    yield l[a+2]

p = para_yield(0)
print(p.__next__())
print(p.__next__())
print(p.__next__())