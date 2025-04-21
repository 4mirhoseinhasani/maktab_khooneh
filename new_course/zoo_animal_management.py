'''
Problem Description:
A zoo wants to create an animal management system. You need to design this system using object-oriented programming (OOP) in Python.

1. Introduction to Object-Oriented Programming (OOP Introduction)
Your task:
Define a class called Animal that has the following properties:

name (name of the animal)
species (species of the animal)
age (age of the animal)
sound (sound of the animal)
Then create an instance of this class for a "lion" and print its properties.
'''
class Animal():
    
    def __init__(self, name, spacies, age, sound):
        # A class attribute (zoo_name) has been added to specify the name of the zoo.
        self.zoo_name = 'Tehran Zoological Garden'
        self.name = name
        self.spacies = spacies
        self.age = age
        self.sound = sound

    # Add a make_sound method to the Animal class that prints the animal's sound.
    def Make_sound(self):
        return self.sound
    # Define an info method that prints the animal's details.

    def info(self):
        return f"A {self.age} year old {self.spacies}-type {self.name} , with {self.sound} sound."
    
    # The __str__ method is implemented in the Animal class so that when you print the object, the animal's characteristics are displayed.
    def __str__(self):
       return self.info()
    
# Create a new class called Bird from Animal that has a new property wing_span (wing size).
class Bird(Animal):
    
    def __init__(self, name, spacies, age, sound, wing_span):
        Animal.__init__(self, name, spacies, age, sound)
        self.wing_span = wing_span

    # The make_sound method has been rewritten to make different bird sounds.
    def Make_sound(self):
        return self.sound
    

lion = Animal('Kamran', 'Asiatic or Persian Lion', 7, 'GHRRRRRRRRRRRRRRR')
print(lion.info())

bird = Bird('Nightingale ', 'Iranian', 2, 'jikjik jikjik', '20-22.5 cm')
print(bird.info())