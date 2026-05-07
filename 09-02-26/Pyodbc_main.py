from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pyodbc

app = FastAPI()

# Database connection
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"  # replace with your server name
    "Database=TeaDB;"    # replace with your database name
    "Trusted_Connection=yes;"  # or use UID/PWD for SQL auth
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

@app.get("/")
def read_root():
    return {"message": "welcome to yash world"}

@app.get("/teas")
def get_teas():
    cursor.execute("SELECT id, name, origin FROM teas")
    rows = cursor.fetchall()
    return [{"id": row.id, "name": row.name, "origin": row.origin} for row in rows]

@app.post("/teas")
def add_teas(tea: Tea):
    cursor.execute(
        "INSERT INTO teas (id, name, origin) VALUES (?, ?, ?)",
        tea.id, tea.name, tea.origin
    )
    conn.commit()
    return {"message": "Tea added successfully okay"}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    cursor.execute(
        "UPDATE teas SET name=?, origin=? WHERE id=?",
        updated_tea.name, updated_tea.origin, tea_id
    )
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "tea not found"}
    return {"message": "Tea updated successfully"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    cursor.execute("DELETE FROM teas WHERE id=?", tea_id)
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "tea not found"}
    return {"message": "Tea deleted successfully"}