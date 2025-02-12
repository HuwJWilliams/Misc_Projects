def add(*args):
    answer = 0
    for arg in args:
        answer += arg
    return answer


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=5, multiply=2)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car = Car(make="nissan")
print(my_car.model)
