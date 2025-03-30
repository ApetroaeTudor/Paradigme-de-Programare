from Organism import *

if __name__=="__main__":
    om=Organism("om")
    om.AddMuschi(50,"Locomotor.IncordareBratStang","BicepsStang")
    om.AddMuschi(80,"Locomotor.IncordareBratDrept","TricepsDrept")
    om.AddMuschi(120,"Echilibru.","Abdominal")
    om.AddTrunchiNervos(100,"Coordonare.ColoanaVertebrala","TrunchiColoana")

    om.printLungimeTrunchiuriNervoase()
    om.printMasaMusculara()
    om.filterMuschiDupaScop("Locomotor")