import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
  cursor = con.cursor()

  usuarios = [
    (2, "Pepe"),
    (3, "Juan")
  ]

  cursor.executemany(
    " insert into usuarios values(?, ?)",
    usuarios,
  )