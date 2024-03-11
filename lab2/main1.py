# main1.py
from finite_automaton1 import FiniteAutomaton
from graph_drawer import GraphDrawer

# Finite Automaton definition
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'a', 'b', 'c'}
transitions = {
    'q0': {'a': ['q0', 'q1'], 'b': ['q2']},
    'q1': {'a': ['q1'], 'b': ['q3'], 'c': ['q2']},
    'q2': {'b': ['q3']},
    'q3': {}
}
initial_state = 'q0'
final_states = {'q3'}

fa = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

# Determine if FA is deterministic or non-deterministic
if fa.is_deterministic():
    print("The finite automaton is deterministic.")
else:
    print("The finite automaton is non-deterministic.")

# Convert FA to Regular Grammar
fa.convert_to_regular_grammar()

# Convert NFA to DFA
dfa_states, dfa_transitions, dfa_initial_state, dfa_final_states = fa.convert_to_dfa()
print("\nDFA States:", dfa_states)
print("DFA Transitions:", dfa_transitions)
print("DFA Initial State:", dfa_initial_state)
print("DFA Final States:", dfa_final_states)

# Draw Finite Automaton
GraphDrawer.draw(states, transitions)
