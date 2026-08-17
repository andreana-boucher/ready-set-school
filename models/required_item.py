class RequiredItem:
    def __init__(
        self,
        name: str,
        quantity_required: int,
        colour: str = "",
        specification: str = "",
        notes: str = "",
        school_list_id: int | None = None,
        id: int | None = None
    ) -> None:
        self.name = name
        self.quantity_required = quantity_required
        self.colour = colour
        self.specification = specification
        self.notes = notes
        self.school_list_id = school_list_id
        self.id = id