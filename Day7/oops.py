class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name: ",self.name)
        print("Age: ", self.age)
person = Person("Devika",25)
person.display_info()