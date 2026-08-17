from models.supply_item import SupplyItem
from services.database import (
    add_supply,
    get_all_supplies,
    update_supply,
    delete_supply
)

### CREATE SUPPLY ITEM
def create_supply(
    name: str,
    quantity: int,
    condition: str,
    colour: str = "",
    specification: str = "",
    notes: str = ""
) -> None:
    supply = SupplyItem(
        name=name,
        quantity=quantity,
        condition=condition,
        colour=colour,
        specification=specification,
        notes=notes
    )

    add_supply(supply)

### VIEW INVENTORY
def view_inventory():
    return get_all_supplies()

### HELPER - GET SUPPLY BY ID
def get_supply_by_id(supply_id: int):
    supplies = get_all_supplies()

    for supply in supplies:
        if supply.id == supply_id:
            return supply

    return None

### EDIT SUPPLY
def edit_supply(
    supply: SupplyItem,
    name: str,
    quantity: int,
    condition: str,
    colour: str = "",
    specification: str = "",
    notes: str = ""
) -> None:
    supply.name = name
    supply.quantity = quantity
    supply.condition = condition
    supply.colour = colour
    supply.specification = specification
    supply.notes = notes

    update_supply(supply)

### DELETE SUPPLY
def remove_supply(supply: SupplyItem) -> None:
    delete_supply(supply.id)