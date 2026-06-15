class School:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f'School: {self.name}')

class Student(School):
    def __init__(self,name,student_name,year,age,height):
        super().__init__(name)
        self.student_name = student_name
        self.year = year
        self.age = age
        self.height = height
    def details(self):
        print('The details of the student are: ')
        print(f'Name: {self.student_name}')
        print(f'Year: {self.year}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')

obj1 = Student('Westminister school','Tom','5','10','140cm')
obj1.display()
obj1.details()

obj2 = Student('Laytmer school','Jack','3','7','125cm')
obj2.display()
obj2.details()