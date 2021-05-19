
class Wallet:
    
    
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return f"this is a wallet {self.num}"
        #"this is a test {0}".format(self.num)
    
x = Wallet(1)
print(x)
print(type(x))

# Create a instance variable on the fly
x.amount = 10
print(x.amount)
x.savings = 100
print(x.savings)
x2 = Wallet(2)

# The id of the objects are different
print(id(x),id(x2))
x2 = x
print(id(x), id(x2))

x3 = Wallet(3)
print(x3)
# This will create an error because it is not shared !!!!!!
print(x2.savings)  # Object does not exist

#every class inherits from the object class
class Wallet(object):
    pass
# What does the class inherit from
x = Wallet()
print(x, type(x))
print(type(3))
print(type(3.0))
print(isinstance(3, int))

class Banking:
    balance = 500  # class variable shared
    
    def __init__(self,custName):  # <---- The constructor
        self.custName = custName
    
cust1 = Banking('John')
cust2 = Banking('Paul')
print(cust1.balance)
print(cust2.balance)

class Banking:
    balance = 0  # class variable shared
    bankDeposits = []
    bankWithdrawals = []
    
    def __init__(self,custName):
        self.custName = custName
        
    def __str__(self):
        return f"The current balance is {self.balance}"
    
    def deposit(self,amt):
        self.amt = amt
        self.balance += self.amt
        self.bankDeposits.append(amt) # Shared amoung the class
        
    def withdrawl(self, amt):
        self.amt = amt
        self.balance -= self.amt 
        self.bankWithdrawals.append(amt)
        
        
    
cust1 = Banking('John') #instantiate a Banking object , save to cust1
cust2 = Banking('Paul') #instantiate a Banking object , save to cust2
cust1.deposit(100) #call method deposit to deposit 100
#print(cust1.balance)
print(cust1) #print calls __str__ to print representation of object
cust1.withdrawl(50)
print(cust1)
cust1.deposit(400)
cust2.deposit(200)
print(cust2.balance)
print(cust1.bankDeposits)  # <== Class variable
print(cust1.balance)

# To track individual deposits
class Banking:
    custBalance = 0  # class variable shared
    bankDeposits = []
    
    def __eq__(self, obj_to_compare):
        if self.custBalance == obj_to_compare:
            return True 
        else:
            return False
    
    def __init__(self,custName,amt = 0):
        self.custName = custName
        self.deposit(amt)
    
    def __str__(self):
        if self.custBalance > 0 :
            return f"the balance is {self.custBalance}"
        else:
            return "your balance is zero or negative"
    
    def deposit(self,amt):
        self.custBalance += amt
        
cust1 = Banking('John', 200)
cust2 = Banking('Paul')
print(cust1)
print(cust2)
print(cust1.custBalance)
cust1.deposit(500)
print('{0} has {1} on deposit'.format(cust1.custName,cust1.custBalance))
print('{0} has {1} on deposit'.format(cust2.custName,cust2.custBalance))

# Add money to Paul's account
cust2.deposit(10000)
print('{0} has {1} on deposit'.format(cust2.custName,cust2.custBalance))

class Banking:
    custBalance = 0  # class variable shared
    bankDeposits = []
    
    def __init__(self,custName,amt = 0):
        self.custName = custName
        self.deposit(amt)
    
    def deposit(self,amt):
        self.custBalance += amt
        self.bankDeposits.append(amt)
        print('{0} now has {1} on deposit, {2} was just deposited'.format(self.custName,
                                                                          self.custBalance,
                                                                          amt))
    def withdrawl(self, amt):
        if self.custBalance < amt:
           print("cannot with withdraw, no sufficient funds")
        total_bank_deposits = int(sum(self.bankDeposits)* 0.5)
        
        if amt > total_bank_deposits:
            print("bank has a liquity problem")
        
        #notice how both if statements will run because 
        # if statements are not mutually exclusive 
        # to make mutually exclusive, use elif 
        """
        if condition1:
        elif condition2 : 
        
        in english: if not condition 1 try condition 2 
        
        
        if condition1:
        if condition2:
        
        in english: try condition 1, try condition 2
        """
        
        
                                                                    
        
cust1 = Banking('John', 200)
cust2 = Banking('Paul')
cust1.deposit(1000)
print('{0} was deposited. Now {1} is in the bank'.format(Banking.bankDeposits,sum(Banking.bankDeposits) ))
cust2.deposit(500)
cust2.deposit(150)
cust1.withdrawl(2000)
print('{0} was deposited. Now {1} is in the bank'.format(Banking.bankDeposits,sum(Banking.bankDeposits) ))

class Banking:
    accountType = 'Banking'
    custBalance = 0  # class variable shared
    bankDeposits = []
    
    def __init__(self,custName,amt = 0):
        self.custName = custName
        self._special = True if amt > 250000 else False
        self.deposit(amt)
    
    def deposit(self,amt):
        self.custBalance += amt
        self.bankDeposits.append(amt)
        print('{0} now has {1} on deposit, {2} was just deposited'.format(self.custName,
                                                                          self.custBalance,
                                                                         amt))
        if self._special:
            print('EXCEEDS FDIC INSURANCE LEVELS')

#a class inherits from it's superclass 
#the default superclass is object

class InvestmentAcct(Banking):
    accountType = 'Investments'
    
    def __init__(self,custName,amt = 0, margin=False):
        super().__init__(custName,amt)
        if self._special:     # <====== NOT ALLOWED
            print('QUALIFIED INVESTOR')        
        self.canMargin = 'Yes' if margin else 'No'
        self.openAccount()
        # Add a protected variable
            
    def openAccount(self):
        # self.custBalance was inherited
        print ('ACCOUNT OPENED' if self.custBalance >= 10000 else 'MINIMUM TO OPEN ACCOUNT IS 10000')


cust1 = Banking('Mary',200)
print(cust1.accountType)
cust2 = InvestmentAcct('Rosalee')
print(cust2.accountType)
print(cust2.canMargin)
cust3 = InvestmentAcct('George',10000, True)
print(cust3.accountType)
print(cust3.canMargin)

# canMargin does not exist for cust1
# print(cust1.canMargin)  # Attribute does not exist error

cust5 = Banking('Holly',300000)
cust6 = InvestmentAcct('Rick',500000)
print(Banking.accountType)
# print(Banking._special)   # <==================== ENCAPSULATED - information hiding
# print(InvestmentAcct._special)

from abc import ABC, abstractmethod 
class Polygons(ABC):
    
    @abstractmethod
    def numberOfSides(self):
        pass
    
    #when we inherit we need to write this method
    #no matter what
    @abstractmethod
    def numberOfDimensions(self):
        pass
   
    def numberOfSides2(self):
        pass
    
class Square(Polygons):
    def area(self,l,w):
        print('The area is {0}'.format(l*w))
    
    def numberOfSides(self):  # <=== Implements the abstract class !!!
        self.sides = 4
    def numberOfDimensions():
        pass
    
        
shape1 = Square()
print(shape1.area(5,6))



#dynamic typing
print(len('this is a string'))
print(len([1 for i in range(6)]))

#superclass sequence can be types
# string inherits from sequence 
# list inherits from sequence 


# len()
# Used on a string
print(len('Python'))

# Used on a list 
print(len([12,34,45]))

# Used on a dictionary
dictFruits = {'oranges': 5, 'apples':3 , 'pears': 5}
print(len(dictFruits))

def multiply(first, second):
    
    #if the variables are ints 
    if isinstance(first, int) and isinstance(second, int):
        return first * second
    #if the variables are str
    if isinstance(first, str) and isinstance(second, str):
        return f"{first} * {second}"
    
    #if the variables are float 
    if isinstance(first, float) and isinstance(second, float):
        return first * second
    
    #checks if first and second are of the same type
    if not all(type(first) == var for var in [first, second]):
        return "types are not the same, this is an error!" 

print(multiply(3,3))
print(multiply(3.0,3.0))
print(multiply("3","3"))
print(multiply("three","three"))
print(multiply("three", 3))

### Class method and static methods

# Python program to demonstrate  
# use of class method and static method. 
from datetime import date 
   
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
       
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
       
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
   
person1 = Person('Gloria', 21) 
person2 = Person.fromBirthYear('Sara', 1996) 
   
print (person1.age) 
print (person2.age) 
   
# print the result 
print (Person.isAdult(22)) 


