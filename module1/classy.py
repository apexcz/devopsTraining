from abc import abstractmethod

class Animal:
    def __init__(self):
        self.distance_traveled_in_km = 0
        self.time_taken_in_mins = 0

    def move(self, distance):
        distance_moved = 0
        while(distance_moved < distance):
           self.time_taken_in_mins += self.time_to_travel_one_km()
           self.distance_traveled_in_km += 1
           distance_moved += 1

    @abstractmethod
    def time_to_travel_one_km(self):
        pass

class Bird(Animal):
    def time_to_travel_one_km(self):
        return 5

class Dog(Animal):
    def time_to_travel_one_km(self):
        return 20 if self.is_tired() else 10

    def is_tired(self):
        return self.distance_traveled_in_km >= 5


myBird = Bird()
myDog = Dog()

myBird.move(10)
myDog.move(10)

print(myBird.time_taken_in_mins)
print(myDog.time_taken_in_mins)
