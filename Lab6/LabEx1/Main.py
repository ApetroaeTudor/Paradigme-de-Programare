from abc import ABC, abstractmethod

class Animal(ABC):
    _weight=0
    _color:str
    
    def __init__(self,weight,color):
        self._weight=weight
        self._color=color
        
    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return "; Weight: "+ str(self._weight)+"kg; Color: "+self._color+" "


    
class Felina(Animal, ABC):
    
    _sound:str
    
    def __init__(self,weight,color,sound):
        super().__init__(weight,color)
        self._sound=sound
        
    @abstractmethod
    def make_sound(self):
        print(self._sound)

    def __repr__(self):
        return "Sunet: " + self._sound+super().__repr__()


class Pisica(Felina):
    
    def __init__(self,weight,color):
        super().__init__(weight,color,"meow")
    
    def make_sound(self):
        super().make_sound()

    def __repr__(self):
        return "Pisica: " + super().__repr__()

class Tigru(Felina):

    def __init__(self,weight,color):
        super().__init__(weight,color,"roar")

    def make_sound(self):
        super().make_sound()

    def __repr__(self):
        return "Tigru: " + super().__repr__()

class Zoo:
    Animals:list[Animal]

    def __init__(self,animalList:list[Animal]):
        self.Animals=animalList

    def PrintAllAnimals(self):
        for animal in self.Animals:
            print(animal)


if __name__=="__main__":
    myZoo=Zoo([Pisica(5,"gri"),Pisica(3,"alba"),Tigru(30,"portocaliu")])
    myZoo.PrintAllAnimals()