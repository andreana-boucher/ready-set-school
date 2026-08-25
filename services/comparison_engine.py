from models.supply_item import SupplyItem
from models.required_item import RequiredItem

### NORMALIZE TEXT - HELPER FUNCTION
# Standardizes text before comparing values.

def normalize_text(value: str) -> str:
    return value.strip().lower()

### MATCH SUPPLY TO REQUIREMENT
# Checks whether an owned supply matches a required school supply.

def items_match(
    supply: SupplyItem,
    required_item: RequiredItem
) -> bool:

    if normalize_text(supply.name) != normalize_text(required_item.name):
        return False

    if required_item.colour:
        if normalize_text(supply.colour) != normalize_text(required_item.colour):
            return False

    if required_item.specification:
        if normalize_text(supply.specification) != normalize_text(
            required_item.specification
        ):
            return False

    return True


### COUNT MATCHING INVENTORY
# Adds up the quantities of usable inventory items that match a requirement.

def get_matching_quantity(
    supplies: list[SupplyItem],
    required_item: RequiredItem
) -> int:
    total_quantity = 0

    for supply in supplies:
        if supply.condition == "Poor":
            continue

        if items_match(supply, required_item):
            total_quantity += supply.quantity

    return total_quantity


### CALCULATE MISSING QUANTITY
# Calculates how many of a required item still need to be purchased.

def get_missing_quantity(
    supplies: list[SupplyItem],
    required_item: RequiredItem
) -> int:
    matching_quantity = get_matching_quantity(
        supplies,
        required_item
    )

    missing_quantity = (
        required_item.quantity_required - matching_quantity
    )

    return max(0, missing_quantity)



### GENERATE SHOPPING LIST
# Creates a list of required items that still need to be purchased.

def generate_shopping_list(
    supplies: list[SupplyItem],
    required_items: list[RequiredItem]
) -> list[dict]:
    shopping_list = []

    for required_item in required_items:
        missing_quantity = get_missing_quantity(
            supplies,
            required_item
        )

        if missing_quantity > 0:
            shopping_list.append({
                "name": required_item.name,
                "quantity": missing_quantity,
                "colour": required_item.colour,
                "specification": required_item.specification,
                "notes": required_item.notes
            })

    return shopping_list

