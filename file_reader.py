import os

class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
          
    def busses_reader(self):
        input_file = 'busses.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        
        busses = []
        for line in file:
            data = line.split()
            busses.append(data[0])
        file.close()
        return busses
       
    def classrooms_reader(self):
        input_file = 'classrooms.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        
        classrooms_list = []
        for line in file:
            classroom_dict = {}
            students_list = []
            data = line.strip().split(',')

            for i in range(len(data)):
                item = data[i]
                if i == 0:
                    classroom_dict['name'] = item
                elif i == 1:
                    classroom_dict['teacher_rut'] = item
                elif i == 2:
                    classroom_dict['license_plate'] = item
                else:
                    students_list.append(item)
            classroom_dict['students'] = students_list
            classrooms_list.append(classroom_dict)
        return classrooms_list
   
    def drivers_reader(self):
        input_file = 'drivers.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        drivers_list = []

        for line in file:
            driver_dict = {}
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 0:
                    driver_dict['first_name'] = item
                elif i == 1:
                    driver_dict['last_name'] = item
                elif i == 2:
                    driver_dict['rut'] = item
                elif i == 3:
                    driver_dict['license_plate'] = item
            drivers_list.append(driver_dict)
        return drivers_list
   
    def students_reader(self):
        input_file = 'students.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        
        students_list = []
        for line in file:
            student_dict = {}
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 0:
                    student_dict['first_name'] = item
                elif i == 1:
                    student_dict['last_name'] = item
                elif i == 2:
                    student_dict['rut'] = item
            students_list.append(student_dict)
        return students_list
  
    def teachers_reader(self):
        input_file = 'teachers.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding='utf-8')
        teachers_list = []
        for line in file:
            teacher_dict = {}
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 0:
                    teacher_dict['first_name'] = item
                elif i == 1:
                    teacher_dict['last_name'] = item
                elif i == 2:
                    teacher_dict['rut'] = item
            teachers_list.append(teacher_dict)
        return teachers_list
    
    def students_ruts(self):
        input_file = 'students.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        rut_students = []
        for line in file:
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 2:
                    rut_students.append(item)
        return rut_students
    
    def teachers_ruts(self):
        input_file = 'teachers.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding='utf-8')
        teachers_rut = []
        for line in file:
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 2:
                    teachers_rut.append(item)
        return teachers_rut

    def drivers_ruts(self):
        input_file = 'drivers.txt'
        file_path = os.path.join(self.folder_path, input_file)
        file = open(file_path, 'r', encoding = 'utf-8')
        drivers_rut = []
        for line in file:
            data = line.strip().split(',')
            for i in range(len(data)):
                item = data[i]
                if i == 2:
                    drivers_rut.append(item)
        return drivers_rut
    
    


                
