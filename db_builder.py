import sqlite3 as lite

con = lite.connect(r"./die_zeit.db")

with con:

    cur = con.cursor()


    cur.execute("CREATE TABLE Articles(id INT, uuid TEXT, title TEXT, releaseDate DATETIME, subtitle TEXT, uri TEXT, href TEXT)")






