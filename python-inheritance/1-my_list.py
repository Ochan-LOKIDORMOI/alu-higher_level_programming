#!/usr/bin/python3
""" Write a class MyList that inherits from list: """


class MyList(list):
    """ Sorts lists object """

    def print_sorted(self):
        """ Print sorted list """
        copy_list = self[:]
        copy_list.sort()
        print('{}'.format(copy_list))
