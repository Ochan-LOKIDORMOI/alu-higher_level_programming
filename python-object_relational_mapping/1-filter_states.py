#!/usr/bin/python3
"""
    This is a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    
    cursor = db.cursor()
    cursor.execute("SELECT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print('"{0}", '.format(state[0]), end='')
