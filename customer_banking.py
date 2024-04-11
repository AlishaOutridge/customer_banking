from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Handling the Savings Account
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate (as a percentage): "))
    savings_maturity = int(input("Enter the number of months for interest calculation: "))
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Savings Account Updated Balance: ${updated_savings_balance:,.2f}")
    print(f"Savings Account Interest Earned: ${savings_interest_earned:,.2f}")

    # Handling the CD Account
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate (as a percentage): "))
    cd_maturity = int(input("Enter the number of months for interest calculation: "))
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"CD Account Updated Balance: ${updated_cd_balance:,.2f}")
    print(f"CD Account Interest Earned: ${cd_interest_earned:,.2f}")

if __name__ == "__main__":
    main()
