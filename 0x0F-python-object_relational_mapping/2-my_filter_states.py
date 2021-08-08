#!/usr/bin/python3
''' Selects states that is equal to the parameter '''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sqlquery = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    sqlquery += "ORDER BY id ASC;"
    cur.execute(sqlquery)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
