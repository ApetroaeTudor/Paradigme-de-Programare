
class State:
    def __init__(self,state_machine,price = None):
        self.state_machine = state_machine
        self.price = price
    def __str__(self):
        pass




class SelectProductSTM:
    def __init__(self):
        self.select_product_state=SelectProduct(self)
        self.coca_cola_state = CocaCola(self,6)
        self.pepsi_state = Pepsi(self,5)
        self.sprite_state = Sprite(self,4)
        self.current_state = self.select_product_state


    def choose_another_product(self):
        self.current_state = self.select_product_state



class SelectProduct(State):
    def choose(self):
        choice = int(input('Please input your drink choice:\n 1.CocaCola\n2.Pepsi\n3.Sprite'))
        if choice == 1:
            self.state_machine.current_state = self.state_machine.coca_cola_state
        elif choice == 2:
            self.state_machine.current_state = self.state_machine.pepsi_state
        elif choice == 3:
            self.state_machine.current_state = self.state_machine.sprite_state
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



class TakeMoneySTM:
    def __init__(self):
        self.wait_state = WaitingForClient(self)
        self.insert_money_state = InsertMoney(self)
        self.current_state = self.wait_state

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
    def insert_50bani(self):
        self.state_machine.add_money(0.5)
    def insert_1leu(self):
        self.state_machine.add_money(1)
    def insert_5lei(self):
        self.state_machine.add_money(5)
    def insert_10lei(self):
        self.state_machine.add_money(10)






class VendingMachineSTM:
    def __init__(self):
        self.take_money_stm = TakeMoneySTM()
        self.select_product_stm = SelectProductSTM()
    
    def proceed_to_checkout(self):
        if(self.select_product_stm.current_state==self.select_product_stm.select_product_state):
            print("Please select a product")
        else:
            if self.select_product_stm.current_state.price:
                if self.select_product_stm.current_state.price > self.take_money_stm.money:
                    print("Insufficient Funds:")
                    print("Your funds: {}".format(self.take_money_stm.money))
                    print("Price of the product: ${}".format(self.select_product_stm.current_state.price))
                    self.select_product_stm.current_state = self.select_product_stm.select_product_state
            else:
                difference = self.take_money_stm.money - self.select_product_stm.current_state.price
                print("You got {}".format(self.select_product_stm.current_state))
                choice = int(input("Get change (choose 1) or buy something else(choose 2)"))
                if(choice == 1):
                    print("You got ${} lei in change".format(self.take_money_stm.money))
                    self.take_money_stm.update_amount_of_money(0)
                elif(choice == 2):
                    print("Please select another product: ")
                    self.take_money_stm.update_amount_of_money(difference)
                self.select_product_stm.current_state = self.select_product_stm.select_product_state