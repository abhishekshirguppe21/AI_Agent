# SLE-3: Architectural Design (Full C4 Model)

## Student Details
- **Name:** Abhishek Ajit Shirguppe
- **PRN:** 25UAM065
- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **Program:** SY B.Tech. CSE (AI & ML)
- **Division:** A

## System Title
**SimpleAI Rule-Based Agent**

## Short Description
SimpleAI is a basic rule-based AI agent that accepts user input and gives a response using predefined rules. The system converts the input into lowercase text and checks it against known keywords or conditions. It is designed as a simple example of an AI agent using condition-based decision making. The complete architecture is documented using the four C4 levels.

## C4 Model Documents
1. [Context Diagram - Level 1](SLE3_Context_Diagram.md)
2. [Container Diagram - Level 2](SLE3_Container_Diagram.md)
3. [Component Diagram - Level 3](SLE3_Component_Diagram.md)
4. [Code Level Overview - Level 4](SLE3_Code_Level.md)

## Main Architecture
The system contains an input module, agent engine, rule set, output module, and exit controller. The Agent Engine processes the user's input and selects a suitable response using predefined rules.

## Design Decisions
- The architecture is divided into small logical parts so that each part has a clear responsibility.
- A rule-based engine is used because the current agent works with predefined keyword conditions and responses.
- The design is kept simple and readable for easy understanding, testing, and future improvement.

## AI Contribution
AI assistance was used to organize and document the C4 architecture. The student reviewed the generated material and selected the parts relevant to the project.

## Conclusion
The C4 model gives a clear view of the SimpleAI Rule-Based Agent from system context to code-level implementation.

**Main project file:** [Agent.py](../Agent.py)
