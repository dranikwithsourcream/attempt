import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

#cur.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

#cur.execute("INSERT INTO employees VALUES ('Andrew', 'Derevianko', 99999)")

cur.execute("SELECT * FROM employees WHERE last='Derevianko'")

print(cur.fetchone())

con.commit()
con.close()