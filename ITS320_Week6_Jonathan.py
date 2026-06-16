 #-------------------------------------------
# Program Name: Animal Shelter Management System
# Author: Jonathan Canola
# Date: 03/29/2026
#-------------------------------------------
# Pseudocode: 
# Imoort ABC abstractmethod
# Create base Animal class
# Create Dog subclass of Animal that takes name, age, breed
# Create Cat subclass of Animal that takes name, age, color
# Create Shelter class with both add and remove @abstractmethod
# Create ShelterInventory class that inherits Shelter
# ShelterInventory holds add, remove, and display methods
# Create MainMenu loop
# MainMenu prompts user to pick between 1-4 of printed choices 
# Choice 1 propomts user to add dog
# Choice 2 propmts user to add cat
# Chocie 3 prompts user to display inventory
# Choice 4 Exits program
# Print error message if invalid input
#-------------------------------------------
# Program Inputs: main menu selection 1-4, dog details (name, age, breed), and cat details (name, age, color)
# Program Outputs: Menu selection, lets user know is valid input, lets user know if dog or cat was added, displays inventory in shelter, exits program
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
    # Dog takes name, age, and breed 
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed
    # prints specific dog to bark
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
    
    def remove_animal(self, name):
        for animal in self.animals:
            self.animals.remove(animal)
            print(f"{name} has successfully been removed from shelter!")
            return
        print(f"{name} not found in shelter inventory.")

    def display_shelter(self):
        for pet in self.animals:
            pet.display_details()
            print(f"Sound: {pet.speak()}")  

# Main Menu Function
def MainMenu():
    my_shelter = ShelterInventory()
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
        # If user input is 1 prompts user to add dog detail for shelter inventory
        if user_choice == '1':
            name = input("Enter the Dog's Name: ")
            age = int(input("Enter Dog's Age: "))
            breed = input("Enter Dog's Breed: ")
            new_dog = Dog(name, age, breed)
            my_shelter.add_animal(new_dog)
        # If user input is 2 prompts user to add cat details for shelter inventory
        elif user_choice == '2':
            name = input("Enter the Cat's Name: ")
            age = int(input("Enter Cat's Age: "))
            color = input("Enter Cat's Color: ")
            new_cat = Cat(name, age, color)
            my_shelter.add_animal(new_cat)
        # If user input is 3 displays currenty shelter inventory
        elif user_choice == '3':
            my_shelter.display_shelter()
        # If user input is 4 exits program
        elif user_choice == '4':
            print("-" * 40)
            print("Exiting program. Goodbye!")
            print("-" * 40)
            break
        # If user enters anything else besides 1-4 propmts error message
        else:
            print("*" * 40)
            print("Error: Enter valid selection.")
            print("*" * 40)
# Runs loop for program
if __name__ == "__main__":
    MainMenu()