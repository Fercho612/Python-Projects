class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height 

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        for height in range(self.height):
            for width in range (self.width):
                picture += "*"
            picture += '\n'
        return picture
    
    def get_amount_inside(self, shape) -> int:
        max_in_width, a = divmod(self.width, shape.width)
        max_in_height, b = divmod(self.height, shape.height)
        return max_in_width * max_in_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size,size)
    
    def set_width(self, new_size):
        self.width = new_size
        self.height = new_size
    def set_height(self, new_size):
        self.width = new_size
        self.height = new_size

    def set_side(self, new_size):
        self.width = new_size
        self.height = new_size

    def __str__(self):
        return f"Square(side={self.width})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

