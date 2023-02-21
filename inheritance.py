class Person(object):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)

    def details(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))
# to inherit from above base class use the parentheses (round brackets) to indicate the parent class
class Voter(Person):
    # name / staff will be derived from the parent class
    def __init__(self, name , age , gender):
         self.name = name
         self.age = age
         self.gender = gender

    # invoke/call the init function in parent class
         Person.__init__(self,name,age, gender)

    # 5. Polymorphism : simply means having many forms
    # we perform polymorphism by defining the same method but giving a different output in the derived classes.
    def details(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))


#
a = Voter('Lucy',36,"female")
# call methods from the parent class
a.display()
a.details()

