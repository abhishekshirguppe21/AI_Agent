# SLE-3 Level 4 - Code Level Overview

## Implementation
The current SimpleAI agent is implemented using procedural Python code. It does not require custom classes such as `class Node`.

## Important Code Elements

### Input
```python
user_input = input("You: ")
```

### Input Normalization
```python
text = user_input.lower()
```

### Agent Function
```python
def ai_agent(user_input):
    # rule-based decision logic
    ...
```

### Decision Logic
The agent uses `if` / `elif` conditions to match user input with predefined keywords and choose a response.

### Output
```python
print("AI:", response)
```

### Exit Condition
The program checks for an exit input such as `bye` and terminates the interaction.

## Level 4 Summary
The code-level view connects the C4 architecture to the actual implementation. The important elements are input collection, text normalization, rule matching, response generation, output, and exit handling.
