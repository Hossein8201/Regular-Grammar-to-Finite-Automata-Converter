from collections import deque
from NFA import NFA

class DFA:
    """
    Deterministic Finite Automaton (DFA) representation.

    Attributes:
        states (set): Set of states.
        alphabet (set): Set of input symbols.
        transitions (dict): Mapping from (state, symbol) to the next state.
        start_state (str): The initial state.
        accept_states (set): Set of accepting states.

    Methods:
        add_transition(state, symbol, next_state): Adds a new transition.
        get_transition(state, symbol): Retrieves the next state for a given transition.
    """

    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}               # Mapping: {(state, symbol): next_state}
        self.start_state = ""
        self.accept_states = set()

    def __str__(self):
        sentence = "# States\n"
        sentence += " ".join(map(str, self.states))
        sentence += "\n# Alphabet\n"
        sentence += " ".join(map(str, self.alphabet))
        sentence += "\n# Start State\n"
        sentence += self.start_state
        sentence += "\n# Final States\n"
        sentence += " ".join(map(str, self.accept_states))
        sentence += "\n# Transitions\n"
        for ((state, symbol), next_state) in self.transitions.items():
            sentence += f"{state} {symbol} {next_state}\n"
        return (sentence + "\n")

    def add_transition(self, state, symbol, next_state):
        # Adds a new transition to the DFA. 
        self.transitions[(state, symbol)] = next_state
        self.states.add(state)
        self.states.add(next_state)
        self.alphabet.add(symbol)

    def get_transition(self, state, symbol):
        # Retrieves the next state for a given transition. 
        return self.transitions.get((state, symbol), None)

    def display(self):
        # Displays DFA information. 
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print("Transitions:")
        for (state, symbol), next_state in self.transitions.items():
            print(f"  ({state}, {symbol}) -> {next_state}")

def epsilon_closure(nfa, states):
    # Computes the ε-closure for a set of states.
    closure = set(states)
    queue = deque(states)

    while queue:
        state = queue.popleft()
        # Checking ε transitions
        transitions = nfa.get_state_transitions(state)
        if transitions and 'ε' in transitions:
            for next_state in transitions['ε']:
                if next_state not in closure:
                    closure.add(next_state)
                    queue.append(next_state)
    return closure

def convert_nfa_to_dfa(nfa):
    """
    Converts an NFA into a DFA 
        using the **subset construction method**.
    """
    dfa = DFA()
    dfa.start_state = "q0"
    dfa.alphabet = nfa.alphabet - {'ε'}         # Removing ε from DFA alphabet

    state_names = {}                            # Mapping sets of states to DFA state names
    state_num = 1

    # Start with the ε-closure of the NFA’s start state
    initial_states = epsilon_closure(nfa, {nfa.start_state})
    state_names[frozenset(initial_states)] = "q0"

    queue = deque([frozenset(initial_states)])
    processed_states = set()

    while queue:
        current_set = queue.popleft()
        if current_set in processed_states:
            continue

        processed_states.add(current_set)
        current_state_name = state_names[frozenset(current_set)]
        dfa.states.add(current_state_name)

        # Check if any state in the set is an accepting state in the NFA
        for state in current_set:
            if state in nfa.accept_states:
                dfa.accept_states.add(current_state_name)
                break

        for symbol in dfa.alphabet:
            # Compute transitions for this symbol
            next_states = set()
            for state in current_set:
                transitions = nfa.get_state_transitions(state)
                if transitions and symbol in transitions:
                    next_states.update(transitions[symbol])

            if next_states:
                # Compute the ε-closure of the next states
                next_set = epsilon_closure(nfa, next_states)
                next_set_frozen = frozenset(next_set)

                if next_set_frozen not in state_names:
                    state_names[next_set_frozen] = f"q{state_num}"
                    state_num += 1
                    queue.append(next_set_frozen)

                dfa.add_transition(current_state_name, symbol, state_names[next_set_frozen])
            else:
                # If no valid transition exists, move to the dead state
                dfa.add_transition(current_state_name, symbol, "N")

    # Add the dead state if necessary
    if any("N" in transition for transition in dfa.transitions.values()):
        dfa.states.add("N")
        for symbol in dfa.alphabet:
            dfa.add_transition("N", symbol, "N")

    return dfa