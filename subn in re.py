import re
print(re.subn('ov', '~*' , 'movie tickets booking in online'))
t = re.subn('ov', '~*' , 'movie tickets booking in online', flags = re.IGNORECASE)
print(t)
print(len(t))
print(t[0])