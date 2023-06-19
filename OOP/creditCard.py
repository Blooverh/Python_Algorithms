"""Example of a class for a credit card"""
class CreditCard:
    """Think of this function as a constructor method in java"""
    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance"""
        
        self.customer=customer
        self.bank= bank
        self.account=account
        self.limit= limit
        self.balance=0

    def getCustomer(self):
        return self.customer
        
    def get_bank(self):
        return self.bank
        
    def get_account(self):
        return self.account
        
    def get_limit(self):
        return self.limit
        
    def get_balance(self):
        return self.balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit"""
        if price+self.balance > self.limit:
            return False
        else:
            self.balance+= price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self.balance-=amount
        
    