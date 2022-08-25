class Bank:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def withdrawal(self, transactionAmount):
        if transactionAmount > self.balance:
            print(f"The withdrawal amount of ${transactionAmount} exceeds your account balance of ${self.balance}. Transaction cancelled.")
        else: 
            self.balance = self.balance - transactionAmount
            self.transaction_log(f"Withdrew: ${transactionAmount}")
    
    def deposit(self, transactionAmount):
        if transactionAmount:
            self.balance = self.balance + transactionAmount
            self.transaction_log(f"Depostied: ${transactionAmount}") 

    def transaction_log(self, transaction_string):
        with open('transactions.txt', 'a') as file:
            file.write(f"{transaction_string}\t\t Account Balance: $ {self.balance}\n")
            
account = Bank(1_000.50)

while True:
    try:
        transactionType = input("What type of transaction would you like to complete? deposit or withdrawal. ")
        transactionType = transactionType.lower()
    except KeyboardInterrupt:
        print("\nLeaving the ATM")
        break
    
    if transactionType in ["withdrawal", "deposit"]:
        
        transactionAmount = float(input(f"How much would you like to {transactionType}? $ "))
        if transactionType == 'deposit':
            newBalance = account.deposit(transactionAmount)
        else:
            newBalance = account.withdrawal(transactionAmount)

        initialBalance = newBalance
        print("Your account balance is $", account.balance)

    else:
        print("You have selected an invalid transaction type. Try again.")
    