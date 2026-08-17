import sqlite3
from models.supply_item import SupplyItem
from models.school_supply_list import SchoolSupplyList
from models.required_item import RequiredItem

DATABASE_PATH = "data/ready_set_school.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

# CREATE SCHOOL SUPPLIES TABLE
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

# retrieve/return the supplies in the supplies table
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

# update the supplies in the supplies table
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

# delete supplies in the supplies table
def delete_supply(supply_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM supplies WHERE id = ?",
        (supply_id,)
    )

    connection.commit()
    connection.close()

# CREATE SCHOOL LIST TABLE

def create_school_lists_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS school_lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_name TEXT NOT NULL,
            grade TEXT NOT NULL,
            school_year TEXT NOT NULL,
            student_name TEXT
        )
    """)

    connection.commit()
    connection.close()

# add school list
def add_school_list(school_list):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO school_lists (
            school_name,
            grade,
            school_year,
            student_name
        )
        VALUES (?, ?, ?, ?)
    """, (
        school_list.school_name,
        school_list.grade,
        school_list.school_year,
        school_list.student_name
    ))

    connection.commit()
    connection.close()

def get_all_school_lists():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM school_lists")
    rows = cursor.fetchall()

    connection.close()

    school_lists = []

    for row in rows:
        school_list = SchoolSupplyList(
            school_name=row[1],
            grade=row[2],
            school_year=row[3],
            student_name=row[4],
            id=row[0]
        )

        school_lists.append(school_list)

    return school_lists

def update_school_list(school_list):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE school_lists
        SET
            school_name = ?,
            grade = ?,
            school_year = ?,
            student_name = ?
        WHERE id = ?
    """, (
        school_list.school_name,
        school_list.grade,
        school_list.school_year,
        school_list.student_name,
        school_list.id
    ))

    connection.commit()
    connection.close()

def delete_school_list(school_list_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM school_lists WHERE id = ?",
        (school_list_id,)
    )

    connection.commit()
    connection.close()

# CREATE REQUIRED ITEMS TABLE - RELATIONSHIP BETWEEN SCHOOL LISTS & REQUIRED ITEMS TABLES

def create_required_items_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS required_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_list_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            quantity_required INTEGER NOT NULL,
            colour TEXT,
            specification TEXT,
            notes TEXT,
            FOREIGN KEY (school_list_id)
                REFERENCES school_lists(id)
        )
    """)

    connection.commit()
    connection.close()

# add required school supply items
def add_required_item(required_item):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO required_items (
            school_list_id,
            name,
            quantity_required,
            colour,
            specification,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        required_item.school_list_id,
        required_item.name,
        required_item.quantity_required,
        required_item.colour,
        required_item.specification,
        required_item.notes
    ))

    connection.commit()
    connection.close()


# read required items
def get_all_required_items():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM required_items")
    rows = cursor.fetchall()

    connection.close()

    required_items = []

    for row in rows:
        required_item = RequiredItem(
            name=row[2],
            quantity_required=row[3],
            colour=row[4],
            specification=row[5],
            notes=row[6],
            school_list_id=row[1],
            id=row[0]
        )

        required_items.append(required_item)

    return required_items

# update required items
def update_required_item(required_item):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE required_items
        SET
            school_list_id = ?,
            name = ?,
            quantity_required = ?,
            colour = ?,
            specification = ?,
            notes = ?
        WHERE id = ?
    """, (
        required_item.school_list_id,
        required_item.name,
        required_item.quantity_required,
        required_item.colour,
        required_item.specification,
        required_item.notes,
        required_item.id
    ))

    connection.commit()
    connection.close()

# Delete required item
def delete_required_item(required_item_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM required_items WHERE id = ?",
        (required_item_id,)
    )

    connection.commit()
    connection.close()

# GET REQUIRED ITEM BY SCHOOL LIST - ALLOWS TO RETRIEVE ITEMS BY SCHOOL LIST ID
def get_required_items_by_school_list(school_list_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM required_items
        WHERE school_list_id = ?
    """, (school_list_id,))

    rows = cursor.fetchall()

    connection.close()

    required_items = []

    for row in rows:
        required_item = RequiredItem(
            name=row[2],
            quantity_required=row[3],
            colour=row[4],
            specification=row[5],
            notes=row[6],
            school_list_id=row[1],
            id=row[0]
        )

        required_items.append(required_item)

    return required_items