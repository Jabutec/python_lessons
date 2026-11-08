from Animal import Animal

class Snake(Animal):
    def __init__(self, name, age, vpotent):
        super().__init__(name, age)
        self.vpotent = vpotent