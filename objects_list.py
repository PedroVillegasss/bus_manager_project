from file_reader import FileReader
from bus import Bus
from classroom import Classroom
from driver import Driver
from person import Person
from student import Student
from teacher import Teacher

class ObjectsList:
    def __init__(self):
        self

    def busses_objects(self, busses_list):
        busses_objects = {}
        for i in range(len(busses_list)):
            bus = Bus(busses_list[i])
            busses_objects[busses_list[i]] = bus
        return busses_objects
    
    def classrooms_objects(self, classrooms_list):
        classrooms_objects = {}
        for i in range(len(classrooms_list)):
            classroom = Classroom(classrooms_list[i]["name"], classrooms_list[i]["teacher_rut"], classrooms_list[i]["license_plate"], classrooms_list[i]["students"])
            classrooms_objects[classrooms_list[i]['teacher_rut']] = classroom
        return classrooms_objects
    
    def drivers_objects(self, drivers_list):
        drivers_object = {}
        for i in range(len(drivers_list)):
            driver = Driver(drivers_list[i]["first_name"], drivers_list[i]["last_name"], drivers_list[i]["rut"], drivers_list[i]["license_plate"])
            drivers_object[drivers_list[i]['rut']] = driver
        return drivers_object

    def students_objects(self, students_list):
        students_objects = {}
        for i in range(len(students_list)): 
            student = Student(students_list[i]["first_name"], students_list[i]["last_name"], students_list[i]["rut"])
            students_objects[students_list[i]['rut']] = student
        return students_objects
    
    def teachers_objects(self, teachers_list):
        teachers_objects = {}
        for i in range(len(teachers_list)):
            teacher = Teacher(teachers_list[i]["first_name"], teachers_list[i]["last_name"], teachers_list[i]["rut"])
            teachers_objects[teachers_list[i]['rut']] = teacher
        return teachers_objects
    