
class student:
    def __init__(self,name):
        self.name = name
        self.__grade =0
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 to 100")
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade >=60:
            return "Passed"
        else:
            return "Failed"
Student = student("Emil")
Student.set_grade(85)
print(Student.get_grade())
print(Student.get_status())
