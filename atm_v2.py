class Transaction:
    def __init__(self,transaction_id,transaction_type,amount,status,resulting_balance):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.status = status
        self.resulting_balance = resulting_balance

class Account:
    def __init__(self,acc_holder,balance,acc_no):
        self.acc_holder = acc_holder
        self._balance = balance
        self.acc_no = acc_no
        self.transaction_history = []
        self.transaction_id=1

    def get_balance(self):
            return self._balance

    def deposit(self,amount):
        if amount <= 0:
            return False
        self._balance += amount
        t = Transaction(self.transaction_id, "Deposit",amount,"Deposited",self._balance)
        self.transaction_history.append(t)
        self.transaction_id += 1
        return True

    def withdraw(self,amount):
        if amount <= 0:
            return False
        if amount > self._balance:
            t = Transaction(self.transaction_id, "Withdraw",amount,"Failed",self._balance)
            self.transaction_history.append(t)
            self.transaction_id += 1
            return False
        self._balance -= amount
        t = Transaction(self.transaction_id, "Withdraw",amount,"Successful",self._balance)
        self.transaction_history.append(t)
        self.transaction_id += 1
        return True

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self,account):
        self.accounts[account.acc_no] = account

    def menu(self,):
      while True:
        while True:
            try:
                acc_no = int(input("Enter account no: "))
            except ValueError:
                print("Enter a valid numeric account no.")
                continue
            if acc_no not in self.accounts:
                print("Account not found.")
                continue
            account = self.accounts[acc_no]
            break

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
                if account.deposit(amount):
                   print("Deposit successful.")
                else:
                   print("Deposit failed.")

            elif choice == "2":
                try:
                    amount = int(input("Enter amount to Withdraw: "))
                except ValueError:
                    print("Please enter a valid numeric amount!")
                    continue
                if account.withdraw(amount):
                    print("Withdraw successful.")
                else:
                    print("Withdraw failed.")

            elif choice == "3":
                print("\n===========BALANCE==========")
                print("Balance: ",account.get_balance())

            elif choice == "4":
                print("\n================================================")
                print("               TRANSACTION HISTORY        ")
                print("=================================================")
                if not account.transaction_history:
                    print("No transactions found.")
                else:
                    for t in account.transaction_history:
                        print(t.transaction_id, t.transaction_type, t.amount, t.status, t.resulting_balance)

                print("=================================================")

            elif choice == "5":
                print("\nExiting..")
                break

            else:
                print("\nInvalid choice!")

acc1 = Account("KRISHNA",100,1)
acc2 = Account("RADHA",50,2)

atm=ATM()
atm.add_account(acc1)
atm.add_account(acc2)
atm.menu()