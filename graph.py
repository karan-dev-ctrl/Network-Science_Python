import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load graph from CSV
G = nx.Graph()
with open("KarateClub.csv") as f:
    for line in f:
        u, v = map(int, line.strip().split(";")) #removes unnecessary spaces(line.strip)
        G.add_edge(u, v)

# Step 2: Adjacency List
adj_list = {node: sorted(list(G.neighbors(node))) for node in G.nodes}

# Step 3: Adjacency Matrix
adj_matrix = nx.to_numpy_array(G, dtype=int)

# Step 4: Degree Statistics
degrees = dict(G.degree())  # stores like key: value(node: degree)
degree_values = list(degrees.values())
min_deg = min(degree_values)
max_deg = max(degree_values)
mean_deg = round(sum(degree_values) / len(degree_values), 2)

# Step 5: Frequency and Relative Frequency.
freq = Counter(degree_values)
total_nodes = len(degree_values)

# Step 6: Export results to file
with open("karate_networkx_results.txt", "w") as f:
    f.write("Adjacency List:\n")
    for node in sorted(adj_list):
        f.write(f"{node}: {adj_list[node]}\n")

    f.write("\nAdjacency Matrix:\n")
    for row in adj_matrix.astype(int):
        f.write(" ".join(map(str, row)) + "\n")

    f.write("\nDegree Statistics:\n")
    f.write(f"Min Degree: {min_deg}\n")
    f.write(f"Max Degree: {max_deg}\n")
    f.write(f"Mean Degree: {mean_deg}\n")

    f.write("\nDegree Frequencies:\n")
    for deg in sorted(freq):
        rel_freq = round(freq[deg] / total_nodes, 3)
        f.write(f"Degree {deg}: Count = {freq[deg]}, Relative Frequency = {rel_freq}\n")

# Step 7: Save histogram
plt.bar(freq.keys(), freq.values(), color='lightgreen')
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Histogram of Node Degrees (Karate Club)")
plt.grid(True)
plt.savefig("karate_networkx_histogram.png")
plt.close()
