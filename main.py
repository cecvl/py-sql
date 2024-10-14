from cs50 import SQL
db = SQL("sqlite:///database.db")

db.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age NUMBER, fav_food STRING)")

# db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)",'Alice', 30, 'pizza')
# db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)",'Bob', 20, 'burgerss')

# people = db.execute("SELECT * FROM users")
# print(people)

people = db.execute("DELETE FROM users WHERE name = 'Bob'")
people = db.execute("SELECT * FROM users")
print(people)

