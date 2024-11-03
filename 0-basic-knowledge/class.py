class T:
    # __init__ 是构造函数，而且必须显式定义
    def __init__(self, name, age): # self 是必不可缺的参数，相当于 this 指针
        self.name = name
        self.age = age

    def print(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

slh = T('slh', 17) # 实例化
slh.print()

class Car:
    def __init__(self, name, year, mile, tank):
        self.name = name
        self.year = year
        self.mile = mile
        self.tank = tank

    def add_tank(self, liter): # 加油
        self.tank += liter
    
class ElectricCar(Car):
    def __init__(self, name, year, mile):
        super().__init__(name, year, mile) # super() 使得子类可以调用父类的方法
        self.battery = 100

    def add_tank(self, liter):
        print("There's no need to add gas") # 会覆盖父类的方法

