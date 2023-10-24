from collections import defaultdict


def load_file(file_path):
    clauses = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(int, line.split())
            clauses.append((x, y))
    return clauses


def build_graph(clauses):
    graph = {}
    for x, y in clauses:
        graph[-x] = graph.get(-x, []) + [y]  # -x implies y
        graph[-y] = graph.get(-y, []) + [x]  # -y implies x
    return graph


def dfs(graph, node, visited, stack):
    visited[node] = True
    if node in graph:
        for neighbor in graph[node]:
            if not visited.get(neighbor, False):
                dfs(graph, neighbor, visited, stack)
    stack.append(node)


def scc_dfs(graph, node, visited, scc):
    visited[node] = True
    scc.append(node)
    if node in graph:
        for neighbor in graph[node]:
            if not visited.get(neighbor, False):
                scc_dfs(graph, neighbor, visited, scc)


def is_satisfiable(file_path):
    clauses = load_file(file_path)
    graph = build_graph(clauses)
    visited = {}
    stack = []

    # Perform DFS for topological sorting
    for node in graph:
        if not visited.get(node, False):
            dfs(graph, node, visited, stack)

    transposed_graph = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            transposed_graph[neighbor] = transposed_graph.get(neighbor, []) + [node]

    visited = {}
    strongly_connected_components = []

    # Find strongly connected components
    while stack:
        node = stack.pop()
        if not visited.get(node, False):
            scc = []
            scc_dfs(transposed_graph, node, visited, scc)
            strongly_connected_components.append(scc)

    # Check for unsatisfiability
    for scc in strongly_connected_components:
        for x in scc:
            if -x in scc:
                return "unsatisfiable"

    # Construct the satisfying assignment using temporary and permanent assignments
    assignment = {}
    temp_assignment = {}
    perm_assignment = {}

    for scc in strongly_connected_components:
        for variable in scc:
            if abs(variable) not in assignment:
                temp_assignment[abs(variable)] = variable > 0

    for var, value in temp_assignment.items():
        if var not in perm_assignment:
            assignment[var] = value
            perm_assignment[var] = value

    for scc in strongly_connected_components:
        for variable in scc:
            if variable > 0 and -variable in assignment:
                if perm_assignment[variable] != perm_assignment[-variable]:
                    return "unsatisfiable"

    return assignment


if __name__ == "__main__":
    file_path = "example1.txt"
    result = is_satisfiable(file_path)

    if result == "unsatisfiable":
        print("Unsatisfiable.")
    else:
        print("Satisfiable.")
        print("Variable Assignments:", result)

    cl = load_file("example1.txt")
    out = True
    for c in cl:
        x, y = c
        if x < 0:
            c1 = not result[abs(x)]
        else:
            c1 = result[x]
        if y < 0:
            c2 = not result[abs(y)]
        else:
            c2 = result[y]
        out = out and (c1 or c2)
    print(out)
