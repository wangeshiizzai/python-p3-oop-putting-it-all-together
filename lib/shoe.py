class Shoe:
    def __init__(self, brand, size, color="White"):
        self.brand = brand
        self.size = size
        self.color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value.strip():
            self._brand = value
        else:
            raise ValueError("Brand must be a non-empty string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.strip():
            self._color = value
        else:
            raise ValueError("Color must be a non-empty string.")

    def cobble(self):
        print("Your shoe has been repaired.")
