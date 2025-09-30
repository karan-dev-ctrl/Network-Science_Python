import networkx as nx
import csv

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

# Step 4: Shortest path, Mean Degree & Diameter
shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
mean_distance = nx.average_shortest_path_length(G)
Diameter = nx.diameter(G)

# Step 5: Closeness Centrality (c(u)) = n-1/sum(d(u,v))
Closeness_centrality = nx.closeness_centrality(G)

# Step 6: Export results to file
with open("Shortest Path, Mean & Diameter, Closeness Centerality.txt", "w") as f:
    f.write("Adjacency List:\n")
    for node in sorted(adj_list):
        f.write(f"{node}: {adj_list[node]}\n")

    f.write("\nAdjacency Matrix:\n")
    for row in adj_matrix.astype(int):
        f.write(" ".join(map(str, row)) + "\n")

    f.write("\n Shortest Path, Mean Degree and diameter:\n")
    f.write(f"Shortest_Paths: {shortest_paths}\n")
    f.write(f"Mean_Distance: {mean_distance}\n")
    f.write(f"Diameter: {Diameter}\n")
    f.write(f"Closeness_Centrality: {Closeness_centrality}\n")

# Step:7 - Save the file in csv format
with open("ClosenessCentrality.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Mean Distance", mean_distance])
    writer.writerow(["Diameter", Diameter])
    writer.writerow(["IdVertex", "Clos. Centr"])
    for node, centrality in Closeness_centrality.items():
        writer.writerow([node, centrality])
        