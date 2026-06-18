class Student:
    def __init__(self):
        self.name = ''
        self.year = ''

class Result(Student):
    def __init__(self):
        super().__init__()
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        self.total = 0
        self.average = 0
        
    def inputs(self):
        self.name = input('Enter the name of the student: ')
        self.year = input('Enter the year of the student: ')
        self.m1 = int(input('Enter the marks out of 100 for math: '))
        self.m2 = int(input('Enter the marks out of 100 for english: '))
        self.m3 = int(input('Enter the marks out of 100 for science: '))
        
    def average_marks(self):
        self.total = (self.m1 + self.m2 + self.m3) 
        self.average = self.total / 3
    
    def show_output(self):
        print('The details of the student are: ')
        print(f'Name: {self.name}')
        print(f'Year: {self.year}')
        print(f'Average mark: {self.average}')
        if self.average >= 90:
            print('You got A+')
        elif self.average >= 80:
            print('You got A')
        elif self.average >= 70:
            print('You got B')
        elif self.average >= 60:
            print('You got C')
        elif self.average >= 50:
            print('You got D')
        elif self.average >= 40:
            print('You got E')
        else:
            print('You failed')

obj1 = Result()
obj1.inputs()
obj1.average_marks()
obj1.show_output()