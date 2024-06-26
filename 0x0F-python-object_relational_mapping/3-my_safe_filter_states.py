#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    select_n = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT * FROM states WHERE name = '{}' ORDER BY id ASC".format(select_n))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
