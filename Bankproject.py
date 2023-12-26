#ACCOUNT LOGIN
users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password. Please try again.")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)




# creating an object of class
s = Bank_Account()


# Calling functions 
s.login()
s.deposit()
s.withdraw()
s.display()
