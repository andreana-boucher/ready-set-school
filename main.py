from services.database import (
    create_supplies_table,
    create_school_lists_table,
    create_required_items_table,
    create_shopping_list_table
)

from ui.main_window import ReadySetSchoolApp
from ui.inventory_screen import InventoryScreen
from ui.school_list_screen import SchoolListScreen


def main():
    # Make sure tables exist
    create_supplies_table()
    create_school_lists_table()
    create_required_items_table()
    create_shopping_list_table()

    app = ReadySetSchoolApp()
    app.mainloop()


# ------------TESTING-------------#

if __name__ == "__main__":
    main()


