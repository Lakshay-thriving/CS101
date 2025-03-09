# CS101 Project 2

## Part 1: PageRank Using a Random Walk

### Introduction
In web search algorithms, PageRank determines the importance of web nodes based on incoming links. One way to compute PageRank is through a random walk, simulating a random surfer navigating a network.

### PageRank Using the Gold Coin Method
Imagine a group of people, each representing a node. We distribute 10,000,000 gold coins randomly across nodes. After distributing all coins, the PageRank is calculated as the proportion of coins each node receives.

### Eigenvalue Method and Matrices
A network of nodes is represented by an $n \times n$ matrix $M$, where $M_{ij}$ denotes the probability of transitioning from node $i$ to node $j$. By applying the power iteration method to the matrix, the dominant eigenvector emerges, representing the steady-state probabilities, which equates to the PageRank.

### Dangling Nodes and Teleportation
Dangling nodes are nodes with no outgoing links, potentially stalling PageRank calculations. To prevent this, a damping factor $d$ (typically 0.85) is introduced. The PageRank algorithm thus incorporates a probability of jumping to a random node (teleportation) to ensure continuity.

### Results
Using the teleportation-based PageRank algorithm, we identified the leader of the network as **2023CSB1091**.

---

## Part 2: Finding Missing Links in the Graph

### Introduction
To detect missing links in a directed graph, we used the least squares method, leveraging linear algebra.

### Adjacency Matrix Construction
The directed graph is represented as an adjacency matrix $A$, where $A_{ij} = 1$ if node $i$ is connected to node $j$, and $A_{ij} = 0$ otherwise.

### Least Squares Method
If a row in the adjacency matrix contains a missing link ($A_{ij} = 0$), we solve a system of linear equations using the least squares approach. The missing link is inferred based on the computed coefficients, replacing zeros where appropriate.

### Bidirectional Links
We analyze if missing links are bidirectional, unidirectional, or nonexistent by evaluating the inferred adjacency matrix.

### Conclusion
By applying the least squares method, missing links were successfully inferred and restored in the impression network, providing a structured way to analyze social interactions.

---

## Part 3: Finding a New Question from the Impression Network

### Introduction
We analyzed a directed graph representing connections between students from Computer Science (CS) and Mathematics and Computing (MnC) departments. Our goal was to assess variance and stability after removing students with more friends outside their department than within it.

### Variance Calculation
Variance quantifies the dispersion of nodeRank scores:
\[
\text{Variance} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}
\]
where $x_i$ are nodeRank scores, $\bar{x}$ is the mean, and $n$ is the total number of students.

### Stability Calculation
Stability measures the effect of node removal on variance:
\[
\text{Stability (\% change)} = \left( \frac{\text{New Variance} - \text{Old Variance}}{\text{Old Variance}} \right) \times 100
\]

### Analysis
After removing students with more external connections, we recalculated variance and stability.

#### Variance Analysis
- The original variance was **$V_{\text{old}} = X$**.
- After removal, variance changed to **$V_{\text{new}} = Y$**.

#### Stability Analysis
- Stability was computed as:
\[
\text{Stability (\% change)} = \left( \frac{Y - X}{X} \right) \times 100
\]
- The CS subgraph's stability increased by **76.94\%**, while MnC subgraph's stability increased by **0.5\%**.

### Observations
1. **CS subgraph impact:** The drastic increase in stability suggests that removing students with more cross-departmental ties reduced noise and improved internal consistency.
2. **MnC subgraph stability:** A minor stability increase indicates that fewer students in MnC had cross-departmental ties, making their removal less significant.
3. **Graph structure influence:** CS had ~100 students, MnC ~40. Only 15 CS students and 3 MnC students had more friends in the other department. This small proportion of removals influenced results differently.

### Conclusion
Our findings highlight that:
- Stability is highly dependent on the distribution of connections.
- CS had greater structural changes due to its larger network size.
- The method can effectively detect and analyze influential network nodes.

By leveraging variance and stability analysis, we provide insights into network behavior and cross-departmental interactions. This methodology can be applied in broader social network studies to evaluate the impact of node removal on community structures.
