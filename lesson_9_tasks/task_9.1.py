class Rectangle:

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    def square(self):
        print(f'Square of rectangle = {self.side1 * self.side2}') 
    
    def perimeter(self):
        print(f'Perimeter of rectangle = {2 * (self.side1 + self.side2)}')


rectangle = Rectangle(10, 20)

print(f'side1 = {rectangle.side1}, side2 = {rectangle.side2}')

rectangle.square()
rectangle.perimeter()



