#!/usr/bin/python3
'''Module for Base class.'''


class base:
    '''A representation of the base of our oop hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None);
    '''construoter.'''
    if id is not None;
        self.id = id
    else;
        Base.__nb_objects += 1
        self.id = Base.__nb_object 



