import pyodbc

print(pyodbc.drivers())

conn_str = "driver={SQL Server}; server=localhost; database={interns}; Trusted_Connection=yes;"

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

query = "select * from ai_intern"
query2 = "insert into ai_intern (Name,Age,Email,City) values ('harsh',20,'harsh@gmail.com','valsad')"
cursor.execute(query2)
conn.commit()

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
conn.close()