#Exercise 3

class Professor:
    def __init__(self, name):
        self.__name = name
        self.__allowed_courses = []
        self.__scheduled_courses = []
        
    def displayProfessor(self):
        print("Professor:", self.__name)

    def get_name(self):
        return self.__name
    def get_allowed_courses(self):
        return self.__allowed_courses
    def get_scheduled_courses(self):
        return self.__scheduled_courses

    def add_allowed_course(self, course):
        self.__allowed_courses.append(course)
            
    def remove_allowed_course(self, course):
        self.__allowed_courses.remove(course)

    def add_scheduled_course(self, course, semester):
        if course not in self.__allowed_courses:
            print(self.__name, "isnt allowed to teach", course)
            return
        else:
            self.__scheduled_courses.append((course, semester))
        

    def remove_scheduled_courses_by_semester(self, semester):
        self.__scheduled_courses = [course for course in self.__scheduled_courses if course[1] != semester]

    def remove_scheduled_courses_by_course(self, course):
        self.__scheduled_courses = [c for c in self.__scheduled_courses if c[0] != course]


prof1 = Professor("Paul Johnson")
prof1.displayProfessor()
prof1.add_allowed_course("CSC100")
prof1.add_allowed_course("CSC300")
prof1.add_allowed_course("ISI300")
prof1.add_allowed_course("ISI374")
#print(prof1.get_allowed_courses())
#prof1.remove_allowed_course("CSC300")
#print(prof1.get_allowed_courses())
prof1.add_scheduled_course("CSC300", "Fall 2020")
prof1.add_scheduled_course("CSC200", "Fall 2020")
prof1.add_scheduled_course("ISI300", "Fall 2021")
prof1.add_scheduled_course("ISI374", "Spring 2023")
print(prof1.get_scheduled_courses())
prof1.remove_scheduled_courses_by_semester("Fall 2020")
prof1.remove_scheduled_courses_by_course("ISI374")
print(prof1.get_scheduled_courses())






