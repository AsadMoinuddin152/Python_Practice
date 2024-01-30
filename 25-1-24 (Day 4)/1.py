from abc import ABC, abstractmethod

# Abstract base class 'Animal' with abstract methods 'sound' and 'eat'
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        print('Animal eating')

# Concrete class 'pet_animals' inheriting from 'Animal'
class pet_animals(Animal):
    def sound(self):
        print("pet animals sound")

    def eat(self):
        print("pet animals eat")

# Abstract base class 'Loan' with abstract methods 'get_interest_rate' and 'calculate_interest'
class Loan(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

# Concrete class 'general_loan' inheriting from 'Loan'
class general_loan(Loan):
    def get_interest_rate(self):
        print("general loan interest rate")

    def calculate_interest(self):
        print("general loan calculate interest")

# Instantiate objects of concrete classes
pet_obj = pet_animals()
loan_obj = general_loan()

# Invoke the 'eat' method of 'pet_animals' and print the result
print(pet_obj.eat())
