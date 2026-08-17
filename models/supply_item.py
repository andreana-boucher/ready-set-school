# build small SupplyItem class
# need id, name, quantity, condition, notes

class SupplyItem:
    VALID_CONDITIONS = ['New', 'Good', 'Fair', 'Poor']
    def __init__(
            self, 
            name: str, # basic type - pencil, glue stick, binder, etc.
            quantity: int, # how many already owned
            condition: str, # new, good, fair, poor
            colour: str ="", 
            specification: str ="", # 3 pring, HB #2, fine tip, etc. 
            notes: str ="", # household info - package already opened, Jackson's name is on, etc.
            id: int | None = None
            ) -> None:
        
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.colour = colour
        self.specification = specification
        self.notes = notes
        self.id = id

        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        
        if not name.strip():
            raise ValueError('Name cannot be empty.')

        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer.')

        if quantity < 0:
            raise ValueError('Quantity cannot be negative.')

        if condition not in self.VALID_CONDITIONS:
            raise ValueError(
                'Condition must be New, Good, Fair, or Poor.'
            )
        


