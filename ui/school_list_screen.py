import customtkinter as ctk

from services.school_list_manager import (
    create_school_list,
    view_school_lists,
    create_required_item,
    view_required_items,
    edit_required_item,
    remove_required_item,
    remove_school_list
)

from services.shopping_list_manager import (
    generate_and_save_shopping_list
)


class SchoolListScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # -----------------------------
        # SCHOOL LIST HEADER
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
            text="School Lists",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )
        title.pack(side="left")

        add_button = ctk.CTkButton(
            header_frame,
            text="Add School List",
            command=self.show_add_school_list_form
        )
        add_button.pack(side="right")

        # -----------------------------
        # SCHOOL LIST DISPLAY
        # -----------------------------

        self.school_lists_frame = ctk.CTkScrollableFrame(self)
        self.school_lists_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.load_school_lists()


    ### LOAD SCHOOL LISTS
    # Retrieves saved school lists and displays them.

    def load_school_lists(self):
        school_lists = view_school_lists()

        for school_list in school_lists:
            list_text = (
                f"{school_list.school_name}  |  "
                f"{school_list.grade}  |  "
                f"{school_list.school_year}"
            )

            if school_list.student_name:
                list_text += (
                    f"  |  Student: "
                    f"{school_list.student_name}"
                )

            # Container for one school list
            list_row = ctk.CTkFrame(
                self.school_lists_frame
            )
            list_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            # School list information
            list_label = ctk.CTkLabel(
                list_row,
                text=list_text,
                anchor="w"
            )
            list_label.pack(
                side="left",
                fill="x",
                expand=True,
                padx=10,
                pady=8
            )

            # Open button
            open_button = ctk.CTkButton(
                list_row,
                text="Open",
                width=70,
                command=lambda s=school_list:
                self.show_required_items(s)
            )
            open_button.pack(
                side="right",
                padx=(5, 10),
                pady=8
            )

            # Delete button
            delete_button = ctk.CTkButton(
                list_row,
                text="Delete",
                width=70,
                command=lambda s=school_list:
                self.delete_school_list_gui(s)
            )
            delete_button.pack(
                side="right",
                padx=5,
                pady=8
            )


    ### SHOW REQUIRED ITEMS
    # Opens a window showing required items for the selected school list.

    def show_required_items(self, school_list):
        required_window = ctk.CTkToplevel(self)

        required_window.title("Required Items")
        required_window.geometry("700x550")

        required_window.transient(self.winfo_toplevel())
        required_window.grab_set()
        required_window.focus()

        title = ctk.CTkLabel(
            required_window,
            text=school_list.school_name,
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            required_window,
            text=(
                f"{school_list.grade} | "
                f"{school_list.school_year}"
            )
        )
        subtitle.pack(
            pady=(0, 20)
        )

        # Add Required Item button
        add_item_button = ctk.CTkButton(
            required_window,
            text="Add Required Item",
            command=lambda: self.show_add_required_item_form(
                school_list,
                required_window
            )
        )
        add_item_button.pack(
            pady=(0, 15)
        )

        # Generate Shopping List button
        generate_button = ctk.CTkButton(
            required_window,
            text="Generate Shopping List",
            command=lambda: self.generate_shopping_list_for_school(
                school_list
            )
        )
        generate_button.pack(
            pady=(0, 15)
        )

        # -----------------------------
        # REQUIRED ITEMS DISPLAY
        # -----------------------------

        items_frame = ctk.CTkScrollableFrame(
            required_window
        )
        items_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        required_items = view_required_items(
            school_list.id
        )

        for item in required_items:
            item_text = (
                f"{item.name}  |  "
                f"Quantity: {item.quantity_required}"
            )

            if item.colour:
                item_text += (
                    f"  |  Colour: {item.colour}"
                )

            if item.specification:
                item_text += (
                    f"  |  Specification: "
                    f"{item.specification}"
                )

            item_row = ctk.CTkFrame(
                items_frame
            )
            item_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            item_label = ctk.CTkLabel(
                item_row,
                text=item_text,
                anchor="w"
            )
            item_label.pack(
                side="left",
                fill="x",
                expand=True,
                padx=10,
                pady=8
            )

            # Edit button
            edit_button = ctk.CTkButton(
                item_row,
                text="Edit",
                width=70,
                command=lambda i=item:
                self.show_edit_required_item_form(
                    school_list,
                    i,
                    required_window
                )
            )
            edit_button.pack(
                side="right",
                padx=(5, 10),
                pady=8
            )

            # Delete button
            delete_button = ctk.CTkButton(
                item_row,
                text="Delete",
                width=70,
                command=lambda i=item:
                self.delete_required_item_gui(
                    school_list,
                    i,
                    required_window
                )
            )
            delete_button.pack(
                side="right",
                padx=5,
                pady=8
            )


    ### SHOW ADD REQUIRED ITEM FORM
    # Opens a form used to add a required item.

    def show_add_required_item_form(
        self,
        school_list,
        required_window
    ):
        form_window = ctk.CTkToplevel(self)

        form_window.title("Add Required Item")
        form_window.geometry("450x550")

        form_window.transient(required_window)
        form_window.grab_set()
        form_window.focus()

        title = ctk.CTkLabel(
            form_window,
            text="Add Required Item",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 20)
        )

        name_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Item Name"
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        quantity_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Quantity Required"
        )
        quantity_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        colour_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Colour (optional)"
        )
        colour_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        specification_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Specification (optional)"
        )
        specification_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        notes_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Notes (optional)"
        )
        notes_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        def save_required_item():
            name = name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            colour = colour_entry.get().strip()
            specification = specification_entry.get().strip()
            notes = notes_entry.get().strip()

            if not name:
                print("Item name is required.")
                return

            if not quantity.isdigit():
                print("Quantity must be a number.")
                return

            if int(quantity) <= 0:
                print("Quantity must be greater than zero.")
                return

            # Split comma-separated colours into individual colours
            colours = [
                value.strip()
                for value in colour.split(",")
                if value.strip()
            ]

            # If no colour was entered, create one item with no colour
            if not colours:
                colours = [""]

            # Create one required item for each colour
            for item_colour in colours:
                create_required_item(
                    school_list_id=school_list.id,
                    name=name,
                    quantity_required=int(quantity),
                    colour=item_colour,
                    specification=specification,
                    notes=notes
                )

            form_window.destroy()
            required_window.destroy()

            self.show_required_items(
                school_list
            )

        save_button = ctk.CTkButton(
            form_window,
            text="Save Required Item",
            command=save_required_item
        )
        save_button.pack(
            fill="x",
            padx=30,
            pady=(20, 8)
        )


    ### SHOW EDIT REQUIRED ITEM FORM
    # Opens a form containing the selected item's current values.

    def show_edit_required_item_form(
        self,
        school_list,
        required_item,
        required_window
    ):
        form_window = ctk.CTkToplevel(self)

        form_window.title("Edit Required Item")
        form_window.geometry("450x550")

        form_window.transient(required_window)
        form_window.grab_set()
        form_window.focus()

        title = ctk.CTkLabel(
            form_window,
            text="Edit Required Item",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 20)
        )

        name_entry = ctk.CTkEntry(
            form_window
        )
        name_entry.insert(
            0,
            required_item.name
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        quantity_entry = ctk.CTkEntry(
            form_window
        )
        quantity_entry.insert(
            0,
            str(required_item.quantity_required)
        )
        quantity_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        colour_entry = ctk.CTkEntry(
            form_window
        )
        colour_entry.insert(
            0,
            required_item.colour
        )
        colour_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        specification_entry = ctk.CTkEntry(
            form_window
        )
        specification_entry.insert(
            0,
            required_item.specification
        )
        specification_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        notes_entry = ctk.CTkEntry(
            form_window
        )
        notes_entry.insert(
            0,
            required_item.notes
        )
        notes_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        def save_changes():
            name = name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            colour = colour_entry.get().strip()
            specification = specification_entry.get().strip()
            notes = notes_entry.get().strip()

            if not name:
                print("Item name is required.")
                return

            if not quantity.isdigit():
                print("Quantity must be a number.")
                return

            if int(quantity) <= 0:
                print("Quantity must be greater than zero.")
                return

            edit_required_item(
                required_item=required_item,
                name=name,
                quantity_required=int(quantity),
                colour=colour,
                specification=specification,
                notes=notes
            )

            form_window.destroy()
            required_window.destroy()

            self.show_required_items(
                school_list
            )

        update_button = ctk.CTkButton(
            form_window,
            text="Update Required Item",
            command=save_changes
        )
        update_button.pack(
            fill="x",
            padx=30,
            pady=(20, 8)
        )


    ### DELETE REQUIRED ITEM
    # Removes a required item and refreshes the window.

    def delete_required_item_gui(
        self,
        school_list,
        required_item,
        required_window
    ):
        remove_required_item(
            required_item
        )

        required_window.destroy()

        self.show_required_items(
            school_list
        )


    ### DELETE SCHOOL LIST
    # Removes a school list and refreshes the display.

    def delete_school_list_gui(
        self,
        school_list
    ):
        remove_school_list(
            school_list
        )

        self.refresh_school_lists()


    ### GENERATE SHOPPING LIST
    # Compares inventory with requirements and saves shortages.

    def generate_shopping_list_for_school(
        self,
        school_list
    ):
        generate_and_save_shopping_list(
            school_list.id
        )

        print("Shopping list generated successfully.")


    ### REFRESH SCHOOL LISTS
    # Clears and reloads the school list display.

    def refresh_school_lists(self):
        for widget in self.school_lists_frame.winfo_children():
            widget.destroy()

        self.load_school_lists()


    ### SHOW ADD SCHOOL LIST FORM
    # Opens a form used to create a new school list.

    def show_add_school_list_form(self):
        form_window = ctk.CTkToplevel(self)

        form_window.title("Add School List")
        form_window.geometry("450x500")

        form_window.transient(self.winfo_toplevel())
        form_window.grab_set()
        form_window.focus()

        title = ctk.CTkLabel(
            form_window,
            text="Add School List",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(25, 20)
        )

        school_name_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="School Name"
        )
        school_name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        grade_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Grade"
        )
        grade_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        school_year_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="School Year"
        )
        school_year_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        student_name_entry = ctk.CTkEntry(
            form_window,
            placeholder_text="Student Name (optional)"
        )
        student_name_entry.pack(
            fill="x",
            padx=30,
            pady=8
        )

        def save_school_list():
            school_name = school_name_entry.get().strip()
            grade = grade_entry.get().strip()
            school_year = school_year_entry.get().strip()
            student_name = student_name_entry.get().strip()

            if not school_name:
                print("School name is required.")
                return

            if not grade:
                print("Grade is required.")
                return

            if not school_year:
                print("School year is required.")
                return

            create_school_list(
                school_name=school_name,
                grade=grade,
                school_year=school_year,
                student_name=student_name
            )

            self.refresh_school_lists()
            form_window.destroy()

        save_button = ctk.CTkButton(
            form_window,
            text="Save School List",
            command=save_school_list
        )
        save_button.pack(
            fill="x",
            padx=30,
            pady=(20, 8)
        )