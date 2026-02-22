

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        double_width = pow(self.width, 2)
        double_height = pow(self.height, 2) 
        return pow((double_width + double_height), 0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        
        for j in range(self.height):
            for i in range(self.width):
                picture += "*"
                if i == self.width - 1:
                    picture += "\n" 

        return picture

    def get_amount_inside(self, shape):
        num_width = self.width // shape.width
        num_height = self.height // shape.height
        num_shape = num_width * num_height
        return num_shape
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return f"Square(side={self.width})"    
    
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
    
rect = Rectangle(3, 6)
print(rect)  # Output: Rectangle(width=3, height=6)
print(rect.get_perimeter())
sq = Square(5)
print(f"Is instance of Square? {isinstance(sq, Square)}")     # True
print(f"Is instance of Rectangle? {isinstance(sq, Rectangle)}") # True
print(sq) # Output: Square(side=5)