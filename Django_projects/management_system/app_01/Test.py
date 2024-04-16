class TestClass(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name


obj = TestClass("tt")


if __name__ == '__main__':
    print(obj)