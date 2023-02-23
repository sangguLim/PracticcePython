class SomeClass:
    def __init__(self,something):
        self.something = something

    def some_function(self):
        print(self.something)


if __name__ == '__main__':
    a=SomeClass('abc')
    a.some_function()        