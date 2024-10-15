from cs50 import SQL
import pandas as pd;
db = SQL("sqlite:///test4.db")

#Q: show tables in testdb
tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(tables)

# columns = db.execute("SELECT * FROM conjugations")  
# print(columns)


