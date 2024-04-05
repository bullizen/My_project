from abc import ABC, abstractmethod

# Abstrakt bas klass för ett fordon
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Klass för en bil som ärver från Vehicle
class Car(Vehicle):
    def start(self):
        return f"{self.make} {self.model} starts the engine."

    def stop(self):
        return f"{self.make} {self.model} stops the engine."

# Klass för en motorcykel som ärver från Vehicle
class Motorcycle(Vehicle):
    def start(self):
        return f"{self.make} {self.model} starts the ignition."

    def stop(self):
        return f"{self.make} {self.model} stops the ignition."


# Skapa en instans av en bil
my_car = Car("Toyota", "Corolla")
print(my_car.start())

# Skapa en instans av en motorcykel
my_bike = Motorcycle("Honda", "CBR500R")
print(my_bike.start())

# I detta exempel är Vehicle en abstrakt bas klass som definierar gränssnittet för ett fordon genom de abstrakta metoderna start och stop. Både Car och Motorcycle är konkreta klasser som ärver från Vehicle och måste implementera dessa abstrakta metoder. Detta möjliggör abstraktionen av fordonens beteenden, där användaren kan interagera med olika typer av fordon på samma sätt utan att behöva förstå de specifika detaljerna för varje fordonstyp.