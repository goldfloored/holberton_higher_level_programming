#!/usr/bin/python3
""" student module to define student class """


class Student:
    """ define student class """
    def __init__(self, first_name, last_name, age):
        """ init modules """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation """
        return (self.__dict__)
