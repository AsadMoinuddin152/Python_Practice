from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        print('Animal eating')
class pet_animals(Animal):
    def sound(self):
        print("pet animals sound")

    def eat(self):
        print("pet animals eat")
        
class Loan(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
class general_loan(Loan):
    def get_interest_rate(self):
        print("general loan interest rate")

    def calculate_interest(self):
        print("general loan calculate interest")
pet_obj = pet_animals()
loan_obj = general_loan()

print(pet_obj.eat())
