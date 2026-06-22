class Shape:
    def __init__(self):
        pass
    def area(self):
        area = print('Area not defined')

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        length = int(input('What is the length of the rectangle '))
        width = int(input('What is the width of the rectangle '))
        area = length * width
        print(f'Area of the rectngle is {area}')

class Circle(Shape):
    def __init__(self):
        super().__init__()
        radius = int(input('What is the radius of the circle '))
        area = 3.14 * radius * radius
        print(f'Area of your circle = {area}')

obj1 = Shape()
obj1.area()
obj2 = Rectangle()
obj3 = Circle()


