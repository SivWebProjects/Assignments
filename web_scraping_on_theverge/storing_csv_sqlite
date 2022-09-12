# Import required libraries
import sqlite3 as sq
import pandas as pd

# Create a connection object,
# Make a new db if not exist already 
# and connect it, if exist then connect.
connection = sq.connect('login_db.db')
 
# Create a cursor object
cur = connection.cursor()
 
# Run create table sql query
cur.execute("create table if not exists news" +
             " (id integer PRIMARY KEY, url text, headline text, author text, date text)")

# Load CSV data into Pandas DataFrame
csv_file_path = 'news.csv'
news = pd.read_csv(csv_file_path)

# Write the data to a sqlite db table
news.to_sql('news', connection, if_exists='replace', index=False)
   
"""
# Run select sql query
cur.execute('select * from news')
 
# Fetch all records
# as list of tuples
records = cur.fetchall()
 
# Display result 
for row in records:
    # display row
    print(row)
"""
     
# Close connection to SQLite database
connection.close()
