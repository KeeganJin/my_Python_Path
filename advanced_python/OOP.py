from time import sleep
from math import sqrt

class Person():

# __init__ is a special method used for initialization while creating
# object
    def __init__(self,name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self): return self._name
    @property
    def age(self): return self._age

    @age.setter
    def age(self, age): self._age = age

    def play(self):
        if self.age < 16:
            print('get from getter method')

    def check_age(age):
        if age >= 16:
            print("u alright")



def main():
    # p1 = Person('John',14)
    # p1.play()
    Person.check_age(88)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
