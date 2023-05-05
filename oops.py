class MyClass:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, {self.name}!")
    def Age(self):
        print(f"Your age is  {self.age}")
li=[1,2,3,4,5,6]
for i in li:
    obj=MyClass(i,i)
    obj.greet()
    obj.Age()


