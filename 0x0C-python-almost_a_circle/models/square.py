#!/usr/bin/python3
<<<<<<< HEAD
=======
"""class Square that inherits from Rectangle"""
>>>>>>> 26145cd71560b11a87c731dbe9ad848e206f989b
from models.rectangle import Rectangle
class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor:"""
        super().__init__(size,size,y,x,id)
        self.size = size
    def __str__(self):
        """he overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""
        return "[Square] ({}) {}/{} - {}".format(self.id,self.x,self.y,self.width)
    @property
    def size(self):
        """The setter should assign (in this order) the width and the height - with the same value"""
        return self.width
    @size.setter
    def size(self, size):
        """The setter should assign (in this order) the width and the height - with the same value"""
        self.width = size
        self.height = size
    def update(self, *args, **kwargs):
        """ public method def update(self, *args, **kwargs) that assigns attributes:"""
        if len(args) == 0 and len(kwargs) != 0:
            """ public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:"""
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "id":
                    self.id = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.size= args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.size= args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.size= args[1]
            self.x = args[2]
            self.y = args[3]

    def to_dictionary(self):
        """public method def to_dictionary(self): that returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
<<<<<<< HEAD
=======

>>>>>>> 26145cd71560b11a87c731dbe9ad848e206f989b
