import customtkinter as ctk

from services.inventory_manager import (
    create_supply,
    view_inventory,
    edit_supply,
    remove_supply
)


class InventoryScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # -----------------------------
        # INVENTORY HEADER
        # -----------------------------

        header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        header_frame.pack(
            fill="x",
            padx=20,
            pady=(30, 20)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="Inventory",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )
        title.pack(side="left")

        add_button = ctk.CTkButton(
            header_frame,
            text="Add Supply",
            command=self.show_add_supply_form
        )
        add_button.pack(
            side="right",
            padx=(10, 0)
        )

        export_button = ctk.CTkButton(
            header_frame,
            text="Export",
            command=self.export_inventory
        )
        export_button.pack(side="right")

        # -----------------------------
        # INVENTORY LIST
        # -----------------------------

        self.inventory_frame = ctk.CTkScrollableFrame(self)
        self.inventory_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.load_inventory()


    ### LOAD INVENTORY
    # Retrieves saved supplies and displays them on the inventory screen.

    def load_inventory(self):
        supplies = view_inventory()

        for supply in supplies:
            supply_text = (
                f"{supply.name}  |  "
                f"Quantity: {supply.quantity}  |  "
                f"Condition: {supply.condition}"
            )

            details = []

            if supply.colour:
                details.append(
                    f"Colour: {supply.colour}"
                )

            if supply.specification:
                details.append(
                    f"Specification: {supply.specification}"
                )

            if details:
                supply_text += "\n" + "  |  ".join(details)

            # Container for one inventory item
            supply_row = ctk.CTkFrame(
                self.inventory_frame
            )
            supply_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            # Supply information
            supply_label = ctk.CTkLabel(
                supply_row,
                text=supply_text,
                anchor="w",
                justify="left"
            )
            supply_label.pack(
                side="left",
                fill="x",
                expand=True,
                padx=10,
                pady=8
            )

            # Delete button
            delete_button = ctk.CTkButton(
                supply_row,
                text="Delete",
                width=70,
                command=lambda s=supply:
                self.delete_supply_item(s)
            )
            delete_button.pack(
                side="right",
                padx=(5, 10),
                pady=8
            )

            # Edit button
            edit_button = ctk.CTkButton(
                supply_row,
                text="Edit",
                width=70,
                command=lambda s=supply:
                self.show_edit_supply_form(s)
            )
            edit_button.pack(
                side="right",
                padx=5,
                pady=8
            )


    ### REFRESH INVENTORY
    # Clears and reloads the inventory display.

    def refresh_inventory(self):
        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        self.load_inventory()


    ### SHOW ADD SUPPLY FORM
    # Opens the form used to add a new supply.

    def show_add_supply_form(self):
        form_window = ctk.CTkToplevel(self)

        form_window.title("Add Supply")
        form_window.geometry("450x550")

        form_window.transient(self.winfo_toplevel())
        form_window.grab_set()
        form_window.focus()

        title = ctk.CTkLabel(
            form_window,
            text="Add Supply",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 20)
        )

        # Name
        name_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Supply Name"
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Quantity
        quantity_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Quantity"
        )
        quantity_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Condition
        condition_dropdown = ctk.CTkComboBox(
            form_window,
            values=[
                "New",
                "Good",
                "Fair",
                "Poor"
            ]
        )
        condition_dropdown.set("Good")
        condition_dropdown.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Colour
        colour_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Colour (optional)"
        )
        colour_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Specification
        specification_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Specification (optional)"
        )
        specification_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Notes
        notes_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Notes (optional)"
        )
        notes_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        ### SAVE SUPPLY
        # Validates the form and saves the new supply.

        def save_supply():
            name = name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            condition = condition_dropdown.get()
            colour = colour_entry.get().strip()
            specification = (
                specification_entry.get().strip()
            )
            notes = notes_entry.get().strip()

            if not name:
                print("Supply name is required.")
                return

            if not quantity.isdigit():
                print("Quantity must be a number.")
                return

            create_supply(
                name=name,
                quantity=int(quantity),
                condition=condition,
                colour=colour,
                specification=specification,
                notes=notes
            )

            self.refresh_inventory()
            form_window.destroy()

        # Save button
        save_button = ctk.CTkButton(
            form_window,
            text="Save Supply",
            command=save_supply
        )
        save_button.pack(
            fill="x",
            padx=30,
            pady=(20, 8)
        )


    ### SHOW EDIT SUPPLY FORM
    # Opens a form with the selected supply's current information.

    def show_edit_supply_form(self, supply):
        form_window = ctk.CTkToplevel(self)

        form_window.title("Edit Supply")
        form_window.geometry("450x550")

        form_window.transient(self.winfo_toplevel())
        form_window.grab_set()
        form_window.focus()

        title = ctk.CTkLabel(
            form_window,
            text="Edit Supply",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 20)
        )

        # Name
        name_entry = ctk.CTkEntry(
            form_window
        )
        name_entry.insert(
            0,
            supply.name
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Quantity
        quantity_entry = ctk.CTkEntry(
            form_window
        )
        quantity_entry.insert(
            0,
            str(supply.quantity)
        )
        quantity_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Condition
        condition_dropdown = ctk.CTkComboBox(
            form_window,
            values=[
                "New",
                "Good",
                "Fair",
                "Poor"
            ]
        )
        condition_dropdown.set(
            supply.condition
        )
        condition_dropdown.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Colour
        colour_entry = ctk.CTkEntry(
            form_window
        )
        colour_entry.insert(
            0,
            supply.colour
        )
        colour_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Specification
        specification_entry = ctk.CTkEntry(
            form_window
        )
        specification_entry.insert(
            0,
            supply.specification
        )
        specification_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        # Notes
        notes_entry = ctk.CTkEntry(
            form_window
        )
        notes_entry.insert(
            0,
            supply.notes
        )
        notes_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        ### SAVE UPDATED SUPPLY
        # Validates and saves the edited supply.

        def save_changes():
            name = name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            condition = condition_dropdown.get()
            colour = colour_entry.get().strip()
            specification = (
                specification_entry.get().strip()
            )
            notes = notes_entry.get().strip()

            if not name:
                print("Supply name is required.")
                return

            if not quantity.isdigit():
                print("Quantity must be a number.")
                return

            edit_supply(
                supply=supply,
                name=name,
                quantity=int(quantity),
                condition=condition,
                colour=colour,
                specification=specification,
                notes=notes
            )

            self.refresh_inventory()
            form_window.destroy()

        # Update button
        update_button = ctk.CTkButton(
            form_window,
            text="Update Supply",
            command=save_changes
        )
        update_button.pack(
            fill="x",
            padx=30,
            pady=(20, 8)
        )


    ### DELETE SUPPLY
    # Removes the selected supply from inventory.

    def delete_supply_item(self, supply):
        remove_supply(supply)
        self.refresh_inventory()


    ### EXPORT INVENTORY
    # Placeholder for future inventory export.

    def export_inventory(self):
        print("Export clicked")