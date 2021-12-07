class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        # return class name with width and height attributes
        return type(self).__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        # return an ascii representation of the shape
        pic_string = ""

        if self.height > 50 or self.width > 50:
            pic_string = "Too big for picture."
        else:
            i = 0
            while i < self.height:
                pic_string = pic_string + "*" * self.width + "\n"
                i += 1

        return pic_string

    def get_amount_inside(self, shape):
        # calculate how many of the shape can fit inside self
        return int(self.get_area() / shape.get_area())




class Square(Rectangle):
    # height and width are the same so set each other
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return type(self).__name__ + "(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height
