#he phrase "monkey patch" in Python exclusively references run-time dynamic alterations to a module.
class normal:
    def fun(self):
        return 'this is normal message'

def mon_fun():
    return 'this is a monkey pathc'

normal.fun=mon_fun
obj = normal
print(obj.fun())