from Animal import Animal

class Snake(Animal):
    def __init__(self, name, age, vpotent):
        super().__init__(name, age)
        self.vpotent = vpotent
        
    def makeSound(self):
            print(f"Hi I am a Snake and I have {self.vpotent} strong")