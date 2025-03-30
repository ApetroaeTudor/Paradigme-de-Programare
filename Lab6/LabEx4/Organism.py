from Classes import *

class Organism:
    nume:str
    muschi:list[MuschiGeneric]
    trunchiuri_nervoase:list[TrunchiNervos]

    def __init__(self,nume:str):
        self.nume=nume
        self.muschi=[]
        self.trunchiuri_nervoase=[]

    def AddMuschi(self,masa:float,scop:str,nume:str):
        celule=[FibraMusculara("Fibra1",masa-masa/3),FibraMusculara("Fibra2",masa/3)]
        tempMuschi=MuschiGeneric(nume,scop,celule)
        self.muschi.append(tempMuschi)

    def AddTrunchiNervos(self,lungime:float,specializare:str,nume:str):
        celule=[FibraNervoasa("Fibra1",lungime-lungime/4),FibraNervoasa("Fibra2",lungime/4)]
        tempTrunchi=TrunchiNervos(nume,specializare,celule)
        self.trunchiuri_nervoase.append(tempTrunchi)

    def printMasaMusculara(self):
        masa=0
        for muscle in self.muschi:
            masa+=muscle.get_masa_musculara()
        print(f"Masa Musculara a organismului cu numele {self.nume} este: {masa}")

    def printLungimeTrunchiuriNervoase(self):
        lungime=0
        for trunchi in self.trunchiuri_nervoase:
            lungime+=trunchi.get_lungime()
        print(f"Lungimea trunchiurilor nervoase a organismului cu numele {self.nume} este: {lungime}")

    def filterMuschiDupaScop(self,scop:str):
        foundAtLeastOne=False
        for muscle in self.muschi:
            if muscle.get_scop().split(".")[0]==scop:
                print(f"Muschi cu scopul {muscle.get_scop()}")
                foundAtLeastOne=True
        if foundAtLeastOne==False:
            print("Nu s-au gasit muschi cu scopul cautat")