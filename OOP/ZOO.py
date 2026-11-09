from Lion import Lion
from Zebra import Zebra
from Snake import Snake
import json


class Zoo:
    def __init__(self, name, entryCost):
        self.name = name
        self.entryCost = entryCost
        self.animals = []
        
    def loadAnimals(self, flag):
        try:
            with open("ZooAnimals.JSON", "r") as ZA:
                listobj = json.load(ZA)
            
            if flag:
                return listobj
            else:
                for animal in listobj:
                    self.addAnimal(animal)
        except FileNotFoundError as FNE:
            print(f"Could not find file {FNE.filename}")
            
            return []
            
        if flag:
            return listobj  
    
    
    
    def addAnimal(self, animalInfo):
        
           
        if animalInfo.get('animalType') == "Lion":
            L = Lion(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('claws'))
            self.animals.append(L)
            
            newListDict = self.loadAnimals(True)
            newListDict.append(animalInfo)
            self.storeAnimals(newListDict)
            
        
                
        elif animalInfo.get('animalType') == "Snake":
            S = Snake(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('vpotent'))
            self.animals.append(S)
            
            newListDict = self.loadAnimals(True)
            newListDict.append(animalInfo)
            self.storeAnimals(newListDict)
                        
            
                        
        elif animalInfo.get('animalType') == "Zebra":
                Z = Zebra(animalInfo.get('name'), animalInfo.get('age'), animalInfo.get('stripes'))
                self.animals.append(Z)
                
                newListDict = self.loadAnimals(True)
                newListDict.append(animalInfo)
                self.storeAnimals(newListDict)
                            
                
                
                
                    
    def storeAnimals(self, animalInfo):
        try:
            with open("ZooAnimals.JSON", "w") as ZA:
                json.dump(animalInfo,ZA, indent=4)
        except FileNotFoundError as FNE:
            print(f"Could not find file {FNE.filename}")
            
            return []
            
            
        
        
        



