import sqlite3

connection = sqlite3.connect('countrydb.db')
update_usa = "UPDATE countries SET population={0} WHERE id={1}" #update countries set population=329000000 where id=8

cursor = connection.cursor()
cursor.execute(update_usa.format(329000000, 8))

connection.commit()