#!/usr/bin/python3
""" first class Base"""
class Base:
    """private class attribute __nb_objects = 0"""
    __nb_objects = 0
    def __init__(self, id=None):
        """ class constructor """
        if id != None:
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
