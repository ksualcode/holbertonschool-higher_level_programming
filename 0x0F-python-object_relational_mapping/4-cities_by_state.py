#!/usr/bin/python3
''' Selects states that start with N '''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sqlquery = "SELECT S.id, C.name, S.name FROM states S"
    sqlquery += " JOIN cities C ON S.id = C.state_id"
    sqlquery += " ORDER BY S.id ASC"
    cur.execute(sqlquery)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
