import sqlite3

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    query = 'Create table IF NOT EXISTS Roster (name TEXT, species TEXT, age INT)'
    cursor.execute(query)
    cursor.execute("SELECT * FROM Roster")
    rows = cursor.fetchall()
    print(rows)

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    query = "Insert into Roster (name, species, age) values('Benjamin Sisko', 'Human', 40 )"
    cursor.execute(query)
    query = "Insert into Roster (name, species, age) values('Jadzia Dax', 'Trill', 300 )"
    cursor.execute(query)
    query = "Insert into Roster (name, species, age) values('Kira Nerys', 'Bajoran', 29 )"
    cursor.execute(query)

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    query = "Update Roster set name = 'Ezri Dax' where name = 'Jadzia Dax'"
    cursor.execute(query)

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    query = "Select name, age from Roster where species = 'Bajoran'"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
