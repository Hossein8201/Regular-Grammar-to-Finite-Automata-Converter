class RegularGrammar:
    def __init__(self, name):
        self.name = name
        self.alphabet = set()
        self.variables = set()
        self.start_symbol = None
        self.rules = []

    def display(self):        
        print(f"Grammar: {self.name}")
        print(f"  Alphabet: {self.alphabet}")
        print(f"  Variables: {self.variables}")
        print(f"  Start Symbol: {self.start_symbol}")
        print(f"  Rules: {self.rules}")