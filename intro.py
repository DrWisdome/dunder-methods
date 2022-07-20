from typing import Any


class Person:
    def __init__(self,name):
        self.name = name
        
    def __repr__(self) -> str:
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be an integer")
        self.name = self.name * x

    def __call__(self, *args: Any, **kwds: Any) -> Any:
            print(*args)
            print(kwds)

    def __len__(self):
        return len(self.name)

p = Person("Tim")
p(4, meno="Fero")
print(len(p))