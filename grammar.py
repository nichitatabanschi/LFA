# grammar.py

import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}
        self.VT = {'a', 'b'}
        self.P = {
            'S': ['aA'],
            'A': ['bS', 'aB'],
            'B': ['bC', 'aB'],
            'C': ['aA', 'b']
        }

    def generate_valid_strings(self, num_strings=5):
        valid_strings = []
        for _ in range(num_strings):
            valid_strings.append(self.generate_string('S'))
        return valid_strings

    def generate_string(self, symbol):
        if symbol in self.VT:  # If the symbol is a terminal, return it
            return symbol
        else:
            production = random.choice(self.P[symbol])  # Choose a random production for the symbol
            string = ''
            for s in production:
                string += self.generate_string(s)  # Recursively generate strings for each symbol in the production
            return string
