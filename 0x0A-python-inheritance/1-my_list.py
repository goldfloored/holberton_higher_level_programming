#!/usr/bin/python3
""" print sorted list module """


class MyList(list):
    """print list class"""
    def print_sorted(self):
        print(sorted(self))
