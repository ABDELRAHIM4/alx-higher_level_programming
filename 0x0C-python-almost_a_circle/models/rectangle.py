#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base
"""class Rectangle that inherits from Base"""
class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        """Call the super class with id"""
        super().__init__(id)
        """Private instance attributes, each with its own public getter and setter"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width (self):
        """set/get the width rectangle"""
        return self.__width
    @width.setter
    def width(self,width):
        if not isinstance(width ,int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        """set/get the height rectangle"""
        if not isinstance(height,int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = height
    @property
    def x(self):
        """set/get the x rectangle"""
        return self.__x
    @x.setter
    def x(self,x):
        if not isinstance(x ,int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    @property
    def y(self):
        """set/get the y rectangle """
        return self.__y
    @y.setter
    def y(self,y):
        if not isinstance(y ,int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    def area(self):
        """def area(self): that returns the area value of the Rectangle instance."""
        return self.__width *self.__height
    def __str__(self):
        """__str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.__x,self.__y,self.__width,self.__height)
    def display(self):
        """ public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here."""
        for i in range(self.height):
            for j in range(self.width):
                for x in range (self.x):
                    for y in range (self.y):
                        if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1 or x == 0 or y == 0:
                            print("#", end="")
                        elif x != 0:
                            print()
                        else:
                            print(" ", end="")
            print()
    def update(self, *args, **kwargs):
        """public method def update(self, *args): that assigns an argument to each attribute"""
        if len(args) == 0 and len(kwargs) != 0:
            """ public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:"""
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                elif key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width= args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width= args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width= args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width= args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
    def to_dictionary(self):
        """public method def to_dictionary(self): that returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}

