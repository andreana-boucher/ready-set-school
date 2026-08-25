from services.database import (
    create_supplies_table,
    create_school_lists_table,
    create_required_items_table,
    create_shopping_list_table
)

def main():
    # Make sure tables exist
    create_supplies_table()
    create_school_lists_table()
    create_required_items_table()
    create_shopping_list_table()


# ------------TESTING-------------#











if __name__ == "__main__":
    main()


