class Bus:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.passengers_list = []
        
    def add_person(self, person_rut):
        self.passengers_list.append(person_rut)
    
