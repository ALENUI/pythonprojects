import json
import os

FILENAME = "./bank-acount-manager/bank-data.txt"


class BankAccount:
    def check_balance(self):
        if not os.path.exists(FILENAME):
            print("No account data found.")
            return

        accountNumber = input("Input account number (use # if unknown): ")

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)

                if accountNumber == "#":
                    name = input("Input account name: ")
                    if not name.isalpha():
                        print("Account name must contain only letters.")
                        return
                    found = False
                    for acc_num, acc_data in data.items():
                        if acc_data["name"].lower() == name.lower():
                            print(f"{acc_data['name']} (Account Number: {acc_num}), your current balance is: {acc_data['balance']}")
                            found = True
                            break
                    if not found:
                        print("Account not found.")
                elif accountNumber in data:
                    acc = data[accountNumber]
                    print(f"{acc['name']} (Account Number: {accountNumber}), your current balance is: {acc['balance']}")
                else:
                    print("Account not found.") 
        except json.JSONDecodeError:
            print("Error reading account data. Please check the file format.")
            return

    def create_account(self):
        accountNumber = input("Input account number (6 digits): ")
        if not accountNumber.isdigit() or len(accountNumber) != 6:
            print("Account number must be a 6-digit number.")
            return

        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading account data. Please check the file format.")
                return
        else:
            data = {}

        if accountNumber in data:
            print("Account already exists.")
            return

        name = input("Input account name: ")
        if not name.isalpha():
            print("Name must contain only letters.")
            return

        try:
            initial_balance = float(input("Input initial deposit: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        data[accountNumber] = {"name": name, "balance": initial_balance}
        with open(FILENAME, "w") as file:
            json.dump(data, file)

        print(f"Account ({accountNumber}) successfully created for {name} with balance {initial_balance}.")

    def withdraw(self):
        accountNumber = input("Input account number: ")
        if not accountNumber.isdigit() or len(accountNumber) != 6:
            print("Account number must be a 6-digit number.")
            return
        if not os.path.exists(FILENAME):
            print("No account data found.")
            return

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
            if accountNumber in data:
                name = data[accountNumber]["name"]
                balance = data[accountNumber]["balance"]
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount > balance:
                        print("Insufficient funds.")
                        return
                    balance -= amount
                    data[accountNumber]["balance"] = balance
                    with open(FILENAME, "w") as file:
                        json.dump(data, file)
                    print(f"{name} (Account Number: {accountNumber}), your new balance is: {balance}")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    return
            else:
                print("Account not found.")
        except json.JSONDecodeError:
            print("Error reading account data. Please check the file format.")
            return

    def deposit(self):
        accountNumber = input("Input account number: ")
        if not accountNumber.isdigit() or len(accountNumber) != 6:
            print("Account number must be a 6-digit number.")
            return
        if not os.path.exists(FILENAME):
            print("No account data found.")
            return

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
            if accountNumber in data:
                name = data[accountNumber]["name"]
                balance = data[accountNumber]["balance"]
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    balance += amount
                    data[accountNumber]["balance"] = balance
                    with open(FILENAME, "w") as file:
                        json.dump(data, file)
                    print(f"{name} (Account Number: {accountNumber}), your new balance is: {balance}")
                except ValueError:
                    print("Invalid Input. Please enter a numeric value.")
            else:
                print("Account not found.")
        except json.JSONDecodeError:
            print("Error reading account data. Please check the file format.")
            return

    def all_accounts(self):
        if not os.path.exists(FILENAME):
            print("No account data found.")
            return

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
            if not data:
                print("No accounts found.")
                return
            print("\nAll Accounts:")
            for acc_num, acc_data in data.items():
                print(f"Account Number: {acc_num}, Name: {acc_data['name']}, Balance: {acc_data['balance']}")
        except json.JSONDecodeError:
            print("Error reading account data. Please check the file format.")
            return

def menu():
    print("\n=== Bank Menu ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Create Account")
    print("5. View All Accounts")
    print("6. Exit")


print("Welcome to the Bank Account Manager!")
account = BankAccount()  # single reusable instance

while True:
    menu()
    choice = input("Please choose an option (1-5): ")

    if choice == '1':
        account.deposit()
    elif choice == '2':
        account.withdraw()
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        account.create_account()
    elif choice == '5':
        account.all_accounts()
    elif choice == '6':
        print("Thank you for using the Bank Account Manager!")
        break
    else:
        print("Invalid choice. Please try again.")
