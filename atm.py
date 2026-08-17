class ATM:
    def __init__(self,balance):
        self.balance = balance
        self.transaction_history = []
        self.transaction_id=1

    def deposit(self,amount):
        if amount <= 0:
            print("Please enter a valid numeric amount!")
            return None

        self.balance += amount
        print("Amount deposited: ",amount)
        self.transaction_history.append(f"Transaction ID: {self.transaction_id} | Deposited: {amount} | Balance: {self.balance}")
        self.receipt("Deposit", amount,"Success")
        self.transaction_id += 1
        return amount

    def withdraw(self,amount):
        if amount <= 0:
            print("Please enter a valid numeric amount!")
            return None

        if amount > self.balance:
            print("Insufficient balance.. ")
            self.transaction_history.append(f"Transaction ID: {self.transaction_id} | Withdrawal failed: {amount} | Balance: {self.balance}")
            self.receipt("Withdrawal", amount,"Failed", "Insufficient balance")
            self.transaction_id += 1
            return None

        self.balance -= amount
        print("Amount withdrawn: ",amount)
        self.transaction_history.append(f"Transaction ID: {self.transaction_id} | Withdrawal successful: {amount} | Balance: {self.balance}")
        self.receipt("Withdrawal", amount,"Success")
        self.transaction_id += 1
        return amount

    def check_balance(self):
        print("BALANCE : ", self.balance)

    def print_transactions(self):
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
           print("No transactions yet")

    def receipt(self,transaction_type,amount,status,reason=""):
        print("\n")
        print("========================")
        print("      ATM RECEIPT")
        print("========================")
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Transaction    : {transaction_type.upper()}")
        print(f"Status         : {status.upper()}")
        print(f"Amount         : {amount}")
        print(f"Balance        : {self.balance}")
        print("========================")
        if reason:
           print(f"Reason         : {reason}")
        print("\n")

    def menu(self):
        while True:
           print("\n============TRANSACTION MENU===========")
           print("1. Deposit")
           print("2. Withdraw")
           print("3. Check Balance")
           print("4. Show Transaction History")
           print("5. Exit")

           choice = input("Enter your choice: ")

           if choice == "1":
               try:
                   amount = int(input("Enter amount to deposit: "))
               except ValueError:
                   print("Please enter a valid numeric amount!")
                   continue
               self.deposit(amount)


           elif choice == "2":
               try:
                   amount = int(input("Enter amount to withdraw: "))
               except ValueError:
                   print("Please enter a valid numeric amount!")
                   continue
               self.withdraw(amount)


           elif choice == "3":
               print("\n===========BALANCE===========")
               self.check_balance()


           elif choice == "4":
               print("\n================================================")
               print("               TRANSACTION HISTORY        ")
               print("=================================================")
               self.print_transactions()
               print("=================================================")

           elif choice == "5":
               print("\nExiting..")
               break

           else:
               print("\nInvalid choice!")


atm = ATM(100)
atm.menu()


