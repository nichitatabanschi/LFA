# finite_automaton1.py

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def is_deterministic(self):
        for state in self.states:
            for symbol in self.alphabet:
                if len(self.transitions[state].get(symbol, [])) > 1:
                    return False
        return True

    def convert_to_regular_grammar(self):
        if not self.is_deterministic():
            print("Cannot convert to regular grammar. The finite automaton is non-deterministic.")
            return

        grammar = {}
        for state in self.states:
            grammar[state] = {}
            for symbol, next_states in self.transitions[state].items():
                grammar[state][symbol] = next_states[0]

        print("Regular Grammar:")
        for state in grammar:
            for symbol in grammar[state]:
                print(f"{state} -> {grammar[state][symbol]} | {symbol}")

    def convert_to_dfa(self):
        if self.is_deterministic():
            print("The finite automaton is already deterministic.")
            return

        dfa_transitions = {}
        dfa_states = set()
        initial_state_closure = self.epsilon_closure({self.initial_state})
        dfa_states.add(initial_state_closure)
        queue = [initial_state_closure]

        while queue:
            current_states = queue.pop(0)
            dfa_transitions[current_states] = {}
            for symbol in self.alphabet:
                next_states = self.move(current_states, symbol)
                next_states_closure = self.epsilon_closure(next_states)
                dfa_transitions[current_states][symbol] = next_states_closure
                if next_states_closure not in dfa_states:
                    dfa_states.add(next_states_closure)
                    queue.append(next_states_closure)

        dfa_final_states = {state for state in dfa_states if state.intersection(self.final_states)}
        return dfa_states, dfa_transitions, initial_state_closure, dfa_final_states

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            epsilon_transitions = self.transitions.get(state, {}).get('', [])
            for epsilon_state in epsilon_transitions:
                if epsilon_state not in closure:
                    closure.add(epsilon_state)
                    stack.append(epsilon_state)
        return frozenset(closure)

    def move(self, states, symbol):
        move_states = set()
        for state in states:
            transitions = self.transitions.get(state, {}).get(symbol, [])
            move_states.update(transitions)
        return frozenset(move_states)
