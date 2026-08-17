import sqlite3
from models.supply_item import SupplyItem

DATABASE_PATH = "data/ready_set_school.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

# create supplies table
def create_supplies_table():
    connection = create_connection()    # connect to database
    cursor = connection.cursor()        # create SQL command handler

    # send SQL command
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS supplies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        condition TEXT NOT NULL,
        colour TEXT,
        specification TEXT,
        notes text
        )        
    """)

    connection.commit()     # save changes
    connection.close()      # close connection

# add supplies to table
def add_supply(supply):
    connection = create_connection()
    cursor = connection.cursor()

    # '?' are placeholders
    # adds a new row to the supplies table
    cursor.execute("""
        INSERT INTO supplies (          
        name,
        quantity,
        condition,
        colour,
        specification,
        notes
        )        
        VALUES (?, ?, ?, ?, ?, ?)       
    """, (
        supply.name,
        supply.quantity,
        supply.condition,
        supply.colour,
        supply.specification,
        supply.notes
    ))

    connection.commit()
    connection.close()

# retrieve/return the supplies in table
def get_all_supplies():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM supplies")
    rows = cursor.fetchall()

    connection.close()

    supplies = []

    for row in rows:
        supply = SupplyItem(
            name = row[1],
            quantity=row[2],
            condition=row[3],
            colour=row[4],
            specification=row[5],
            notes=row[6],
            id=row[0]
        )

        supplies.append(supply)

    return supplies

# update the supplies in the table
def update_supply(supply):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE supplies
        SET
            name = ?,
            quantity = ?,
            condition = ?,
            colour = ?,
            specification = ?,
            notes = ?
        WHERE id = ?
    """, (
        supply.name,
        supply.quantity,
        supply.condition,
        supply.colour,
        supply.specification,
        supply.notes,
        supply.id
    ))

    connection.commit()
    connection.close()

def delete_supply(supply_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM supplies WHERE id = ?",
        (supply_id,)
    )

    connection.commit()
    connection.close()