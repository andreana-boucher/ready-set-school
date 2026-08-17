from services.inventory_manager import (
    create_supply,
    view_inventory,
    edit_supply,
    remove_supply,
    get_supply_by_id
)
from services.database import (
    create_supplies_table,
    create_school_lists_table,
    create_required_items_table
)

from services.school_list_manager import (
    create_school_list,
    view_school_lists,
    edit_school_list,
    remove_school_list,
    create_required_item,
    view_required_items,
    edit_required_item,
    remove_required_item
)


def main():
    # Make sure tables exist
    create_supplies_table()
    create_school_lists_table()
    create_required_items_table()



#--------------------------------#

if __name__ == "__main__":
    main()




