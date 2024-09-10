# 2-CNF Solver Using SCCs and DFS

## Overview

This project provides an efficient solution for solving 2-CNF (Conjunctive Normal Form) formulas using Strongly Connected Components (SCCs) and Depth-First Search (DFS) techniques. By transforming the 2-CNF problem into a graph-based representation, the solution optimizes the search process and achieves polynomial time complexity.

## Problem Description

2-CNF formulas are logical formulas in conjunctive normal form where each clause contains exactly two literals. The goal is to determine whether there is a satisfying assignment of truth values to the variables. If a satisfying assignment exists, the formula is considered satisfiable; otherwise, it is unsatisfiable.

## Approach

### Graph Representation

1. **Graph Construction**: 
   - Convert the 2-CNF formula into a directed graph with `2*N` nodes, where `N` represents the number of variables. Each variable and its negation are represented as separate nodes.
   - Represent each clause as two directed edges between nodes in the graph.

2. **SCC Detection**:
   - Apply Depth-First Search (DFS) to identify Strongly Connected Components (SCCs) in the graph. SCCs are crucial for determining whether the formula is satisfiable by revealing mutually reachable groups of nodes.

3. **Satisfiability Check**:
   - After detecting SCCs, check if both a variable and its negation belong to the same SCC. If they do, the formula is unsatisfiable. If not, a satisfying assignment is possible.

## Implementation

The implementation involves the following steps:

1. **Input Transformation**: Convert the 2-CNF formula into a graph format.
2. **SCC Computation**: Use DFS to compute SCCs.
3. **Result Determination**: Evaluate SCCs to determine the satisfiability of the formula.

## Usage

To utilize this implementation:

1. **Define the Variables**: Set the number of variables and list of clauses.
2. **Run the Solver**: Implement the algorithm to determine satisfiability.
3. **Interpret Results**: Assess whether the formula is satisfiable based on the SCC analysis.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Please follow standard GitHub practices for submitting issues and pull requests.
