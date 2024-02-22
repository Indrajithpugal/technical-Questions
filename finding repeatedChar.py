#objective-- finding the repeated single character in a string
#basic way-- this script taken 1 hr for pugal by achieved without referring any ans in google
a = 'this is hello world from united states'

repeat_controller = []
for counting in range(len(a)):
    matches = 0
    for data,count in zip(a,range(len(a))):
        if a[counting]==data:
            matches +=1
    re = f'{a[counting]} occurs {matches} in the given string'

    if re in repeat_controller:
        pass
    else:
        repeat_controller.append(re)
        print(re)
