import mysql.connector

# function to make connection with the database

def get_db_connection():
  conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ntando_01',
    database = 'poonuhchee'
  )

  return conn