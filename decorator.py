def uppercaser(func):
    def inner():
        data = func()
        data=data.upper()
        return data
    return inner

def greeting(func):
    def wrapper():
        data = func()
        data = data +' to ladies and gentleman'
        return data
    return  wrapper

def splitter(func):
    def wrapping():
        data = func()
        data = data.split()
        return data
    return wrapping

def capitalizer(x):
    def caps():
        datas=x()
        data = len(datas)
        print(datas)
        return data
    return caps



@capitalizer
@splitter
@greeting
@uppercaser
def message():
    return 'hello world'

print(message())