from models.supply_item import SupplyItem
from models.required_item import RequiredItem
from services.database import (create_supplies_table, get_all_supplies, update_supply, delete_supply)

create_supplies_table()
supplies = get_all_supplies()
# print(supplies)

for supply in supplies:
    print(
        supply.id,
        supply.name,
        supply.quantity,
        supply.condition,
        supply.colour,
        supply.specification,
        supply.notes
    )


# if supplies:
#     supply_to_delete = supplies[0]

#     delete_supply(supply_to_delete.id)

#     print("Supply deleted successfully.")

