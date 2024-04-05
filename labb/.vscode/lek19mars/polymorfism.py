# Gemensam superklass
class Animal:
    def make_sound(self):
        pass

# Härledd klass (Barnklass)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Härledd klass (Barnklass)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Härledd klass (Barnklass)
class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# Funktion som använder polymorfism
def animal_sound(animal):
    return animal.make_sound()

# Skapa instanser av olika djur
my_dog = Dog()
my_cat = Cat()
my_bird = Bird()

# Använd polymorfism för att anropa make_sound-metoden för olika djur
print("Dog says:", animal_sound(my_dog))
print("Cat says:", animal_sound(my_cat))
print("Bird says:", animal_sound(my_bird))

# I detta exempel är Animal superklassen som definierar en gemensam metod make_sound. De härledda klasserna Dog, Cat, och Bird överskriver denna metod och implementerar sina egna versioner av ljudet som de gör. Funktionen animal_sound demonstrerar polymorfism genom att använda samma gränssnitt (make_sound) för olika typer av djur, vilket gör att vi kan behandla dem på ett enhetligt sätt även om de tillhör olika klasser.