from services.database import (
    create_supplies_table,
    create_school_lists_table,
    create_required_items_table
)

# Make sure tables exist
create_supplies_table()
create_school_lists_table()
create_required_items_table()
