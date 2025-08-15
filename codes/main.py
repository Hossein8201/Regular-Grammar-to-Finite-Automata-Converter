"""
main.py

This is the main module of the project. It reads regular grammars from `input.txt`.
converts them into NFAs, transforms NFAs into DFAs, applies the specified operation
on DFAs, and writes the final DFA to `output.txt`.
"""

from Parser import Parser
from TestCase import TestCase
from RegularGrammar import RegularGrammar
from NFA import convert_grammar_to_nfa
from DFA import convert_nfa_to_dfa
from functions import compute_union, compute_intersection, compute_complement
import os

# Check if the input file exists
input_file = "input.txt"
if not os.path.exists(input_file):
    raise FileNotFoundError(f"File '{input_file}' not found!")

# Parse the input file and retrieve test cases
parser = Parser(input_file)
tests = parser.test_cases
answer_dfa = []

# Process each test case
for test in tests:
    # Convert regular grammars into NFAs
    nfa_list = [convert_grammar_to_nfa(grammar) for grammar in test.grammars]

    # Convert NFAs into DFAs
    dfa_list = [convert_nfa_to_dfa(nfa) for nfa in nfa_list]

    # Apply the specified operation on the DFAs
    final_dfa = None

    operation = test.operation
    if operation == "Complement":
        # Compute the complement of a single DFA
        final_dfa = compute_complement(dfa_list[0])

    elif operation == "Union":
        # Compute the union of multiple DFAs
        final_dfa = compute_union(dfa_list[0], dfa_list[1])
        for dfa in dfa_list[2:]:
            final_dfa = compute_union(final_dfa, dfa)

    elif operation == "Intersection":
        # Compute the intersection of multiple DFAs
        final_dfa = compute_intersection(dfa_list[0], dfa_list[1])
        for dfa in dfa_list[2:]:
            final_dfa = compute_intersection(final_dfa, dfa)

    # Store the final DFA result
    answer_dfa.append(final_dfa)

# Write the final DFA results into the output file
output_file = "output.txt"
number = 1
with open(output_file, "w", encoding="utf-8") as file:
    for dfa in answer_dfa:
        file.write(str(number) + "\n")  # Write the test case number
        file.write(str(dfa))  # Write the DFA representation
        number += 1

# Print success message
print(f"Processing result saved in '{output_file}'.")