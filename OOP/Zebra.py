from Animal import Animal

class Zebra(Animal):
    def __init__(self, name, age, stripes):
        super().__init__(name, age)
        self.stripes = stripes