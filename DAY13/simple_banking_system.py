from art import *
import getpass

class GonePayAccounts:
    def __init__(self):
        tprint('MobilePay')
        self.total_bank_balance_possible = 9999999
        self.credentials_1 = ""
        self.credentials_password_dont_use = ""
        self.total_bank_balance = 0.0

    def sign_up_page(self):
        self.credentials_1 = input('Enter Username: ')
        self.credentials_password_dont_use = getpass.getpass('Enter password: ')
        self.total_bank_balance = float(input('Enter total bank balance: '))

    def transfer_money(self):
        user_to_send_money = input('Enter recipient name: ')
        sent_from = self.credentials_1
        amount_to_transfer = float(input('Enter amount to transfer: '))
        if amount_to_transfer > self.total_bank_balance:
            print("Insufficient funds.")
            return None
        self.total_bank_balance -= amount_to_transfer
        return {'sent from': sent_from, 'sent_to': user_to_send_money, 'amount': amount_to_transfer}

    def display_information_in_dashboard(self):
        tprint('Dashboard')
        print(f'Username: {self.credentials_1}\nTotal balance: {self.total_bank_balance}')
        if self.total_bank_balance >= self.total_bank_balance_possible:
            print("Are you Elon Musk?")
        elif self.total_bank_balance <= 500:
            print('Main Gareeb hoon')
        elif 500 < self.total_bank_balance <= 10000:
            print('Middle class ka dard')
        else:
            print('Rich kid')

        while True:
            choice = int(input('Enter 1 to transfer money\nEnter 2 to quit\n>>> '))
            if choice == 2:
                break
            elif choice == 1:
                return_output = self.transfer_money()
                if return_output:
                    print("Transfer successful.")
                    print(return_output)
            else:
                print("Invalid choice. Try again.")

    def authenticate_information(self):
        print('Sign in:')
        input_username = input('Enter username: ')
        input_password = getpass.getpass('Enter password: ')
        
        if input_password == self.credentials_password_dont_use and input_username == self.credentials_1:
            print('Successfully logged in')
            self.display_information_in_dashboard()
        else:
            print('Invalid credentials!')

    def deposit_amount(self, deposited_amount):
        self.total_bank_balance += deposited_amount
        print('After deposit')
        self.display_information_in_dashboard()

    def withdraw_amount(self, withdraw_amount):
        if withdraw_amount > self.total_bank_balance:
            print("Insufficient funds.")
        else:
            self.total_bank_balance -= withdraw_amount
            print('After withdrawal')
            self.display_information_in_dashboard()

# Main execution logic
def main():
    N_users = int(input('Enter number of users: '))
    all_accounts = [GonePayAccounts() for _ in range(N_users)]

    for account in all_accounts:
        choice = int(input('Enter 1 to Sign Up\nEnter 2 to Sign In\n>>> '))
        if choice == 1:
            account.sign_up_page()
        elif choice == 2:
            account.authenticate_information()
        else:
            print("Invalid choice. Please restart the process.")

    # Assuming one user wants to authenticate and perform transactions
    cache_user_name = input('Enter your username to authenticate: ')
    correct_object = None

    for account in all_accounts:
        if cache_user_name == account.credentials_1:
            correct_object = account
            break

    if correct_object:
        correct_object.authenticate_information()
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
