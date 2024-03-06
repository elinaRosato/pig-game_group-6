class Player:
    
    def __init__(self, name, is_computer=False):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        else:
            self.name = name
             
        if not isinstance(is_computer, bool):
            raise TypeError("Is computer must be a boolean.")
        else:
            self.is_computer = is_computer
