class Bar(object):
    def __init__(self) -> None:
        self.value = ''
    def __get__(self,instance,owner):
        print("returned from descriptor object")
        return self.value
    def __set__(self,instance,value):
        print("set in descriptor object")
        self.value = value
    def __delete__(self,instance):
        print("delete in descriptor object")
        del self.value

class Foo(object):
    bar = Bar()

f = Foo()
f.bar = 10
print(f.bar)
del f.bar