class ShoppingItem:
    def __init__(
        self,
        school_list_id: int,
        name: str,
        quantity: int,
        colour: str = "",
        specification: str = "",
        notes: str = "",
        purchased: bool = False,
        id: int | None = None
    ) -> None:
        self.school_list_id = school_list_id
        self.name = name
        self.quantity = quantity
        self.colour = colour
        self.specification = specification
        self.notes = notes
        self.purchased = purchased
        self.id = id