# main.py

from grammar import Grammar
from finite_automaton import FiniteAutomaton

if __name__ == "__main__":
    grammar = Grammar()
    valid_strings = grammar.generate_valid_strings()
    print("Valid strings:", valid_strings)

    fa = FiniteAutomaton(grammar)
    input_string = "aabb"
    if fa.check_input_string(input_string):
        print(f"'{input_string}' can be obtained via state transitions.")
    else:
        print(f"'{input_string}' cannot be obtained via state transitions.")
