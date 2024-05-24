# Create a class called Person with attributes for name, age, and email. Implement validation to ensure that age is a 
# positive integer and email follows a valid format.

import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def validate_person(self):
        if not isinstance(self.age, int) or self.age <= 0:
            return "Age must be a positive integer."
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.email):
            return "Invalid email format."
        return True

# Example usage:
person1 = Person("John Doe", 25, "john.doe@example.com")
validation_result = person1.validate_person()
print(validation_result if validation_result is True else "Validation error:", validation_result)
