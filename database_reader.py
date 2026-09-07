import sqlite3

connection = sqlite3.connect("genomic_data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM patients")
records = cursor.fetchall()

print("Here is the data pulled from the database:")
print(records)

connection.close()