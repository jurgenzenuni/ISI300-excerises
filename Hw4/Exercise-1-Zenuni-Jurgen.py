#Exercise 1
#Students Section
class Student:
    def __init__(self, name, address, completed_courses=None, grades=None):
        self._name = name
        self._address = address
        self._completed_courses = completed_courses or []
        self._grades = grades or []
    def displayStudent(self):
        print("Name:", self._name, 
              "\nAddress:", self._address, 
              "\nCompleted Courses:", self._completed_courses,
              "\nGrades:", self._grades) 

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_completed_courses(self):
        return self._completed_courses

    def set_completed_courses(self, completed_courses):
        self._completed_courses = completed_courses

    def get_grades(self):
        return self._grades

    def set_grades(self, grades):
        self._grades = grades


#student1 = Student("John Smith", "123 Main St")
#print(student1.get_address())
#student1.set_name("Chris James")
#print(student1.get_name())
#student1.set_completed_courses(["English", "Math"])
#print(student1.get_completed_courses())
student2 = Student("Jurgen Zenuni", "300 test st", ["Math", "Science"], ["A", "B-"])
student2.displayStudent()
#print(student2.get_grades())

#Professor section
class Professor:
    def __init__(self, name, address, courses_taught = None):
        self._name = name
        self._address = address
        self._courses_taught = courses_taught or []
    def displayProfessor(self):
        print("Name:", self._name,
              "\nAddress:", self._address,
              "\nCourses Taught:", self._courses_taught)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address
    def set_address(self, address):
        self._address = address

    def get_courses_taught(self):
        return self._courses_taught
    def set_courses_taught(self, courses_taught):
        self._courses_taught = courses_taught

prof1 = Professor("Caleb Johnson", "505 ND lane", ["csc315", "isi300", "csc126"])
#print(prof1.get_name(), prof1.get_address())
prof1.displayProfessor()
