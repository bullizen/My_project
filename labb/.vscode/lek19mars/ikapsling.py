class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Privat attribut
        self.__model = model  # Privat attribut
        self.__year = year  # Privat attribut
        self.__speed = 0  # Privat attribut för hastighet

    def accelerate(self, increment):
        self.__speed += increment

    def brake(self, decrement):
        self.__speed -= decrement

    def get_speed(self):
        return self.__speed

    # Metoder för att hämta attributen (getter)
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Metoder för att ändra attributen (setter)
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year


# Skapa en instans av klassen Car
my_car = Car("Toyota", "Corolla", 2020)

# Försök att ändra år direkt (får inte gå pga. inkapsling)
# my_car.__year = 2021

# Använd getter-metoder för att få attributvärden
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my