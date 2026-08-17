from models.school_supply_list import SchoolSupplyList
from models.required_item import RequiredItem
from services.database import (
    add_school_list,
    get_all_school_lists,
    update_school_list,
    delete_school_list,
    add_required_item,
    get_required_items_by_school_list,
    update_required_item,
    delete_required_item
)

### CREATE A SCHOOL LIST
# Creates a SchoolSupplyList object and saves it to the database.

def create_school_list(
    school_name: str,
    grade: str,
    school_year: str,
    student_name: str = ""
) -> None:
    school_list = SchoolSupplyList(
        school_name=school_name,
        grade=grade,
        school_year=school_year,
        student_name=student_name
    )

    add_school_list(school_list)


### VIEW SCHOOL LISTS
# Retrieves and returns all saved school lists from the database.

def view_school_lists():
    return get_all_school_lists()


### EDIT A SCHOOL LIST
# Updates the details of an existing school list.

def edit_school_list(
    school_list: SchoolSupplyList,
    school_name: str,
    grade: str,
    school_year: str,
    student_name: str = ""
) -> None:
    school_list.school_name = school_name
    school_list.grade = grade
    school_list.school_year = school_year
    school_list.student_name = student_name

    update_school_list(school_list)


### DELETE A SCHOOL LIST
# Removes an existing school list from the database.

def remove_school_list(school_list: SchoolSupplyList) -> None:
    delete_school_list(school_list.id)


### ADD A REQUIRED ITEM
# Creates a RequiredItem object, links it to a school list, and saves it.

def create_required_item(
    school_list_id: int,
    name: str,
    quantity_required: int,
    colour: str = "",
    specification: str = "",
    notes: str = ""
) -> None:
    required_item = RequiredItem(
        name=name,
        quantity_required=quantity_required,
        colour=colour,
        specification=specification,
        notes=notes,
        school_list_id=school_list_id
    )

    add_required_item(required_item)

### VIEW REQUIRED ITEMS
# Retrieves all required items linked to a specific school list.

def view_required_items(school_list_id: int):
    return get_required_items_by_school_list(school_list_id)


### EDIT A REQUIRED ITEM
# Updates an existing required item linked to a school list.

def edit_required_item(
    required_item: RequiredItem,
    name: str,
    quantity_required: int,
    colour: str = "",
    specification: str = "",
    notes: str = ""
) -> None:
    required_item.name = name
    required_item.quantity_required = quantity_required
    required_item.colour = colour
    required_item.specification = specification
    required_item.notes = notes

    update_required_item(required_item)
    

### DELETE A REQUIRED ITEM
# Removes an existing required item from its school list.

def remove_required_item(required_item: RequiredItem) -> None:
    delete_required_item(required_item.id)