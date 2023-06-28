from file_reader import FileReader
from input_reader import InputReader
from objects_list import ObjectsList

def correct_file_name():
     while True: 
            name = input("Ingrese el nombre del archivo en el cual posee las instrucciones de input: ")
            if name[-4:] == ".txt":
                return name
            else:
                print("Error, por favor agregar '.txt' al final del nombre")
#=================================================================================================================
input_folder = "data/"
f = FileReader(input_folder)
o = ObjectsList()
#=================================================================================================================
busses_list = f.busses_reader()
busses_objects = o.busses_objects(busses_list)

teachers_list = f.teachers_reader()
teachers_objects = o.teachers_objects(teachers_list)
teachers_ruts = f.teachers_ruts()

students_list = f.students_reader()
students_objects = o.students_objects(students_list)
students_ruts = f.students_ruts()

drivers_list = f.drivers_reader()
drivers_objects = o.drivers_objects(drivers_list)
drivers_ruts = f.drivers_ruts()

classrooms_list = f.classrooms_reader()
classrooms_objects = o.classrooms_objects(classrooms_list)
#=================================================================================================================
input_filename = correct_file_name()
input_reader = InputReader('input.txt')
input_commands = input_reader.read_file()
#=================================================================================================================
for command in input_commands:
    if 'LETS' in command:
        try:
            teachers_objects[command[0]].add_student(command, classrooms_objects, busses_objects)
        except:
            print('Error, solo un profesor puede subir a un estudiante')

    elif 'GETS' in command:
        try:
            teachers_objects[command[0]].aboard_bus(command, busses_objects, classrooms_objects)
        except:
            try:
                drivers_objects[command[0]].aboard_bus(command, busses_objects)
            except:
                 print("El rut no corresponde ni a un profesor ni a un chofer")

    elif 'DRIVES' in command:
        empty_busses = []
        filled_busses = []
        for license_plate in busses_objects:
            if len(busses_objects[license_plate].passengers_list) == 0:
                empty_busses.append(license_plate)
            else:
                filled_busses.append(license_plate)

for i in range(len(filled_busses)):
    if len(busses_objects[filled_busses[i]].passengers_list) == len(classrooms_objects[teachers_ruts[i]].students_list) + 2:
        print(f"El bus {filled_busses[i]} se lleno correctamente, puede iniciar su viaje")
            
    else:
        print(f"El bus {filled_busses[i]} no puede iniciar su viaje, su lista de pasajeros aun no esta completa")