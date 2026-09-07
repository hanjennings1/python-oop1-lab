#!/usr/bin/env python3

class Book:
    def __init__ (self, title, page_count):
        self.title = title
        self.page_count = page_count         # goes through the setter below for validation
        self.current_page = 1  # tracks reading progress, starts on page 1
    
    def get_page_count(self):
         # returns the hidden/stored value
        return self._page_count

    def set_page_count(self, value):
        # only allow page_count to be set if it's an integer
        if type(value) is int and 0 <= value:
            self._page_count = value
        else:
            print("page_count must be an integer")

    # wires get_page_count/set_page_count together so page_count behaves
    # like a normal attribute but runs validation on assignment
    page_count = property(get_page_count, set_page_count)


    # turns the page for reading online book
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        if self.current_page < self.page_count:
            self.current_page += 1

    # tells user what page they're on now
    def display_current_page(self):
        print(f"You are on page {self.current_page} of {self.page_count}.")

    # tells user the total page count / book length
    def display_page_count(self):
        print(f"This book has {self.page_count} pages.")