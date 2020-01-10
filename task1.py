class Student():
    def __init__(self,name,last_name,department,year_of_entrance):
        self.name = name
        self.last_name =last_name
        self.department = department
        self.year_of_entrance = year_of_entrance
    def get_student_info(self):
        return f"{self.name} {self.last_name} поступил на факультет {self.department} в {self.year_of_entrance} году"

student1 = Student("Иван","Иванов","Программирования""2017")
print(student1.get_student_info())