import sqlite3

try:
    connection = sqlite3.connect('countrydb.db')
    select_query = 'SELECT * FROM countries'

    cursor = connection.cursor()
    cursor.execute(select_query)
    countries = cursor.fetchall()

    select_singapore = 'SELECT * FROM countries WHERE id=2'
    cursor.execute(select_singapore)

    singapore = cursor.fetchone()
    print(singapore)

except sqlite3.Error as sql_error:
    print(sql_error)

except:
    print("there is an error " )

finally:
    if connection:
        connection.close()


for c in countries:
   print(c[1])


