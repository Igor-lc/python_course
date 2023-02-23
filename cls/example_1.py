class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()

people = People("n")
#print(people.get_name())

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("willie", 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        # print("create object", self.restaurant_name, self.cuisine_type)

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

restaurant1 = Restaurant("Premier1", "Palace")
restaurant2 = Restaurant("Premier2", "Palace")
restaurant = Restaurant("Premier1", "Palace", 2)
print(restaurant)
'''
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
print(restaurant1.open_restaurant())
print(restaurant2.describe_restaurant())'''


class User:
    def __init__(self, first_name, age, professional):
        self.name = first_name
        self.age = age
        self.p = professional

    def describe_user(self):
        print(f"{self.name}")

    def greet_user(self):
        print(f"Hey, {self.first_name}")

user1 = User("Python", 30, "Backend_ingeneer")
#print(user1.name)
