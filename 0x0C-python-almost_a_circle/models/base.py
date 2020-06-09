#!/usr/bin/python3
"""[Base class]
"""
import json


class Base:
    """[Base]
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        n_lst = []
        if list_objs is not None:
            for x in range(len(list_objs)):
                n_lst += [list_objs[x].to_dictionary()]
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(n_lst))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        n_file = cls.__name__ + ".json"
        n_lst = []

        try:
            with open(n_file, 'r') as f:
                n_lst = cls.from_json_string(f.read())
            for a, _b in enumerate(n_lst):
                n_lst[a] = cls.create(**n_lst[a])
        except:
            pass
        return n_lst
