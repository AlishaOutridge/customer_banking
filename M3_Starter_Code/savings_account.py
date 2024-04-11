from Account import Account

def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)
    interest_earned = savings_account.calculate_interest(months)
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)
    return updated_balance, interest_earned

