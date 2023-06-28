from person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, rut):
        super().__init__(first_name, last_name, rut)
    
    def add_student(self, command, classroom_objects, busses_objects):
        teacher_rut = command[0]
        student_rut = command[2]
        classroom = classroom_objects[teacher_rut]
        license_plate = command[6]

        if student_rut in classroom.students_list:
            if license_plate in classroom.license_plate:
                busses_objects[classroom.license_plate].add_person(student_rut)

            else:
                print('Error, el estudiante se esta subiendo a un bus que no le corresponde')

        else:
            print(f'El estudiante no pertenece al curso del profesor {teacher_rut}')

    def aboard_bus(self, command, busses_objects, classroom_objects):
        student_list = classroom_objects[command[0]].students_list
        passenger_list = busses_objects[command[5]].passengers_list

        if len(student_list) == len(passenger_list):
            busses_objects[command[5]].add_person(self.rut)
            
        else:
            print("Aun no se suben todos los alumnos, el profesor no se puede subir")


        
