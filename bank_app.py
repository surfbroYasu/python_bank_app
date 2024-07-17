# bank app 
# types of functions
# deposit withdrawal ledgering
class Bank:
    def __init__(self) -> None:
        self.check_account(input("What is your first name?:  "), input("What is your last name?: "))

    def open_r_file(self, fname, lname):
            return open (f'{fname}_{lname}.txt', 'r')
            
    def open_w_file(self, fname, lname):
        return open (f'{fname}_{lname}.txt', 'w')
                
                
                
    def check_account(self, fname, lname):
        while True:
                
            fname = fname.lower()
            lname = lname.lower()
            action = input(f"{fname} {lname} (next / back): ")
            if action == "next":
                break
            elif action == "back":
                self.__init__()
                break
            else:
                print("invalid!")
                
        try:
            r_file = self.open_r_file(fname, lname)
            total = r_file.readline()
            print(total)
            total = float(total)
            self.despatch(fname, lname, total)
                        
                        
        except FileNotFoundError:
            while True:
                confirm = input("Would you like to open your account?y/n: ")
                if confirm == "y":
                    self.open_account(fname, lname)
                    break
                elif confirm == "n":
                    print("You have selected NO")
                    return None
                else:
                    print("Invalid")

                    
    def despatch(self, fname, lname, total):
        while True:
            next_action = input("Select your next action: (Withdrawal / Deposit / Balance / Exit)  ")
            if next_action.lower() == "withdrawal":
                self.withdrawal(fname, lname, total)
                break
            elif next_action.lower() == "deposit":
                self.deposit(fname, lname, total)
                break
            elif next_action.lower() == "balance":
                self.check_balance(fname, lname, total)
                break
            elif next_action.lower() == "exit":
                print("Thank you for choosing MyBank")
                return None
            else:
                print("Invalid")
                        


    def open_account(self, fname, lname):
        while True:
            initial_amount = float(input("How much initial amount do you want to put down? "))
            if 10 < initial_amount < 100_000:
                
                while True:
                    final_confirm = input(f"$ {initial_amount} ?  y/n: ")
                    
                    if final_confirm.lower() == "y":
                        # next action
                        print(f"opening your account with $ {initial_amount: ,}")
                        
                        with open (f"{fname}_{lname}.txt", "w")as f:
                            f.write(str(initial_amount))
                            
                        self.despatch(fname, lname, initial_amount, f)
                        return None
                        # File write and amount typed in
                        
                    elif final_confirm.lower() == "n":
                        self.open_account(fname, lname)
                        break
                    else:
                        print("Plese type in | y |or| n |")
                        pass
                        # Back to final_confirmation
                
            elif initial_amount == 0:
                print("Amount must be at lease $10 and cannot exceed $10000")

        
        # file open and overwrite balance 
        

        pass

    def deposit(self, fname, lname, total):
        deposit_amount = input("How much do you want to put in?: $ ")
        total += float(deposit_amount)
        print(total)
        w_file = self.open_w_file(fname, lname)
        w_file.write(str(total))
            
        self.despatch(fname, lname, total)
    
    def withdrawal(self, fname, lname, total):
        w_amount = input("How much do you want to withdraw?: $ ")
        total -= float(w_amount)
        w_file = self.open_w_file(fname, lname)
        w_file.write(str(total))
        self.despatch(fname, lname, total)
    
    def check_balance(self, fname, lname, total):
        print(f'{fname.capitalize()} {lname.capitalize()} \nBALANCE: ${total}')
        self.despatch(fname, lname, total)
        
a = Bank()