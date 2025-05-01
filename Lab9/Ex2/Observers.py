
class Observable:
    def __init__(self):
        self.observers = []
    def attach(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
    def detach(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
    def updateAll(self):
        for obs in self.observers:
            obs.update()

class Observer:
    def update(self):
        pass

class DisplayObserver(Observer):
    def __init__(self,take_money_stm):
        self.take_money_stm = take_money_stm

    def update(self):
        print("\n--From DisplayObserver -- Current Balance is: {}\n".format(self.take_money_stm.money))

class ChoiceObserver(Observer):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine
    def update(self):
        print("\n-- From ChoiceObserver -- Choice made, proceeding to checkout\n")
        self.vending_machine.proceed_to_checkout()
