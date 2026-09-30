# SLE-2: Profiling Report – Empirical Performance Analysis

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Abhishek Ajit Shirguppe  
**PRN:** 25UAM065  
**Division:** A  
**Date:** 30 September 2026  
**Repository:** https://github.com/abhishekshirguppe21/AI_Agent

## 1. Algorithms / Versions Profiled

For SLE-2, two standard search algorithms were profiled on the same graph:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

The experiment uses a small 15-node graph with the same start node (**A**) and goal node (**O**) for both algorithms. This makes the comparison controlled and reproducible.

## 2. Profiling Method

The Python program `SLE2_Profile.py` uses:

- `time.perf_counter()` to measure execution time.
- A manual **node-expanded counter** to measure search effort.
- **5 benchmark runs**.
- **20,000 repetitions per run** to make the timing more stable.

The measured time is reported as the average time per search in milliseconds.

## 3. Results

The following values were obtained from the profiling experiment.

| Parameter | BFS | DFS |
|---|---:|---:|
| Average time per search | 0.001000 ms | 0.002293 ms |
| Nodes expanded | 4 | 15 |

Individual benchmark measurements:

| Run | BFS (ms/search) | DFS (ms/search) |
|---|---:|---:|
| 1 | 0.000739 | 0.002542 |
| 2 | 0.000732 | 0.002321 |
| 3 | 0.001111 | 0.002268 |
| 4 | 0.000978 | 0.002228 |
| 5 | 0.001441 | 0.002105 |

## 4. Justification & Analysis

For this particular graph and traversal order, BFS reached the goal after expanding 4 nodes, while DFS expanded all 15 nodes before reaching the goal. The measured average time also differed between the two implementations.

The result demonstrates why empirical profiling is useful. Theoretical properties describe how algorithms behave generally, but the actual execution time and number of nodes expanded depend on the graph structure, goal position, traversal order and implementation.

These results should not be interpreted as a universal statement that BFS is always faster than DFS. They are measurements for the specific graph, implementation and machine used in this experiment.

## 5. AI Contribution Note

AI assistance was used to help select a suitable BFS-versus-DFS profiling experiment, structure the Python profiling code, and organize the report and comparison table.

The student performed the experiment, used the same graph and search conditions for both algorithms, and recorded the profiling results.

## 6. Conclusion

The profiling experiment provides an empirical comparison of BFS and DFS using execution time and nodes expanded. On the selected 15-node graph, BFS expanded fewer nodes and had a lower measured average time than DFS. The experiment also shows the importance of testing algorithms on actual inputs instead of relying only on theoretical descriptions.

The complete profiling code is available in `SLE2_Profile.py`.
