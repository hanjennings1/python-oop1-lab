#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size  # goes through the setter below for validation
        self.price = price

    def get_size(self):
        # returns the hidden/stored value
        return self._size

    def set_size(self, value):
        # only allow size to be set to one of the three valid options
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # wires get_size/set_size together so size behaves like 
    # a normal attribute but runs validation on assignment
    size = property(get_size, set_size)

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1  # tipping adds $1 to the price