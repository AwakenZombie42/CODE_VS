class Dog:
    species = "Canine" # Class attribute
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute
    def description(self):
        return f"{self.name} is {self.age} years old."

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.name)
print(dog1.species)
print(dog2.name)
print(dog2.species)

print(dog1.description())
print(dog2.description())