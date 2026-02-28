class Coffee:
    def __init__(self, size, price):
        self._size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        allowed_sizes = ["Small", "Medium", "Large"]
        if value not in allowed_sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1.0