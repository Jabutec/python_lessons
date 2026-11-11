class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def makeSound(self):
        print(f"Hi I am {self.name} and I am {self.age} years old")
        