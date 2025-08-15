# Regular Grammar to Finite Automata Converter

A comprehensive Python implementation for processing regular grammars, converting them to finite automata (NFA and DFA), and performing set operations on the resulting automata.

## 🎯 Project Overview

This project implements a complete pipeline for working with regular languages:
1. **Parse regular grammars** from text files
2. **Convert regular grammars to NFAs** (Nondeterministic Finite Automata)
3. **Transform NFAs to DFAs** using subset construction
4. **Perform set operations** (union, intersection, complement) on DFAs
5. **Generate output** in a standardized format

## 🏗️ Architecture

The project is organized into several key modules:

- **`RegularGrammar.py`** - Core grammar representation class
- **`Parser.py`** - Input file parser for test cases
- **`NFA.py`** - NFA implementation and grammar-to-NFA conversion
- **`DFA.py`** - DFA implementation and NFA-to-DFA conversion
- **`functions.py`** - Set operations (union, intersection, complement)
- **`main.py`** - Main execution pipeline
- **`TestCase.py`** - Test case management

## 🚀 Features

### Core Functionality
- **Regular Grammar Processing**: Parse and validate regular grammar definitions
- **NFA Construction**: Convert regular grammars to equivalent NFAs
- **DFA Conversion**: Transform NFAs to deterministic automata using subset construction
- **Set Operations**: Perform union, intersection, and complement operations on DFAs
- **Multi-DFA Support**: Handle operations involving more than two DFAs

### Algorithm Implementation
- **Subset Construction**: Standard algorithm for NFA to DFA conversion
- **Epsilon Closure**: Proper handling of ε-transitions
- **Dead State Management**: Automatic addition of dead states for invalid transitions
- **State Minimization**: Efficient state representation and naming

## 📁 File Structure

```
Project Root/
├── README.md                # Project overview and instructions (this file)
├── report.pdf               # Project report
├── MidtermProject.pdf       # Midterm project document
└── codes/                   # Source code directory
    ├── main.py                  # Main execution script
    ├── RegularGrammar.py        # Grammar representation
    ├── Parser.py                # Input file parser
    ├── NFA.py                   # NFA implementation
    ├── DFA.py                   # DFA implementation
    ├── functions.py             # Set operations
    ├── TestCase.py              # Test case management
    ├── input.txt                # Input test cases
    └── output.txt               # Generated results
```

## 📖 Input Format

The input file (`input.txt`) contains test cases in the following format:

```
1:
G1:
# Alphabet
a b
# Variables
S A
# Start
S
# Rules
S -> ε
S -> aA
S -> bS
A -> bA
A -> aS
========
# Operation
Complement
```

### Grammar Rules
- **Alphabet**: Input symbols (terminals)
- **Variables**: Non-terminal symbols
- **Start**: Starting symbol
- **Rules**: Production rules in the form `A -> aB` or `A -> a` or `A -> ε`
- **Operation**: Desired set operation (Union, Intersection, or Complement)

## 🔧 Usage

### Running the Project

1. **Ensure Python is installed** on your system
2. **Navigate to the project directory**:
   ```bash
   cd path/to/codes
   ```
3. **Run the main script**:
   ```bash
   python main.py
   ```

### Input Preparation

1. **Create or modify** `input.txt` with your test cases
2. **Follow the format** specified above
3. **Ensure grammar rules** are valid regular grammar productions

### Output

The program generates `output.txt` containing:
- Test case numbers
- DFA representations with:
  - States
  - Alphabet
  - Start state
  - Final states
  - Transition table

## 🧮 Supported Operations

### 1. Complement
- **Input**: Single DFA
- **Output**: DFA accepting the complement language
- **Implementation**: Swaps accepting and non-accepting states

### 2. Union
- **Input**: Multiple DFAs
- **Output**: DFA accepting the union of all input languages
- **Implementation**: Product construction with OR logic for acceptance

### 3. Intersection
- **Input**: Multiple DFAs
- **Output**: DFA accepting the intersection of all input languages
- **Implementation**: Product construction with AND logic for acceptance

## 🔬 Algorithm Details

### Grammar to NFA Conversion
- **ε-rules**: Add to accepting states
- **Single symbol rules**: Create accepting state with direct transition
- **Two-symbol rules**: Standard state-to-state transitions

### NFA to DFA Conversion
- **Subset Construction**: Maps sets of NFA states to DFA states
- **Epsilon Closure**: Computes reachable states via ε-transitions
- **State Naming**: Systematic naming convention (q0, q1, q2, ...)
- **Dead State**: Added for undefined transitions

### Set Operations
- **Product Construction**: Combines states from multiple DFAs
- **State Mapping**: Efficient state representation and lookup
- **Acceptance Logic**: Implements appropriate boolean logic for each operation

## 📊 Example Output

```
1
# States
q0 q1
# Alphabet
b a
# Start State
q0
# Final States
q1
# Transitions
q0 b q0
q0 a q1
q1 b q1
q1 a q0
```

## 🧪 Testing

The project includes built-in test cases covering:
- **Single grammar operations** (complement)
- **Binary operations** (union of two grammars)
- **Multiple grammar operations** (intersection of three grammars)

## 🔍 Error Handling

- **File validation**: Checks for input file existence
- **Grammar validation**: Validates production rule formats
- **Alphabet consistency**: Ensures matching alphabets for set operations
- **State management**: Handles edge cases in automaton construction

## 🎓 Educational Value

This project demonstrates key concepts in:
- **Formal Language Theory**
- **Automata Theory**
- **Regular Languages and Grammars**
- **Finite State Machines**
- **Algorithm Implementation**

## 🚧 Requirements

- **Python 3.x**
- **No external dependencies** (uses only standard library)
- **UTF-8 encoding support** for proper text processing

## 📝 License

This project is created for educational purposes in the Theory of Machines & Languages course.

## 👨‍💻 Author

Student ID: 40133014  
Course: Theory of Machines & Languages  
Semester: 6

## 🤝 Contributing

This is an academic project, but suggestions and improvements are welcome. Please ensure any modifications maintain the educational objectives and theoretical correctness of the algorithms.

---

*This project successfully demonstrates the complete pipeline from regular grammar specification to finite automata operations, providing a solid foundation for understanding formal language theory and automata construction.*
