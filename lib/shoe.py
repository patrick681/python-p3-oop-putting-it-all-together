class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Default condition for new shoes

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):  # Update the condition to 'New' after repair
        self.condition = "New"  # Set condition back to 'New' after cobbling
        print("Your shoe is as good as new!")
