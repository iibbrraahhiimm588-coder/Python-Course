# =========================================
# ATM SYSTEM – FUNCTION BASED FLOW
# =========================================

# 1) Sabse pehle system data hota hai
# ek saved PIN
# ek starting balance


# 2) authenticate() function
# Ye function user se PIN leta hai
# aur saved PIN se compare karta hai
# Agar match kare to True return karta hai
# warna False return karta hai


# 3) show_menu() function
# Ye user ko ATM ke options dikhata hai
# (balance, withdraw, deposit, exit)
# User ki choice return karta hai


# 4) check_balance(balance) function
# Ye sirf current balance return karta hai


# 5) withdraw(balance) function
# Ye user se withdraw amount leta hai
# check karta hai ke amount <= balance
# agar haan to balance se minus karta hai
# updated balance return karta hai
# agar nahi to same balance wapas bhej deta hai


# 6) deposit(balance) function
# Ye user se deposit amount leta hai
# balance me add karta hai
# updated balance return karta hai


# 7) Main program flow:

# - Sabse pehle authenticate() call hota hai
# - Agar False aaye, program end
# - Agar True aaye, ATM menu start


# 8) While loop start hota hai
# - show_menu() se choice li jati hai
# - if / elif se decide hota hai:
#     -> 1 ho to check_balance()
#     -> 2 ho to withdraw()
#     -> 3 ho to deposit()
#     -> 4 ho to break (exit)


# 9) Har operation ke baad
# updated balance ko variable me store kiya jata hai


# 10) Jab user exit karta hai
# loop break hota hai
# aur program finish ho jata hai

# ATM Program with Functions

saved_pin = 7555  # Initial saved PIN

# Function to authenticate user
def authentication(saved_pin):
    pin = int(input('Enter your PIN: '))
    if saved_pin == pin:
        return True
    else:
        return False

# Function to show menu and get user choice
def show_menu():
    print("\n--- ATM Menu ---")
    print("1: Balance")
    print("2: Withdraw")
    print("3: Deposit")
    print("4: Exit")
    user_choice = input("Enter your choice: ")
    return user_choice

# Function to show current balance
def Current_balance(balance):
    return balance

# Function to withdraw amount
def withdraw(balance):
    withdraw_amount = int(input("Enter your withdraw amount: "))
    if withdraw_amount > balance:
        print("Not enough balance!")
        return balance
    else:
        balance -= withdraw_amount
        print(f"Withdraw successful! Updated balance: {balance}")
        return balance

# Function to deposit amount
def deposit(balance):
    deposit_amount = int(input("Enter your deposit amount: "))
    balance += deposit_amount
    print(f"Deposit successful! Updated balance: {balance}")
    return balance

# Main program flow
def main_program(saved_pin):
    balance = 10000  # Initial balance
    if authentication(saved_pin):
        print("Access granted.")
        while True:
            choice = show_menu()
            if choice == "1":
                print("Current balance:", Current_balance(balance))
            elif choice == "2":
                balance = withdraw(balance)  # Update balance after withdraw
            elif choice == "3":
                balance = deposit(balance)   # Update balance after deposit
            elif choice == "4":
                print("Thanks for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Incorrect PIN. Access denied.")

# Run the ATM program
main_program(saved_pin)

