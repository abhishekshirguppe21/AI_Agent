from collections import deque
import time

# SLE-2: BFS vs DFS empirical profiling
# Same graph, start node and goal are used for both algorithms.

GRAPH = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I", "J"],
    "E": ["K"],
    "F": ["L"],
    "G": ["M"],
    "H": ["N"],
    "I": ["O"],
    "J": ["O"],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": []
}

START = "A"
GOAL = "O"
RUNS = 5
REPETITIONS = 20000


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    expanded = 0

    while queue:
        node = queue.popleft()
        expanded += 1

        if node == goal:
            return expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return expanded


def dfs(graph, start, goal):
    stack = [start]
    visited = {start}
    expanded = 0

    while stack:
        node = stack.pop()
        expanded += 1

        if node == goal:
            return expanded

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return expanded


def benchmark(search_function):
    start_time = time.perf_counter()
    for _ in range(REPETITIONS):
        search_function(GRAPH, START, GOAL)
    end_time = time.perf_counter()

    return (end_time - start_time) / REPETITIONS * 1000


print("SLE-2: BFS vs DFS Profiling")
print("Graph nodes:", len(GRAPH))
print("Start:", START, "| Goal:", GOAL)
print("Runs:", RUNS, "| Repetitions per run:", REPETITIONS)
print()

bfs_times = []
dfs_times = []

for run in range(1, RUNS + 1):
    bfs_ms = benchmark(bfs)
    dfs_ms = benchmark(dfs)
    bfs_times.append(bfs_ms)
    dfs_times.append(dfs_ms)

    print(f"Run {run}: BFS = {bfs_ms:.6f} ms/search, DFS = {dfs_ms:.6f} ms/search")

bfs_nodes = bfs(GRAPH, START, GOAL)
dfs_nodes = dfs(GRAPH, START, GOAL)

print()
print(f"BFS average time: {sum(bfs_times) / RUNS:.6f} ms/search")
print(f"DFS average time: {sum(dfs_times) / RUNS:.6f} ms/search")
print(f"BFS nodes expanded: {bfs_nodes}")
print(f"DFS nodes expanded: {dfs_nodes}")
