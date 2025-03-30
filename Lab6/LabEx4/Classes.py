from abc import ABC,abstractmethod


class Celula(ABC):
    @abstractmethod
    def get_nume(self)->str:
        raise NotImplementedError("Metoda trebuie implementata!")

class FibraMusculara(Celula):
    nume:str
    masa_musculara:float


    def __init__(self,nume,masa_musculara):
        self.nume=nume
        self.masa_musculara=masa_musculara

    def get_nume(self) ->str:
        return self.nume

    def get_masa_musculara(self)->float:
        return self.masa_musculara

class FibraNervoasa(Celula):
    nume:str
    lungime:float

    def __init__(self,nume,lungime):
        self.nume=nume
        self.lungime=lungime

    def get_nume(self):
        return self.nume

    def get_lungime(self):
        return self.lungime



class MuschiGeneric:
    nume:str
    scop:str
    fibre:list[FibraMusculara]
    masa_musculara:float=0.0

    def __init__(self,nume:str,scop:str,fibre:list[FibraMusculara]):
        self.nume=nume
        self.scop=scop
        self.fibre=fibre
        for fibra in fibre:
            self.masa_musculara+=fibra.get_masa_musculara()

    def get_masa_musculara(self)->float:
        return self.masa_musculara
    def get_nume(self)->str:
        return self.nume
    def get_scop(self)->str:
        return self.scop

class TrunchiNervos:
    nume:str
    specializare:str
    nervi:list[FibraNervoasa]
    lungime:float=0.0

    def __init__(self,nume:str,specializare:str,nervi:list[FibraNervoasa]):
        self.nume=nume
        self.specializare=specializare
        self.nervi=nervi
        for nerv in nervi:
            self.lungime+=nerv.get_lungime()

    def get_nume(self)->str:
        return self.nume
    def get_lungime(self)->float:
        return self.lungime
    def get_specializare(self)->str:
        return self.specializare