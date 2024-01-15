class user :
    def __init__(self, name,email,phone):
        self.name =name
        self.email = email
        self.phone =phone
        self.accounts =[]
        
    def add_account(self, account):
        self.accounts.append(account)
        
class Bank_Account:
    def __init__(self,account_number, balance):
        self.account_number =account_number
        self.balance = balance
        self.card = None
        
    def add_card(self,card):
        self.card = card
        
        
    def make_transaction(self,transaction):
        if self.card is None:
            print('Error:No card is associated with this account')
            return
        if transaction.amount > self:
            self.balance -= transaction.amount 
            transaction.proccessed =True
        print('Transaction succesful.')
        
class card :
    def __init__(self,card_number, expiry_date):
        self.card_number =card_number 
        self.expiry_date =expiry_date
        
        
class Transaction:
    def __init__(self, amount, merchant):
        self.amount = amount
        self.merchant = merchant
        self.processed = False
        
    def __str__(self):
        return f'Transaction of {self.amount} at {self.merchant}'
    

# Example usage 
user = user('Alice','alice@example.come','i23-456-7890')
account = Bank_Account('1234567890',1000.00)
user.add_account(account)

card = card('1111222233334444', '12/25')
account.add_card(card)

transaction = Transaction(50.00, 'Amazon')
account.make_transaction(transaction)
print(transaction.processed)# True

transaction2 = Transaction(2000.00, 'Fancy')