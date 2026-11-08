class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def makeSound(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        
class Snake(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length
        
    def makeSound(self):
        print(f"I am a snake and I am {self.length} cm long.")
        
class Lion(Animal):
    def __init__(self, name, age,):
        super().__init__(name, age)
    
    def run(self,runSpeed):
        print(f"I am a {self.name} the Lion and my top speed is {runSpeed} km/h")

class Zoo:
    def __init__(self, name, animals):
        self.name = name
        self.animals = animals
        
A1 = Animal("Bob", 7)
S1 = Snake("Candy", 12, 1000)
L1 = Lion("Junior", 10)


animalList = [A1,S1]

Z1 = Zoo("Midvaal Zoo", animalList)

for animal in Z1.animals:
    animal.makeSound()
    
L1.run(20)