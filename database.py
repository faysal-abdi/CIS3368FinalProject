import mysql.connector

# MySQL database connection
connection = mysql.connector.connect(
    host='atelier-database.cfow8sqg0g8l.us-east-1.rds.amazonaws.com',
    user='Abdi',
    password='layaabdi',
    database='Aretas',
    port=3306
)