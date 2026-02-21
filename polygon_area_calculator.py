

class Rectanggle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        self._height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2(self.height + self.height)
    
    def get_diagonal(self):
        double_width = pow(self.width, 2)
        double_height = pow(self.height, 2) 
        return pow((double_width + double_height), 0.5)
    
    def get_picture(self):
        pass

    
    