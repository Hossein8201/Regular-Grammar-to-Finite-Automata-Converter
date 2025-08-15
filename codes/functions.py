from collections import deque
from DFA import DFA

def compute_complement(dfa):
    """
    Computes the complement of a given DFA.
    
    Parameters:
        dfa (DFA): The input DFA.
        
    Returns:
        DFA: A new DFA representing the complement of the input DFA.
    """
    complement_dfa = DFA()
    complement_dfa.states = dfa.states.copy()
    complement_dfa.alphabet = dfa.alphabet.copy()
    complement_dfa.transitions = dfa.transitions.copy()
    complement_dfa.start_state = dfa.start_state
    
    # New set of accepting states = all states except the original accepting states
    complement_dfa.accept_states = dfa.states.difference(dfa.accept_states)
    
    return complement_dfa

def compute_union(dfa1, dfa2):
    """
    Computes the union of two DFAs.
    
    Parameters:
        dfa1 (DFA): The first input DFA.
        dfa2 (DFA): The second input DFA.
        
    Returns:
        DFA: A new DFA representing the union of the two input DFAs.
    """
    if dfa1.alphabet != dfa2.alphabet:
        raise ValueError("Alphabets must be the same.")

    union_dfa = DFA()
    union_dfa.alphabet = dfa1.alphabet.copy()
    state_mapping = {}
    queue = deque()
    state_count = 0

    # Initial state
    start_state = (dfa1.start_state, dfa2.start_state)
    union_dfa.start_state = f"q{state_count}"
    state_mapping[start_state] = union_dfa.start_state
    union_dfa.states.add(union_dfa.start_state)
    queue.append(start_state)
    state_count += 1

    while queue:
        current_pair = queue.popleft()
        current_state_name = state_mapping[current_pair]
        s1, s2 = current_pair

        # Check accepting states
        if s1 in dfa1.accept_states or s2 in dfa2.accept_states:
            union_dfa.accept_states.add(current_state_name)

        for symbol in union_dfa.alphabet:
            next_s1 = dfa1.transitions.get((s1, symbol), "N")
            next_s2 = dfa2.transitions.get((s2, symbol), "N")
            next_pair = (next_s1, next_s2)

            if next_pair not in state_mapping:
                new_state_name = f"q{state_count}"
                state_mapping[next_pair] = new_state_name
                union_dfa.states.add(new_state_name)
                queue.append(next_pair)
                state_count += 1

            union_dfa.add_transition(current_state_name, symbol, state_mapping[next_pair])

    return union_dfa

def compute_intersection(dfa1, dfa2):
    """
    Computes the intersection of two DFAs.
    
    Parameters:
        dfa1 (DFA): The first input DFA.
        dfa2 (DFA): The second input DFA.
        
    Returns:
        DFA: A new DFA representing the intersection of the two input DFAs.
    """
    if dfa1.alphabet != dfa2.alphabet:
        raise ValueError("Alphabets must be the same.")

    intersection_dfa = DFA()
    intersection_dfa.alphabet = dfa1.alphabet.copy()
    state_mapping = {}
    queue = deque()
    state_count = 0

    # Initial state
    start_state = (dfa1.start_state, dfa2.start_state)
    intersection_dfa.start_state = f"q{state_count}"
    state_mapping[start_state] = intersection_dfa.start_state
    intersection_dfa.states.add(intersection_dfa.start_state)
    queue.append(start_state)
    state_count += 1

    while queue:
        current_pair = queue.popleft()
        current_state_name = state_mapping[current_pair]
        s1, s2 = current_pair

        # Check accepting states
        if s1 in dfa1.accept_states and s2 in dfa2.accept_states:
            intersection_dfa.accept_states.add(current_state_name)

        for symbol in intersection_dfa.alphabet:
            next_s1 = dfa1.transitions.get((s1, symbol))
            next_s2 = dfa2.transitions.get((s2, symbol))
            next_pair = (next_s1, next_s2)

            if next_pair not in state_mapping:
                new_state_name = f"q{state_count}"
                state_mapping[next_pair] = new_state_name
                intersection_dfa.states.add(new_state_name)
                queue.append(next_pair)
                state_count += 1

            intersection_dfa.add_transition(current_state_name, symbol, state_mapping[next_pair])

    if not intersection_dfa.accept_states:
        print("The intersection of the languages is empty.")

    return intersection_dfa