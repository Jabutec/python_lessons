# Object Oriented Programming

class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def meow(self):
        print(f"{self.name} says meow")
    
my_cat = Cat("Rex", 5)

print(f"My cat's name is {my_cat.name} and she's {my_cat.age} years old ")
print(my_cat.meow())
        
        

