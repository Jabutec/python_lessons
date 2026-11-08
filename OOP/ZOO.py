from Lion import Lion
from Zebra import Zebra
from Snake import Snake
import json


class Zoo:
    def __init__(self, name, entryCost):
        self.name = name
        self.entryCost = entryCost
        self.animals = []
        
    def loadAnimals(self):
        pass
    
    def addAnimal(self, animalInfo):
        
        {
            "animalType": "Lion",
            "animalName": "Bob",
            "animalAge": 12,
            "claws" : 10
        }
         
        if animalInfo.animalType == "Lion":
            L = Lion(animalInfo.name, animalInfo.age, animalInfo.claws)
            self.animals.append(L)
            with open("ZooAnimals.JSON", "w") as ZA:
                json.dump(animalInfo,ZA)
                
        if animalInfo.animalType == "Snake":
            S = Snake(animalInfo.name, animalInfo.age, animalInfo.vpotent)
            self.animals.append(S)
            with open("ZooAnimals.JSON", "w") as ZA:
                json.dump(animalInfo,ZA)
                        
        if animalInfo.animalType == "Lion":
                Z = Zebra(animalInfo.name, animalInfo.age, animalInfo.stripes)
                self.animals.append(Z)
                with open("ZooAnimals.JSON", "w") as ZA:
                    json.dump(animalInfo,ZA)
        
        



