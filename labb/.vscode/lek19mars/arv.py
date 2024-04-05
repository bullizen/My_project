# Basklass
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Härledd klass (Barnklass)
class Dog(Animal):
    def __init__(self, name):
        # Anropa basklassens konstruktor
        super().__init__("Dog")
        self.name = name

    def make_sound(self):
        return "Woof!"

# Härledd klass (Barnklass)
class Cat(Animal):
    def __init__(self, name):
        # Anropa basklassens konstruktor
        super().__init__("Cat")
        self.name = name

    def make_sound(self):
        return "Meow!"

# Skapa en instans av Dog och Cat
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

# Använd metoder från basklassen och de härledda klasserna
print(f"{my_dog.name} the {my_dog.species} says: {my_dog.make_sound()}")
print(f"{my_cat.name} the {my_cat.species} says: {my_cat.make_sound()}")

# I detta exempel är Animal basklassen som definierar en allmän struktur för alla djur. Både Dog och Cat är härledda klasser som ärver från Animal och utökar funktionaliteten genom att implementera sina egna versioner av make_sound-metoden. Genom att använda arv kan vi återanvända kod och etablera en relation mellan olika typer av djurklasser.