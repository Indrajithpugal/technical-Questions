
#1st approach
'''
n = int(input('enter the boundary of fibinauci series'))
first,second = 0,1

for i in range(0,n):
    if i>0:
        print(first)
        first,second=second, first+second

#2nd approach

n = int(input("please give a number for fibonacci series : "))
first,second=0,1
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
    print(result)
'''

