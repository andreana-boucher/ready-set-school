import customtkinter as ctk

from services.school_list_manager import (
    view_school_lists
)

from services.shopping_list_manager import (
    view_shopping_list,
    mark_item_as_purchased,
    mark_item_as_not_purchased,
    remove_shopping_item
)


class ShoppingListScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # -----------------------------
        # SHOPPING LIST HEADER
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
            text="Shopping List",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )
        title.pack(side="left")

        # -----------------------------
        # SCHOOL LIST SELECTION
        # -----------------------------

        selection_frame = ctk.CTkFrame(
            self
        )
        selection_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        selection_label = ctk.CTkLabel(
            selection_frame,
            text="School List:"
        )
        selection_label.pack(
            side="left",
            padx=(15, 10),
            pady=15
        )

        self.school_lists = view_school_lists()

        school_list_names = []

        for school_list in self.school_lists:
            display_name = self.get_school_list_display_name(
                school_list
            )

            school_list_names.append(
                display_name
            )

        if school_list_names:
            self.school_list_dropdown = ctk.CTkComboBox(
                selection_frame,
                values=school_list_names,
                width=450
            )

            self.school_list_dropdown.set(
                school_list_names[0]
            )

        else:
            self.school_list_dropdown = ctk.CTkComboBox(
                selection_frame,
                values=["No school lists available"],
                width=450
            )

            self.school_list_dropdown.set(
                "No school lists available"
            )

        self.school_list_dropdown.pack(
            side="left",
            padx=10,
            pady=15
        )

        load_button = ctk.CTkButton(
            selection_frame,
            text="Load",
            command=self.load_selected_shopping_list
        )
        load_button.pack(
            side="left",
            padx=10,
            pady=15
        )

        # -----------------------------
        # SHOPPING ITEMS DISPLAY
        # -----------------------------

        self.shopping_items_frame = ctk.CTkScrollableFrame(
            self
        )
        self.shopping_items_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )


    ### GET SCHOOL LIST DISPLAY NAME
    # Creates the text shown in the school-list dropdown.

    def get_school_list_display_name(
        self,
        school_list
    ):
        display_name = (
            f"{school_list.school_name} | "
            f"{school_list.grade} | "
            f"{school_list.school_year}"
        )

        if school_list.student_name:
            display_name += (
                f" | {school_list.student_name}"
            )

        return display_name


    ### GET SELECTED SCHOOL LIST
    # Finds the SchoolSupplyList object selected in the dropdown.

    def get_selected_school_list(self):
        if not self.school_lists:
            return None

        selected_name = (
            self.school_list_dropdown.get()
        )

        for school_list in self.school_lists:
            display_name = (
                self.get_school_list_display_name(
                    school_list
                )
            )

            if display_name == selected_name:
                return school_list

        return None


    ### LOAD SELECTED SHOPPING LIST
    # Loads shopping items for the selected school list.

    def load_selected_shopping_list(self):
        for widget in (
            self.shopping_items_frame.winfo_children()
        ):
            widget.destroy()

        selected_school_list = (
            self.get_selected_school_list()
        )

        if selected_school_list is None:
            return

        shopping_items = view_shopping_list(
            selected_school_list.id
        )

        for item in shopping_items:
            item_text = (
                f"{item.name}  |  "
                f"Quantity: {item.quantity}"
            )

            details = []

            if item.colour:
                details.append(
                    f"Colour: {item.colour}"
                )

            if item.specification:
                details.append(
                    f"Specification: "
                    f"{item.specification}"
                )

            if details:
                item_text += (
                    "\n" +
                    "  |  ".join(details)
                )

            # Container for one shopping item
            item_row = ctk.CTkFrame(
                self.shopping_items_frame
            )
            item_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            # Shopping item information
            item_label = ctk.CTkLabel(
                item_row,
                text=item_text,
                anchor="w",
                justify="left"
            )
            item_label.pack(
                side="left",
                fill="x",
                expand=True,
                padx=10,
                pady=8
            )

            # Purchased status button
            status_text = (
                "Undo Purchased"
                if item.purchased
                else "Mark Purchased"
            )

            status_button = ctk.CTkButton(
                item_row,
                text=status_text,
                width=130,
                command=lambda i=item:
                self.toggle_purchased_status(i)
            )
            status_button.pack(
                side="right",
                padx=5,
                pady=8
            )

            # Delete button
            delete_button = ctk.CTkButton(
                item_row,
                text="Delete",
                width=70,
                command=lambda i=item:
                self.delete_shopping_item_gui(i)
            )
            delete_button.pack(
                side="right",
                padx=(5, 10),
                pady=8
            )


    ### TOGGLE PURCHASED STATUS
    # Marks an item as purchased or not purchased.

    def toggle_purchased_status(
        self,
        shopping_item
    ):
        if shopping_item.purchased:
            mark_item_as_not_purchased(
                shopping_item
            )

        else:
            mark_item_as_purchased(
                shopping_item
            )

        self.load_selected_shopping_list()


    ### DELETE SHOPPING ITEM
    # Removes an item from the shopping list.

    def delete_shopping_item_gui(
        self,
        shopping_item
    ):
        remove_shopping_item(
            shopping_item
        )

        self.load_selected_shopping_list()