from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age, claws):
        super().__init__(name, age)
        self.claws = claws