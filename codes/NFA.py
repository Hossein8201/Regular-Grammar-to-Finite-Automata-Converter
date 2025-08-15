from RegularGrammar import RegularGrammar

class NFA:
    """
    Nondeterministic Finite Automaton (NFA) representation.

    Attributes:
        states (set): Set of states.
        alphabet (set): Set of input symbols.
        transitions (dict): Mapping from (state, symbol) to a set of next states.
        start_state (str): Initial state.
        accept_states (set): Set of accepting states.

    Methods:
        add_transition(state, symbol, next_state): Adds a new transition.
        get_state_transitions(state): Retrieves all transitions for a given state.
    """

    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}                           # {(state, symbol): [next_states]}
        self.start_state = ""
        self.accept_states = set()

    def add_transition(self, state, symbol, next_state):
        # Adds a new transition to the NFA.
        self.transitions.setdefault((state, symbol), []).append(next_state)
        self.states.add(state)
        self.states.add(next_state)
        self.alphabet.add(symbol)

    def get_state_transitions(self, state):
        """
        Retrieves all transitions for a given state.
        Returns: {symbol: [next_states]}
        """
        transitions = {}
        for (s, symbol), next_states in self.transitions.items():
            if s == state:
                transitions.setdefault(symbol, []).extend(next_states)
        return transitions

    def display(self):
        # Displays NFA information.
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print("Transitions:")
        for (state, symbol), next_states in self.transitions.items():
            print(f"  ({state}, {symbol}) -> {next_states}")

def convert_grammar_to_nfa(grammar):
    # Converts a regular grammar into an NFA.
    nfa = NFA()
    nfa.start_state = grammar.start_symbol
    nfa.states = grammar.variables.copy()
    nfa.alphabet = grammar.alphabet.copy()

    for i in grammar.rules:
        left, production = i

        if production == "ε" or production == "Îµ":                    # Empty transition
            nfa.accept_states.add(left)
        elif len(production) == 1 and production in grammar.alphabet:  # Direct transition to accepting state
            accept_state = f"{left}_final"
            nfa.states.add(accept_state)
            nfa.accept_states.add(accept_state)
            nfa.add_transition(left, production, accept_state)
        elif len(production) == 2:                                      # Standard transition
            nfa.add_transition(left, production[0], production[1])
        else:
            raise ValueError(f"Invalid production: {production}")

    return nfa