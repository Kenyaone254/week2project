class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person("John", 36, "male")
print("Name:", p1.name, "Age:", p1.age, "Gender:", p1.gender)
