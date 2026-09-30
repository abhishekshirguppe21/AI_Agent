# AI_Agent

A basic Python rule-based AI agent that responds to simple questions using predefined responses.

## Project
- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **Student:** Abhishek Ajit Shirguppe
- **PRN:** 25UAM065
- **Division:** A

## Files
- [Agent.py](./Agent.py) – Main Python AI Agent
- [AI log](./AI%20log) – AI Contribution Log

## How to Run
Run: `python Agent.py`

Type questions such as: hello, What is Python?, What is GitHub?, help, What is your name?
Type **bye** to exit.

## SLE-2 – Profiling Report: Empirical Performance Analysis

### Topic
**Empirical Performance Analysis of BFS and DFS**

SLE-2 evaluates the practical performance of two standard graph-search algorithms:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

Both algorithms are tested under the same conditions so that their observed performance can be compared fairly.

### Objective
The main objectives of this SLE-2 experiment are to:
1. Implement BFS and DFS in Python.
2. Use the same graph, start node, and goal node for both algorithms.
3. Measure actual execution time.
4. Count the number of nodes expanded by each algorithm.
5. Repeat the experiment to obtain more stable timing measurements.
6. Analyze the observed results and relate them to algorithm behavior.

### Experimental Setup
- **Graph size:** 15 nodes
- **Start node:** A
- **Goal node:** O
- **Benchmark runs:** 5
- **Repetitions per run:** 20,000
- **Timing method:** Python `time.perf_counter()`
- **Performance metrics:** average execution time per search and nodes expanded

Using the same input conditions for BFS and DFS makes the experiment controlled and reproducible.

### Profiling Results

| Parameter | BFS | DFS |
|---|---:|---:|
| Average time per search | 0.001000 ms | 0.002293 ms |
| Nodes expanded | 4 | 15 |

The timing values are empirical measurements for this specific implementation, graph, traversal order, and execution environment.

### Analysis
For the selected graph, BFS reaches the goal after expanding 4 nodes, while DFS expands 15 nodes before reaching the goal. The measured execution times also differ.

This experiment demonstrates why empirical profiling is useful: theoretical complexity describes general algorithm behavior, while actual performance can depend on the input graph, goal position, traversal order, implementation, and machine.

The results **should not be treated as a universal claim that BFS is always faster than DFS**. They describe the behavior observed in this particular experiment.

### AI Contribution
AI assistance was used to help select the BFS-versus-DFS profiling approach, structure the Python benchmarking code, and organize the report. The student performed the experiment using the same graph and search conditions for both algorithms and recorded the profiling results.

### Conclusion
The SLE-2 experiment provides an empirical comparison of BFS and DFS using two measurable performance indicators: execution time and nodes expanded. On the selected 15-node graph, BFS expanded fewer nodes and had a lower measured average time than DFS. The experiment highlights the importance of testing algorithms on actual inputs in addition to studying their theoretical properties.

### SLE-2 Files
- [SLE2_Profile.py](./SLE2_Profile.py) – BFS vs DFS profiling program
- [SLE2_Report_25UAM065.md](./SLE2_Report_25UAM065.md) – Complete SLE-2 profiling report
- [SLE2_AI_Log.md](./SLE2_AI_Log.md) – AI contribution log
