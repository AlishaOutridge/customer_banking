""" Create a Account class with methods"""

class Account:
    def __init__(self, balance=0.0, interest_rate=0.0):
        self.balance = balance
        self.interest_rate = interest_rate

    def set_balance(self, new_balance):
        self.balance = new_balance

    def set_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate

    def calculate_interest(self, months):
        return (self.balance * (self.interest_rate / 100) * months) / 12
