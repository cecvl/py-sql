from cs50 import SQL
import pandas as pd;
db = SQL("sqlite:///swahili.db")

#Q: import specific columns from a csv files
# A: pd.read_csv('file.csv', usecols=['column1', 'column2'])
#Q: read the columns from csv file to a database
# A: df.to_sql('table_name', con=engine)
# Q: explain con=engine
# A: con=engine is the connection to the database
# Q: how do you create a connection to a database
# A: engine = create_engine('sqlite:///database.db')
# Q: clear a database tables

#Q: table with six fields
# A: CREATE TABLE IF NOT EXISTS users (name TEXT, age NUMBER


#Q: copy data from an original csv with specific columns only
#A: 
people = db.execute("SELECT * FROM words")
print(people)
