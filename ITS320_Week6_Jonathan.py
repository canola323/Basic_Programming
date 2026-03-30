 #-------------------------------------------
# Program Name: Animal Shelter Management System
# Author: Jonathan Canola
# Date: 03/24/2026
#-------------------------------------------
# Pseudocode: [See suggestions below]
#-------------------------------------------
# Program Inputs: [See suggestions below]
# Program Outputs: [See suggestions below]
#-------------------------------------------


from abc import ABC, abstractmethod

# Animal Class 
class Animal(ABC):

    def __init__(self, name, age, species):

        self._name = name
        self._age = age
        self.species = species
        
    def display_details(self):
        print(f"Name: {self._name}, Age: {self._age}, Species: {self.species}")

    def age_update(self, new_age):
        if new_age > self._age:
            self._age = new_age

    @abstractmethod
    def speak(self):
        """Polymorphism"""
        pass

# Dog subclass
class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def bark(self):
        return "Woof!"
    
    def speak(self):
        return self.bark()

# Cat subclass
class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def meow(self):
        return "Meow"
    
    def speak(self):
        return self.meow()
    
class Shelter(ABC):
    @abstractmethod
    def add_animal(self, animal):
        pass

    @abstractmethod
    def remove_animal(self, name):
        pass

class ShelterInventory(Shelter):
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal._name} added to shelter.")

    def display_shelter(self):
        for pet in self.anmimals:
            pet.display_all()
            print(f"Sound: {pet.speak()}")  

# Main Menu Function
def MainMenu():
    shelter_guest = ShelterInventory()
    # Menu Loop until user exits program
    while True:

        print("-" * 40)
        print("Animal Shelter Management System")
        print("-" * 40)
        print("1. Add New Dog.")
        print("2. Add New Cat.")
        print("3. Display Current Animal Residents.")
        print("4. Exit.")
        # Asks user to select options 1-5
        user_choice = input("Please make a selection (e.g. 1 - 4): ")
        # Validates user makes valid selection

        if user_choice == '1':
            name = input("Enter the Dog's Name: ")
            age = int(input("Enter Dog's Age: "))
            breed = input("Enter Dog's Breed: ")
            new_dog = Dog(name, age, breed)
            shelter_guest.add_animal(new_dog)

        elif user_choice == '2':
            name = input("Enter the Cat's Name: ")
            age = int(input("Enter Cat's Age: "))
            breed = input("Enter Cat's Breed: ")
            new_cat = Cat(name, age, breed)
            shelter_guest.add_animal(new_cat)

        elif user_choice == '3':
            shelter_guest.display_all()

        elif user_choice == '4':
            print("-" * 40)
            print("Exiting program. Goodbye!")
            print("-" * 40)
            break

        else:
            print("*" * 40)
            print("Error: Enter valid selection.")
            print("*" * 40)

if __name__ == "__MainMenu__":
    MainMenu()