from Account import Account

def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, interest_rate)
    interest_earned = cd_account.calculate_interest(months)
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)
    return updated_balance, interest_earned
