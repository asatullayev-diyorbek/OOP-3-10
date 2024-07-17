class Cat:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__dict__['_Cat__age']

    @age.setter
    def age(self, age):
        raise AttributeError("age ni o'zgartirolmaysiz")


c1 = Cat("Misha", 2)
# c1.age = 3
print(c1.age)