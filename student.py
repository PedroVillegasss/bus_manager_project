from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, rut):
        super().__init__(first_name, last_name, rut)
