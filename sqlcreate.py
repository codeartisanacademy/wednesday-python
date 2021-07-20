import sqlite3

connection = sqlite3.connect('countrydb.db')
insert_country = "INSERT INTO countries (name, population, continent) VALUES ('{0}',{1},'{2}')"

cursor = connection.cursor()
#print(insert_country.format('USA', 328000000, 'America'))
cursor.execute(insert_country.format('USA', 328000000, 'America'))

connection.commit()

print(cursor.lastrowid)