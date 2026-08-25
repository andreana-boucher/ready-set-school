import customtkinter as ctk

from ui.inventory_screen import InventoryScreen
from ui.school_list_screen import SchoolListScreen
from ui.shopping_list_screen import ShoppingListScreen


class ReadySetSchoolApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ready, Set, School!")
        self.geometry("1000x650")

        # Main layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -----------------------------
        # NAVIGATION SIDEBAR
        # -----------------------------

        self.sidebar = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=0
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_rowconfigure(5, weight=1)

        app_title = ctk.CTkLabel(
            self.sidebar,
            text="Ready, Set,\nSchool!",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        )
        app_title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 25)
        )

        home_button = ctk.CTkButton(
            self.sidebar,
            text="Home",
            command=self.show_home
        )
        home_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=10
        )

        inventory_button = ctk.CTkButton(
            self.sidebar,
            text="Inventory",
            command=self.show_inventory
        )
        inventory_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=10
        )

        school_lists_button = ctk.CTkButton(
            self.sidebar,
            text="School Lists",
            command=self.show_school_lists
        )
        school_lists_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=10
        )

        shopping_list_button = ctk.CTkButton(
            self.sidebar,
            text="Shopping List",
            command=self.show_shopping_list
        )
        shopping_list_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=10
        )

        # -----------------------------
        # CONTENT AREA
        # -----------------------------

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.show_home()


    # -----------------------------
    # SCREEN NAVIGATION
    # -----------------------------

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    def show_home(self):
        self.clear_content()

        title = ctk.CTkLabel(
            self.content_frame,
            text="Ready, Set, School!",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )
        title.pack(pady=(40, 5))

        tagline = ctk.CTkLabel(
            self.content_frame,
            text="Skip the Scramble.",
            font=ctk.CTkFont(size=16)
        )
        tagline.pack()


    def show_inventory(self):
        self.clear_content()

        inventory_screen = InventoryScreen(
            self.content_frame
        )
        inventory_screen.pack(
            fill="both",
            expand=True
        )


    def show_school_lists(self):
        self.clear_content()

        school_list_screen = SchoolListScreen(
            self.content_frame
        )
        school_list_screen.pack(
            fill="both",
            expand=True
        )


    def show_shopping_list(self):
        self.clear_content()

        shopping_list_screen = ShoppingListScreen(
            self.content_frame
        )
        shopping_list_screen.pack(
            fill="both",
            expand=True
        )