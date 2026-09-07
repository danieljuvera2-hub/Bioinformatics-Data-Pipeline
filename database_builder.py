import sqlite3
connection = sqlite3.connect("genomic_data.db")
cursor = connection.cursor()

cursor.execute("""
    INSERT INTO patients (gene_name, expression_level)
    VALUES ('BRCA1', 154.2)
""")

connection.commit()
connection.close()

print("Patient data inserted successfully")