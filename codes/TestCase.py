class TestCase:
    def __init__(self, test_id, grammars, operation):
        self.test_id = test_id
        self.grammars = grammars
        self.operation = operation

    def display(self):
        print(f"Test Case {self.test_id}:")
        for grammar in self.grammars:
            grammar.display()
        print(f"Operation: {self.operation}")
        print("-" * 40)