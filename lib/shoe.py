#!/usr/bin/env python3

class Shoe:
    def _init_(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  # Use the property setter for validation
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"