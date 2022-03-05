def add(*args):
    n = 0
    for numb in args:
        n += numb
    return n

print(add(1,2,43,5,6,7,56,423))

def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
    

print(calculate(1, add=4,multiply=3))

class Car():
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")