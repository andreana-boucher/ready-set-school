class RequiredItem:
    def __init__(
        self,
        name: str,
        quantity_required: int,
        colour: str = "",
        specification: str = "",
        notes: str = ""
    ) -> None:
        
        self.name = name
        self.quantity_required = quantity_required
        self.colour = colour
        self.specification = specification
        self.notes = notes