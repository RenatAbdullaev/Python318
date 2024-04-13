class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age


p = Person("irina", 26)

print(p.__dict__)

p.name = "igor"
p.age = 31

print(p.name)
print(p.age)

del p.name

print(p.__dict__)
