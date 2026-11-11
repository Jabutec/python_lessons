from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age, claws):
        super().__init__(name, age)
        self.claws = claws
        
    def makeSound(self):
            print(f"Hi I am a Lion and I have {self.claws} claws")