from Animal import Animal

class Zebra(Animal):
    def __init__(self, name, age, stripes):
        super().__init__(name, age)
        self.stripes = stripes
        
    def makeSound(self):
        print(f"Hi I am a Zebra and I have {self.stripes} number of stripes")