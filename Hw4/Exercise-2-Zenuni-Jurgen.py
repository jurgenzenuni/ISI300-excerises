#exercise 2

class Student:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__exams = []
    def displayStudent(self):
        print("Name:", self.__name, 
              "\nAddress:", self.__address) 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def add_exam(self, course_name, grade):
        self.__exams.append((course_name, grade))

    def get_grade(self, course_name):
        for exam in self.__exams:
            if exam[0] == course_name:
                return exam[1]

    def list_exams(self):
        for exam in self.__exams:
            print("Course:", exam[0], "- Exam Grades:", exam[1])

student1 = Student("John Smith", "918 Main St")
print(student1.get_name())
student1.set_name("Chris Smith")
student1.displayStudent()
student1.add_exam("Math", 93)
student1.add_exam("English", 88)
print(student1.get_grade("Math"))
student1.list_exams()
