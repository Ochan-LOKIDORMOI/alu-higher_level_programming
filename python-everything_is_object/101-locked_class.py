#!/usr/bin/python3
"""def a locked class"""


class lockedclass:
    """
    Avoid the user from giving new lockedclass attributes
    for anything ut only for the one called 'first_name'.
    """

    __slots__ = ["first_name"]
