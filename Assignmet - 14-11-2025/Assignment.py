import random
import csv
import networkx as nx  # only used for exporting to GEXF

def preferential_attachment(n_nodes=550, m=2, seed=42):
    """
    Implements the Barabási–Albert (BA) preferential attachment model manually.
    - Start with a complete graph of 3 nodes (0, 1, 2)
    - Each new node connects to m existing nodes with probability ∝ degree
    """
    random.seed(seed)

    # Start with complete graph of 3 nodes
    edges = []
    nodes = [0, 1, 2]
    for i in range(3):
        for j in range(i + 1, 3):
            edges.append((i, j))

    # Track node degrees
    degree = {0: 2, 1: 2, 2: 2}

    # Add new nodes until we reach n_nodes
    for new_node in range(3, n_nodes):
        # Create weighted list of nodes based on degree
        weighted_nodes = []
        for node, deg in degree.items():
            weighted_nodes.extend([node] * deg)

        # Randomly choose m *distinct* existing nodes
        targets = set()
        while len(targets) < m:
            targets.add(random.choice(weighted_nodes))

        # Add new edges and update degrees
        for target in targets:
            edges.append((new_node, target))
            degree[target] += 1

        degree[new_node] = m  # new node gets m edges

    return edges


def export_to_gephi(edges, filename_prefix):
    """
    Exports the network edges into two formats suitable for Gephi:
    - CSV edge list (source, target)
    - GEXF graph file
    """
    csv_file = f"{filename_prefix}.csv"
    gexf_file = f"{filename_prefix}.gexf"

    # --- Export to CSV ---
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Source", "Target"])
        writer.writerows(edges)
    print(f"✅ Saved edge list for Gephi: {csv_file}")

    # --- Export to GEXF using NetworkX ---
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.write_gexf(G, gexf_file)
    print(f"✅ Saved GEXF for Gephi: {gexf_file}")


# --- Generate BA networks ---
edges_m2 = preferential_attachment(n_nodes=550, m=2, seed=1)
edges_m3 = preferential_attachment(n_nodes=550, m=3, seed=2)

# --- Export for Gephi ---
export_to_gephi(edges_m2, "BA_m2_550")
export_to_gephi(edges_m3, "BA_m3_550")

print("\n🎯 Done! Both networks are ready for Gephi visualization.")
