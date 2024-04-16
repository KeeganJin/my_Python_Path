
# OOP 



## class
* In Python, __init__ is an instance method that initializes a newly created object.
* using _started name to show that it's protected, but it still can be directly assessed.
* as for the object as argument, it's regarding to the old/style 
* 
## built-in method 

* __str__

## @property built-in decorator
* @property is used to define a read-only attribute.
*
```python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
```
### static method and class method
* class methods: called on the class itself, not on a specific object instance
* @staticmethod
* @classmethod

## relation between classes

* is-a
* has-a
* use-a

## inherit and poly-morphism
* method with the same name different child class 

## Abstract class
* can not be initialized
* can only be inherited, that's the purpose.
* if a class has abstract method, then it cannot be initialized.


# UI


# Reflection

control the method in a form of string.
```python
getattr()
```