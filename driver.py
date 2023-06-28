from person import Person

class Driver(Person):
    def __init__(self, first_name, last_name, rut, license_plate):
        super().__init__(first_name, last_name, rut)
        self.license_plate = license_plate

    def aboard_bus(self, command, busses_objects):
        if self.license_plate == command[5]:
            busses_objects[self.license_plate].add_person(self.rut)
        
        else:
            print('El conductor se esta subiendo a un bus que no corresponde')