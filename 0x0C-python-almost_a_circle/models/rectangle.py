#!/usr/bin/python3
<<<<<<< HEAD
import turtle
import json
""" first class Base"""
class Base:
    """ first class Base"""
    """private class attribute __nb_objects = 0"""
    __nb_objects = 0
    """class constructor"""
    def __init__(self, id=None):
        """ class constructor """
        if id is not  None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
    def to_json_string(list_dictionaries):
        """static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    def save_to_file(cls, list_objs):
        """lass method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dict))
    def from_json_string(json_string):
        """static method def from_json_string(json_string): that returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)
    def create(cls, **dictionary):
        """ class method def create(cls, **dictionary): that returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 1, 1, **dictionary)
        else:
            instance = cls(1, 1, 1, **dictionary)
        instance.update(**dictionary)
        return instance
    def load_from_file(cls):
        """class method def load_from_file(cls): that returns a list of instances:"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dict = cls.from_json_string(json_string)
                list_instance = [cls.create(**d) for d in list_dict]
                return list_instance
        except Exception:
            return []
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(cls.csv_header())
            for obj in list_objs:
                writer.writerow(obj.to_csv())
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            list_objs = [cls.from_csv(row) for row in reader]
        return list_objs
    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.color("black")
        pen.speed(0)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.right(90)
                pen.forward(rect.height)
                pen.right(90)
            pen.hideturtle()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(square.size)
                pen.right(90)
            pen.hideturtle()
        turtle.done()
=======
"""class Rectangle that inherits from Base"""
from models.base import Base
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
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
<<<<<<< HEAD
=======
        """set/get the width rectangle"""
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
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
<<<<<<< HEAD
=======
        """set/get the height rectangle"""
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
        if not isinstance(height,int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = height
    @property
    def x(self):
<<<<<<< HEAD
=======
        """set/get the x rectangle"""
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
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
<<<<<<< HEAD
=======
        """set/get the y rectangle """
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
        return self.__y
    @y.setter
    def y(self,y):
        if not isinstance(y ,int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
<<<<<<< HEAD
    def area(self): 
        """that returns the area value of the Rectangle instance."""
        return self.__width * self.__height
    def display(self):
        for h in range (self.height):
            for w in range (self.width):
                print("#", end= "")
            print()
=======
    def area(self):
        """def area(self): that returns the area value of the Rectangle instance."""
        return self.__width *self.__height
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
    def __str__(self):
        """__str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.__x,self.__y,self.__width,self.__height)
    def display(self):
        """ public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here."""
        for i in range(self.height):
            for j in range(self.width):
                for y in range(self.y):
                    for x in range(self.x):
                        if y == 0:
                            print()

                        elif i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1 or u != 0:
                            print("#", end="")
                        else:
                            print(" ", end="")
            print()
<<<<<<< HEAD
    def update(self,*args, **kwargs):
=======
    def update(self, *args, **kwargs):
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
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
<<<<<<< HEAD
            self.__height = args[2] 
=======
            self.__height = args[2]
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width= args[1]
<<<<<<< HEAD
            self.__height = args[2] 
=======
            self.__height = args[2]
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
            self.__x = args[3]
            self.__y = args[4]
    def to_dictionary(self):
        """public method def to_dictionary(self): that returns the dictionary representation of a Rectangle"""
<<<<<<< HEAD
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}    
    @classmethod
    def csv_header(cls):
        return ['id', 'width', 'height', 'x', 'y']

    def csv_data(self):
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv_data(cls, data):
        id, width, height, x, y = data
        return cls(id, width, height, x, y)
=======
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}

>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d
