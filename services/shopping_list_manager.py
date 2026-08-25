from models.shopping_item import ShoppingItem
from services.comparison_engine import generate_shopping_list
from services.inventory_manager import view_inventory
from services.school_list_manager import view_required_items
from services.database import (
    add_shopping_item,
    get_shopping_items_by_school_list,
    update_shopping_item,
    delete_shopping_item,
    delete_shopping_items_by_school_list
)



### VIEW SHOPPING LIST
# Retrieves all shopping items linked to a school list.

def view_shopping_list(school_list_id: int):
    return get_shopping_items_by_school_list(school_list_id)


### MARK ITEM AS PURCHASED
# Marks a shopping item as purchased and saves the change.

def mark_item_as_purchased(shopping_item: ShoppingItem) -> None:
    shopping_item.purchased = True
    update_shopping_item(shopping_item)


### MARK ITEM AS NOT PURCHASED
# Marks a shopping item as not purchased and saves the change.

def mark_item_as_not_purchased(shopping_item: ShoppingItem) -> None:
    shopping_item.purchased = False
    update_shopping_item(shopping_item)


### REMOVE SHOPPING ITEM
# Removes a shopping item from the shopping list.

def remove_shopping_item(shopping_item: ShoppingItem) -> None:
    delete_shopping_item(shopping_item.id)


### GENERATE AND SAVE SHOPPING LIST
# Compares required items with inventory and saves missing items.

def generate_and_save_shopping_list(school_list_id: int) -> None:
    supplies = view_inventory()
    required_items = view_required_items(school_list_id)

    generated_items = generate_shopping_list(
        supplies,
        required_items
    )

    delete_shopping_items_by_school_list(school_list_id)

    for item in generated_items:
        shopping_item = ShoppingItem(
            school_list_id=school_list_id,
            name=item["name"],
            quantity=item["quantity"],
            colour=item["colour"],
            specification=item["specification"],
            notes=item["notes"],
            purchased=False
        )

        add_shopping_item(shopping_item)


### PREPARE SHOPPING LIST FOR EXPORT
# Converts shopping items into clean data for printing or export.

def prepare_shopping_list_for_export(school_list_id: int):
    shopping_items = view_shopping_list(school_list_id)

    export_data = []

    for item in shopping_items:
        export_data.append({
            "name": item.name,
            "quantity": item.quantity,
            "colour": item.colour,
            "specification": item.specification,
            "notes": item.notes,
            "purchased": item.purchased
        })

    return export_data