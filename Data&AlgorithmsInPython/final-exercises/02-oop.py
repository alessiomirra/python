from oop import CreditCard, PredatoryCreditCard
from vector import Vector

##############################################################

# 2.4
# Write a Python class called "Flower" with attribues in constructor
# for name(str), number of petals(int) and price(float). Add methods to set those each of 
# those values and retrieve each of those values

##############################################################

class Flower:
    """A class representing a flower"""

    def __init__(self, name = None, petals = None, price = None):
        """Create a new flower insance
        
        name       The flower's name (str)
        petals     The petals number (int)
        price      The flower's price   (float)
        """
        self._name = self._petals = self._price = None 

        self.set_name(name)
        self.set_petals_number(petals)
        self.set_price(price)
    
    def set_name(self, name):
        """Set the flower's name"""
        try:
            self._name = str(name)
        except:
            print(("Invalid input for name. It must be a string"))

    def set_petals_number(self, number):
        """Set the flower's petals number"""
        try:
            self._petals = int(number)
        except: 
            print("Invalid Input") 

    def set_price(self, price):
        """Set the flower's price"""
        if price is not None:
            try: 
                self._price = float(price)
            except: 
                print ('Invalid price, must be a number (no dollar sign)') 
    
    def get_name(self):
        """Retrieve name"""
        if self._name is None: return ('Attribute has not been set')
        else: return self._name
    
    def get_price(self):
        """Retrieve price"""
        if self._price is None: return ('Attribute has not been set')
        else: return self._price
    
    def get_petals(self):
        """Retrieve petals"""
        if self._petals is None: return ('Attribute has not been set')
        else: return self._petals


##############################################################

# 2.5, 2.6
# Revise the charge() and make payement() method of CreditCard class 
# to ensure that the caller sends a number as parameter 
# In make_payment() raise a Value error if a negative value is sent
# Reference to CreditCard class in oop.py file

##############################################################

class CreditCard2(CreditCard):
    """Class extending the CreditCard original"""
    def __init__(self,customer,bank,acnt,limit):
        super().__init__(customer,bank,acnt,limit)

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
            
        Return True if charge was processed; False if charge was denied.
        """
        try: 
            price = float(price)
        except TypeError:
            print("Invalid value for price")
        if price + self._balance > self._limit:     # if charge would exceed limit
            return False                            # cannot accept charge
        else: 
            self._balance += price 
            return True 

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        try: 
            if amount < 0:
                raise ValueError(("The amount value can't be negative"))
            amount = float(amount)
        except TypeError: 
            print("Invalid value for amount")
        self._balance -= amount 


##############################################################

# 2.7
# The CreditCard class initializes the balance of a new account to zero. Modify the class so that 
# a new account can be given a non-zero balance using an optional fifth parameter to the constructor. 
# The four-parameter constructor should continue to produce an account with zero balance 

# For this exercise I'll create a class inheriting from the original CreditCard

##############################################################

class CreditCardWithBalance(CreditCard):
    """Extending the original CreditCard Class in order to add a ner parameter"""
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        super().__init__(customer, bank, acnt, limit)
        self._balance = balance  


##############################################################

# 2.9, 2.10, 2.12, 2.13, 2.14

# 2.9: Implement the __sub__ method for the Vector class so that u-v returns a new vector instance repreenting the 
# difference between two vectors

# 2.10: Implement the __neg__ method for the Vector class so that -v returns a new vector whose coordinates are all 
# negated values of the respective coorfinates of v

# 2.12: Implement the __mul__ method for the Vector class so that the expression v * 3 returns a new vector with coordinates
# that are 3 times the respective coordinates of v

# 2.13: Implement the __rmul__ method to provide additional support for syntax 3 * v 

# 2.14: Implement a method that returns a scalar representing the dot product of the vectors 

##############################################################

class Vector2(Vector):
    """Extends the Vector class adding two more methods for substraction and negative coordinates"""
    def __init__(self,d):
        super().__init__(d)

    def __sub__(self, other):
        """Returns substraction of two vectors"""
        if len(self) != len(other):
            raise ValueError("Dimension must agree")
        result = Vector(len(self))  
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result 

    def __neg__(self):
        """Returns the vector with negative coordinates"""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result 

    def __mul__(self):
        """Returns the vector which coordinates are multiplied by 3"""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * 3
        return result 

    def __rmul__(self):
        """Return the vector resulting from a right-hand multiplication"""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = 3 * self[i]
        return result 

    def __dot__(self, other):
        """Returns the dot product of two vectors"""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = 0 
        for i in range(len(self)):
            result += self[i] * other[i]
        return result 

##############################################################

# 2.15

# The Vector class provides a constructor that takes an integer d, and produces a d-dimensional vector with all cordinates
# equal to 0. Another convenient form would be to send the constructor a parameter that is some iterable type representing a 
# sequence of numbers, and to create a vector with dimension equal to length of the sequence and coordinates equal to the sequence 
# values. Modify the constructor so that either of these forms is acceptable. 
# SO: if an integer is sent it produces a vector of that dimensions with all zeros, but if a sequence of numbers is provided, it 
# produces a vector with coordinates based on that sequence. 

##############################################################

class AlternativeVector:
    """Represent a Vector

    Instead of accept only an integer as value, it can accept sequences even
    """
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d 
        else: 
            try: 
                self._coords = list(d)
            except TypeError:
                raise TypeError("Invalid parameter. Please provide an integer or an iterable sequence of numbers")


##############################################################

# 2.17
# Draw a class inheritance diagram for the following set of class: 
# - Class Goat extends object and adds an instance variable _tail and methods milk() and jump()
# - Class Pig extends object and adds an instance variable _nose and methods eat(food) and wallow()
# - Class Horse extends object and adds instance variables _height and _color, and methods run() and jump()
# - Class Race extends Horse and adds a method race()
# - Class Equestrian extends Horse, adding an instance variable _weight and methods trot() and is_trained()

"""
            object 
        /     |     \ 
   Horse     Goat     Pig
  /     \
Racer   Equestrian


|--------------------------|    
|Class: Goat               | 
|--------------------------|
|Fields:                   |
|_tail                     |
|--------------------------| 
|Behaviors:                |
|milk()                    | 
|jump()                    |
|--------------------------| 

|--------------------------|
|Class: Pig                | 
|--------------------------|
|Fields:                   |
|_nose                     |
|--------------------------| 
|Behaviors:                |
|eat(food)                 | 
|wallow()                  |
|--------------------------| 

|--------------------------|
|Class: Horse              | 
|--------------------------|
|Fields:                   |
|_height    _color         |
|--------------------------| 
|Behaviors:                |
|run()                     | 
|jump()                    |
|--------------------------| 

|--------------------------|
|Class: Racer              | 
|--------------------------|
|Fields:                   |
|--------------------------| 
|Behaviors:                |
|race()                    |
|--------------------------| 

|--------------------------|
|Class: Equestrian         | 
|--------------------------|
|Fields:                   |
|_weight                   |
|--------------------------| 
|Behaviors:                |
|trot()                    | 
|is_trained()              |
|--------------------------| 

"""

##############################################################

##############################################################

# 2.24
# What are the primary classes and methods that a Python Softwere for an e-book reader needs? We don't need to write any code
# for this project but we have to include an inheritance diagram for it. The softwere architecture should at least include ways
# for costumers to buy new books, view their list of purchased books, read their purchased books

# Book --> Main class 
# E-book --> Extending book class 

"""
Inheritance diagram: 

    Book
      |
    E-Book 

"""

# Methods: 
# purchase_book()
# view_purchased()
# read_purchased()

##############################################################

##############################################################

# 2.25
# In 2.12 and 2.14 we have implemented two methods: one for the multiplication of a vector for a scalar, another for the 
# dot product between two vectors. Give a single implementation of the __mul__ method that use type checking to support 
# both syntaxes, u * v (u and v are vectors) and u * k (where k is an int number). 

##############################################################

class Vector3(AlternativeVector):
    """Extends the AlternativeVector class"""
    def __init__(self, d):
        super().__init__(d)

    def __mul__(self, other):
        """On the base of the 'other's' type it will return:
        - The vector coordinates if other is an int
        - The dot product if other is an iterable representing another vector
        """
        if isinstance(other, int):
            result = Vector3(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other  
            return result 
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError("Dimensions must agree") 
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i] 
        else: 
            raise ValueError("This type is not supported")


##############################################################

# 2.28, 2.29
# 2.28: PredatoryCreditCard class provides a process_month method that models the completition of a monthly cycle. 
# Modify the class so that once a customer has made ten calls to charge() in the current month, each additional 
# call to that function results in an additional $1 surcharge 
# 2.29: Modify PredatoryCreditCard so that a customer is assigned a minimum monthly payment, as a percentage of the balance, 
# and so that a late fee is assessed if the customer does not subsequentialy pay that minimum amount before the next 
# monthly cycle

##############################################################

class PredatoryCreditCard2(PredatoryCreditCard):
    MAX_CHARGES = 10
    MINIMUM_PCT = 0.1
    LATE_FEE = 10

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr 
        self._num_charges = 0 
        self._minimum_payment = 0

    def charge(self, price):
        success = super().charge(price)
        if not success: 
            self._balance += 5 
        else: 
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES: 
                self._balance += 1
        return success 

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        self._num_charges = 0   # reset the counter at the beginning of the month 
        if self._minimum_payment >0:
            self._balance += self.LATE_FEE
        if self._balance >0:
            self._minimum_payment = self._balance * self.MINIMUM_PCT

    def make_payment(self, value):
        if super().make_payment(value):
            self._minimum_payment = max (0, self._minimum_payment - value)
