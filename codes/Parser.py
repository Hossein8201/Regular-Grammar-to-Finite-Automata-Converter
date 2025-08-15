from TestCase import TestCase
from RegularGrammar import RegularGrammar

class Parser:
    def __init__(self, file_path):
        self.test_cases = []
        self._parse_file(file_path)
        
    def _parse_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            current_test_case = None
            current_grammars = []
            current_operation = None
            section = None

            for line in file:
                line = line.strip()
                if not line or line.startswith("="):                # Ignore empty lines and separators
                    continue

                if line[0].isdigit() and line.endswith(":"):        # New test case
                    if current_test_case:                           # Save previous test case
                        self.test_cases.append(TestCase(current_test_case, current_grammars, current_operation))
                    current_test_case = line[:-1]                   # Remove ":"
                    current_grammars = []
                    current_operation = None
                    continue

                if line.startswith("G"):
                    current_grammars.append(RegularGrammar(line[:-1]))
                    continue

                if line.startswith("#"):
                    section = line[1:].strip()
                    continue

                if current_grammars:
                    grammar = current_grammars[-1]                  # Get the last grammar in the list
                    if section == "Alphabet":
                        grammar.alphabet.update(line.split())
                    elif section == "Variables":
                        grammar.variables.update(line.split())
                    elif section == "Start":
                        grammar.start_symbol = line
                    elif section == "Rules":
                        grammar.rules.append(tuple(line.split(" -> ")))
                    elif section == "Operation":
                        current_operation = line

            if current_test_case:                                   # Save the last test case
                self.test_cases.append(TestCase(current_test_case, current_grammars, current_operation))
