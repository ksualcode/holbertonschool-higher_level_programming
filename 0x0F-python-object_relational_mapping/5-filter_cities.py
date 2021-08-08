#!/usr/bin/python3
''' Selects states that start with N '''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sqlquery = "SELECT C.name FROM states S"
    sqlquery += " JOIN cities C ON S.id = C.state_id"
    sqlquery += " WHERE S.name LIKE BINARY %(stateName)s ORDER BY C.id ASC"
    cur.execute(sqlquery, {'stateName': argv[4]})
    query_rows = cur.fetchall()
    string = ""
    for row in query_rows:
        string += str(row)[2:-3] + ", "
    print(string[:-2])
    cur.close()
    conn.close()
