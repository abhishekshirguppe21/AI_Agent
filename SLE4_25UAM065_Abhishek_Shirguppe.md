# SLE-4: Final Viva & Architecture Decision Record (ADR)

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM065  
**Name:** Abhishek Ajit Shirguppe  
**Division:** A  
**Date:** 17 October 2026  
**GitHub Repository:** https://github.com/abhishekshirguppe21/AI_Agent

---

## PART A: Architecture Decision Record (ADR)

### Title: Choose Breadth-First Search (BFS) for the Tested Graph-Search Task

**Status:** Accepted  
**Date:** 17 October 2026  
**PRN & Name:** 25UAM065 – Abhishek Ajit Shirguppe

### 1. Context

In SLE-2, I compared Breadth-First Search (BFS) and Depth-First Search (DFS) using the same 15-node graph. Both searches used node A as the start and node O as the goal. The experiment measured average execution time and the number of nodes expanded. The purpose was to use actual profiling results, rather than theory alone, to understand how the algorithms behaved on this input. I needed to decide which algorithm was more suitable for this particular tested graph-search task.

### 2. Decision

For the tested graph-search task, I choose **Breadth-First Search (BFS)**. In the recorded experiment, BFS expanded fewer nodes and had a lower average execution time than DFS. This decision applies to the tested graph and conditions; it does not mean BFS is always faster for every problem.

### 3. Alternatives Considered

- **Depth-First Search (DFS):** Explores a path deeply before backtracking. It was tested, but expanded more nodes in this experiment.
- **BFS:** Explores nodes level by level. It was selected because it performed better on the measured input.
- **Greedy Best-First Search (optional alternative):** Uses a heuristic to guide exploration, but it was not part of the recorded SLE-2 benchmark and was not compared experimentally here.

### 4. Rationale / Justification

- The SLE-2 experiment used the same graph and start/goal nodes for BFS and DFS, making the comparison fair for this test.
- The graph contained 15 nodes, with A as the start and O as the goal.
- The report recorded an average time per search of **0.001000 ms for BFS** and **0.002293 ms for DFS**.
- BFS expanded **4 nodes**, while DFS expanded **15 nodes** before reaching the goal in the recorded test.
- Therefore, BFS had both the lower measured time and the lower node-expansion count for this particular input.
- Keeping the search algorithm as a separate part of a program makes it easier to test or replace the algorithm without mixing it with input handling or result display.
- The design decision is supported by the SLE-2 profiling results; the architecture point should be checked against the exact modules shown in my submitted SLE-3 C4 diagrams.
- These numbers describe this experiment and execution environment only; they do not prove that BFS is universally faster than DFS.

### 5. Consequences

**Positive:**
- The choice is supported by recorded measurements instead of assumptions alone.
- BFS expanded fewer nodes on the tested graph.
- The search logic can be tested separately from input and output handling.

**Negative / Trade-offs:**
- BFS can use more memory because it stores frontier nodes in a queue.
- On a different graph or with a different goal position, DFS may perform differently.
- The recorded timings are very small and may vary with machine load and runtime conditions.

### 6. References

- GitHub repository: https://github.com/abhishekshirguppe21/AI_Agent
- SLE-2 profiling details and recorded results: [README – SLE-2 section](./README.md#sle-2--profiling-report-empirical-performance-analysis)
- SLE-3 C4 diagrams: refer to the diagrams submitted separately, and ensure the architecture statement above matches them.

---

## PART B: Short Summary of My SLE Journey

In SLE-1, I created a basic Python rule-based AI agent that responds to simple questions using predefined responses. I maintained a README and an AI contribution log to document the project and assistance used. In SLE-2, I compared BFS and DFS on the same 15-node graph and recorded execution time and nodes expanded. The results showed that BFS expanded 4 nodes and averaged 0.001000 ms per search, while DFS expanded 15 nodes and averaged 0.002293 ms. In SLE-3, the task was to represent the system architecture through C4 diagrams: Context, Container, Component, and Code. In SLE-4, I used the SLE-2 evidence to record and justify the decision to choose BFS for the tested graph-search task. The decision is limited to the measured test and should be defended with the submitted SLE-3 diagrams.

## PART C: AI Contribution Note

- **AI tools used:** ChatGPT / AI assistance.
- **What AI helped with:** Organizing the ADR sections, explaining the alternatives and trade-offs, and drafting the viva preparation points.
- **What I did myself:** I am responsible for checking the report against my repository, understanding the BFS/DFS profiling results, verifying the final wording, and explaining the decision during viva. The recorded profiling figures are taken from the repository's SLE-2 report.

## PART D: Viva Preparation Notes

1. **Why choose BFS?** In my test, BFS expanded 4 nodes and took an average of 0.001000 ms per search, compared with 15 nodes and 0.002293 ms for DFS.
2. **Why not DFS?** DFS expanded more nodes in this particular graph. It may still be useful for other problems.
3. **What did profiling measure?** Average execution time and the number of nodes expanded.
4. **Is BFS always faster than DFS?** No. Results depend on the graph, traversal order, goal location, implementation, and execution environment.
5. **What is an ADR?** An Architecture Decision Record explains a design decision, the alternatives considered, the reason for the choice, and its consequences.
6. **What is C4?** It is a way to describe software architecture at Context, Container, Component, and Code levels. I should explain the specific modules shown in my own SLE-3 diagrams.
