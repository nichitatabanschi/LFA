class CFGrammar:
    def __init__(self, non_terminals, terminals, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions

    def is_terminal(self, symbol):
        return symbol in self.terminals

    def is_non_terminal(self, symbol):
        return symbol in self.non_terminals

    def is_valid_production(self, production):
        lhs, rhs = production.split('→')
        lhs = lhs.strip()
        rhs = rhs.strip()
        if lhs not in self.non_terminals:
            return False
        if not all(symbol in self.non_terminals.union(self.terminals) for symbol in rhs):
            return False
        return True

    def add_production(self, production):
        if not self.is_valid_production(production):
            print("Invalid production!")
            return
        lhs, rhs = production.split('→')
        lhs = lhs.strip()
        rhs = rhs.strip()
        if lhs in self.productions:
            self.productions[lhs].append(rhs)
        else:
            self.productions[lhs] = [rhs]

    def generate(self, start_symbol, max_length):
        if start_symbol not in self.non_terminals:
            print("Invalid start symbol!")
            return
        if max_length < 1:
            print("Max length should be at least 1!")
            return
        import random
        generated = ''
        stack = [start_symbol]
        while stack:
            current_symbol = stack.pop()
            if self.is_terminal(current_symbol):
                generated += current_symbol
                if len(generated) >= max_length:
                    break
            elif self.is_non_terminal(current_symbol):
                if current_symbol in self.productions:
                    productions_for_current = self.productions[current_symbol]
                    chosen_production = random.choice(productions_for_current)
                    for symbol in chosen_production[::-1]:
                        stack.append(symbol)
                else:
                    print(f"No production found for non-terminal {current_symbol}")
            else:
                print(f"Unknown symbol {current_symbol}")
        return generated

    def generate_valid_strings(self, start_symbol, num_strings, max_length):
        valid_strings = []
        for _ in range(num_strings):
            generated_string = self.generate(start_symbol, max_length)
            valid_strings.append(generated_string)
        return valid_strings


class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def check_string(self, input_string):
        current_state = self.start_state
        for char in input_string:
            if char not in self.alphabet:
                return False
            current_state = self.transitions.get((current_state, char), None)
            if current_state is None:
                return False
        return current_state in self.accept_states


# Define the grammar
VN = {'S', 'A', 'B', 'C'}
VT = {'a', 'b'}
P = {
    'S': ['aA'],
    'A': ['bS', 'aB'],
    'B': ['bC', 'aB'],
    'C': ['aA', 'b']
}

# Create an instance of CFGrammar
cfg = CFGrammar(VN, VT, P)

# Generate 5 valid strings from the grammar
valid_strings = cfg.generate_valid_strings('S', 5, 10)
print("Generated valid strings:")
for string in valid_strings:
    print(string)

# Convert CFGrammar to FiniteAutomaton
states = set(VN)
states.add('q')
transitions = {}
for non_terminal, productions in P.items():
    for production in productions:
        if len(production) == 1 and production in VT:
            # Terminal transition
            if (non_terminal, production) not in transitions:
                transitions[(non_terminal, production)] = 'q'
        elif len(production) == 2 and production[0] in VT and production[1] in VN:
            # Non-terminal transition
            if (non_terminal, production[0]) not in transitions:
                transitions[(non_terminal, production[0])] = production[1]
        elif len(production) == 2 and production[0] in VN and production[1] in VT:
            # Terminal transition after non-terminal
            if (non_terminal, production[1]) not in transitions:
                transitions[(non_terminal, production[1])] = 'q'

fa = FiniteAutomaton(states, VT, transitions, 'S', {'q'})

# Check if input strings can be obtained from the Finite Automaton
input_strings = ['aab', 'abab', 'baa', 'bbb']
for string in input_strings:
    if fa.check_string(string):
        print(f"'{string}' can be obtained from the Finite Automaton.")
    else:
        print(f"'{string}' cannot be obtained from the Finite Automaton.")
