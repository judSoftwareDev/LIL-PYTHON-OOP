"""
CHALLENGE OBJECTIVES:
- provided with a base class, Animal
- includes properties (name, sound)
- includes method/def/function: make_sound to print the sound

* CREATE TWO SUB CLASSES WHICH INHERIT FROM Animal:
- Dog
- Cat

* ADD ADDITIONAL METHODS:
- wag_tail() for dog
- purr() for Cat
- each will print a simple message
"""

class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(f"His pet's name is: {self.name} and is doing {self.sound}")
        
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
    def wag_tail(self):
        print(f"{self.name}'s tail is wagging.")    

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
    def purr(self):
        print(f"{self.name}'s is purring.")

pet_dog = Dog('Pony', 'arf arf')
pet_dog.make_sound()
pet_dog.wag_tail()

pet_cat = Cat('Mingming', 'meow')
pet_cat.make_sound()
pet_cat.purr()    





    
    
    
    
    
    
