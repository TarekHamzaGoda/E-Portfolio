class BankAccount():
    """ A class to hold account information"""

    def __init__(self, account_num, account_name, account_balance):
        self.account_num = account_num  # Public
        self._account_name = account_name  # Protected
        self._account_balance = account_balance  # Private


# Creating Objects
Customer_1 = BankAccount("AE41221", "John", 90223)

accn = Customer_1.account_num
accname = Customer_1._account_name
accb = Customer_1.__account_balance


print(accn)
print(accname)
print(accb) # Error

