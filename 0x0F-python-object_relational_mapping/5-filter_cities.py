#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb
"""script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    """script that lists all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE cities.name = %s ORDER BY cities.id ASC",(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    cur.close()
    db.close()
