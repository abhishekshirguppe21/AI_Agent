# SLE-3 Repository Checklist

## Required C4 Levels

### Level 1 – Context
User / Operator -> Simple AI Agent -> Response on Console

### Level 2 – Container
Input / Console -> Text Processor -> Rule / Intent Matcher -> Response Generator -> Conversation Loop / Exit Handling

### Level 3 – Component
The **Rule / Intent Matcher** is the selected main container.

Its components are:
- Keyword Detection
- Priority / if-elif Rules
- Response Selection
- Fallback Handler

### Level 4 – Code
Main code elements:
- `ai_agent(user_input)`
- `text = user_input.lower()`
- `if / elif` keyword rules
- `return`
- `while True:`
- `input("You: ")`
- `if user_input.lower() == "bye": break`

## Submission Requirements
- PRN: 25UAM065
- Name: Abhishek Ajit Shirguppe
- Division: A
- Report: `SLE3_Report_25UAM065.md`
- Architecture: `C4_ARCHITECTURE.md`

All four C4 levels are represented, with the Component level covering only one main container.