import StateMachines as s

if __name__ == "__main__":
    vending_machine = s.VendingMachineSTM()
    vending_machine.take_money_stm.current_state.client_arrived()
    vending_machine.select_product_stm.current_state.choose()
    
    vending_machine.proceed_to_checkout()
