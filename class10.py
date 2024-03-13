"""Banking System 
Problem Statement: Design a banking system with Classes for customers , accounts & tansactions
Implement features Like: - 
1.Deposit
2.Withdrawal
3.Tranfer
4.Account Management
"""

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def transfer(self, amount, target_account):
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
        else:
            print("Insufficient balance!")

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute(self):
        if self.sender.balance >= self.amount:
            self.sender.balance -= self.amount
            self.receiver.balance += self.amount
        else:
            print("Insufficient balance!")

# Account Management
customer1 = Customer("John Doe", "123 Main St", "123-456-7890")
customer2 = Customer("Jane Smith", "456 Elm St", "987-654-3210")

account1 = Account("123456789", customer1)
account2 = Account("987654321", customer2)

# Deposit
account1.deposit(1000)
print(account1.balance)  # Output: 1000

# Withdrawal
account1.withdraw(500)
print(account1.balance)  # Output: 500

# Transfer using Transaction
transaction = Transaction(account1, account2, 200)
transaction.execute()
print(account1.balance)  # Output: 300
print(account2.balance)  # Output: 200

# Account Management
print(account1.customer.name)  # Output: John Doe
print(account2.customer.name)  # Output: Jane Smith

print("___________________________________________________________________________________________________")

"""Create an Online Shopping  Systen with classes ,representing products , customers ,orders & Shooping carts
Implement features like:
Adding /removing items from carts
processing orders
managing nventory
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                break

    def process_order(self):
        total_price = 0
        for item in self.items:
            product = item[0]
            quantity = item[1]
            if product.quantity >= quantity:
                product.quantity -= quantity
                total_price += product.price * quantity
            else:
                print(f"Insufficient quantity for {product.name}")
        print(f"Total price: {total_price}")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                break

    def process_order(self, customer):
        order = Order(customer)
        for item in self.items:
            order.add_item(item[0], item[1])
        order.process_order()
        self.items = []

# Product Management
product1 = Product("Apple", 1.0, 10)
product2 = Product("Banana", 0.5, 20)
product3 = Product("Orange", 0.8, 15)

# Customer Management
customer1 = Customer("John Doe", "123 Main St", "123-456-7890")
customer2 = Customer("Jane Smith", "456 Elm St", "987-654-3210")

# Shopping Cart Management
cart1 = ShoppingCart()
cart1.add_item(product1, 2)
cart1.add_item(product2, 3)
cart1.add_item(product3, 1)
cart1.process_order(customer1)  # Output: Total price: 4.3

cart2 = ShoppingCart()
cart2.add_item(product2, 5)
cart2.add_item(product3, 2)
cart2.process_order(customer2)  # Output: Insufficient quantity for Banana
                                 #         Total price: 1.6

# Inventory Management
print(product1.quantity)  # Output: 8
print(product2.quantity)  # Output: 12
print(product3.quantity)  # Output: 12