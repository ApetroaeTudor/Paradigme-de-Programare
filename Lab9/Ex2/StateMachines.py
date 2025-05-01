import Observers as obs    

class State:
    def __init__(self,state_machine,price = None):
        self.state_machine = state_machine
        self.price = price
    def __str__(self):
        pass




class SelectProductSTM(obs.Observable):
    def __init__(self):
        super().__init__()
        self.select_product_state=SelectProduct(self)
        self.coca_cola_state = CocaCola(self,6)
        self.pepsi_state = Pepsi(self,5)
        self.sprite_state = Sprite(self,4)
        self.current_state = self.select_product_state


    def choose_another_product(self):
        self.current_state = self.select_product_state
        self.current_state.choose()



class SelectProduct(State):
    def choose(self):
        choice = int(input('Please input your drink choice:\n1.CocaCola\n2.Pepsi\n3.Sprite\n'))
        if choice == 1:
            self.state_machine.current_state = self.state_machine.coca_cola_state
            self.state_machine.updateAll()
        elif choice == 2:
            self.state_machine.current_state = self.state_machine.pepsi_state
            self.state_machine.updateAll()
        elif choice == 3:
            self.state_machine.current_state = self.state_machine.sprite_state
            self.state_machine.updateAll()
        else:
            print("Invalid choice, choose again")
            self.choose()

class CocaCola(State):
    def __str__(self):
        return "CocaCola"

class Pepsi(State):
    def __str__(self):
        return "Pepsi"

class Sprite(State):
    def __str__(self):
        return "Sprite"



class TakeMoneySTM(obs.Observable):
    def __init__(self):
        super().__init__()
        self.wait_state = WaitingForClient(self)
        self.insert_money_state = InsertMoney(self)
        self.current_state = self.wait_state
        self.attach(obs.DisplayObserver(self))

        self.money = 0

    def add_money(self,value):
        self.money = self.money + value
    
    def update_amount_of_money(self,value):
        self.money = value

class WaitingForClient(State):
    def client_arrived(self):
        print("Cliend arrived, please insert money")
        self.state_machine.current_state = self.state_machine.insert_money_state

class InsertMoney(State):
    def insert_10bani(self):
        self.state_machine.add_money(0.1)
        self.state_machine.updateAll()
    def insert_50bani(self):
        self.state_machine.add_money(0.5)
        self.state_machine.updateAll()
    def insert_1leu(self):
        self.state_machine.add_money(1)
        self.state_machine.updateAll()
    def insert_5lei(self):
        self.state_machine.add_money(5)
        self.state_machine.updateAll()
    def insert_10lei(self):
        self.state_machine.add_money(10)
        self.state_machine.updateAll()






class VendingMachineSTM:
    def __init__(self):
        self.take_money_stm = TakeMoneySTM()
        self.select_product_stm = SelectProductSTM()

        self.select_product_stm.attach(obs.ChoiceObserver(self))
    
    def proceed_to_checkout(self):
        if(self.select_product_stm.current_state==self.select_product_stm.select_product_state):
            print("Please select a product")
        else:
            if self.select_product_stm.current_state.price:
                if int(self.select_product_stm.current_state.price) > int(self.take_money_stm.money):
                    print("Insufficient Funds:")
                    print("Your funds: {}".format(self.take_money_stm.money))
                    print("Price of the product: {}".format(self.select_product_stm.current_state.price))
                    choice = int(input("Insert money(1) or leave(2)\n"))
                    if choice == 1:
                        moneyChoice = int(input("1.10 bani\n2.50 de bani\n3.1leu\n4.5lei\n5.10lei\n"))
                        if moneyChoice==1:
                            self.take_money_stm.current_state.insert_10bani()
                        elif moneyChoice==2:
                            self.take_money_stm.current_state.insert_50bani()
                        elif moneyChoice==3:
                            self.take_money_stm.current_state.insert_1leu()
                        elif moneyChoice==4:
                            self.take_money_stm.current_state.insert_5lei()
                        elif moneyChoice==5:
                            self.take_money_stm.current_state.insert_10lei()
                        else:
                            print("invalid choice")
                        self.proceed_to_checkout()
                        # self.select_product_stm.updateAll()
                    else:
                        self.take_money_stm.current_state = self.take_money_stm.wait_state
                        self.select_product_stm.current_state = self.select_product_stm.choose_another_product

                    # self.select_product_stm.current_state = self.select_product_stm.select_product_state
                else:
                    difference = self.take_money_stm.money - self.select_product_stm.current_state.price
                    print("You got {}".format(self.select_product_stm.current_state))
                    choice = int(input("Get change (choose 1) or buy something else(choose 2)\n"))
                    if(choice == 1):
                        print("You got {} lei in change".format(difference))
                        self.take_money_stm.update_amount_of_money(0)
                        self.take_money_stm.current_state = self.take_money_stm.wait_state
                        self.select_product_stm.current_state = self.select_product_stm.select_product_state
                    elif(choice == 2):
                        self.take_money_stm.update_amount_of_money(difference)
                        self.select_product_stm.choose_another_product()