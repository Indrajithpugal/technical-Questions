'''
we can manage resources using the context managers when we create a context manager using classes
we have to define that classes with "__enter__" and "__exit__"
__enter__: returns the source that we need to manage
__exit__: will cleanup the files
'''
#Basic example file:
# Python program creating a
# context manager

class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')
