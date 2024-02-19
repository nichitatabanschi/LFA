# finite_automaton.py

class FiniteAutomaton:
    def __init__(self, grammar):
        self.states = grammar.VN
        self.transitions = {}
        for non_terminal, productions in grammar.P.items():
            for production in productions:
                if production[0] in self.states:
                    self.transitions.setdefault(non_terminal, []).append(production[0])

    def check_input_string(self, input_string):
        current_state = 'S'
        for char in input_string:
            if char not in self.transitions.get(current_state, []):
                return False
            current_state = char
        return current_state == 'C'
