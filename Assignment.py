import networkx as nx
import community  # python-louvain
import pandas as pd

# Parameters
n = 550
ps = [0.001, 0.006, 0.01]
graphs = []

# Generate graphs
for p in ps:
    G = nx.gnp_random_graph(n, p)
    nx.write_gexf(G, f"graph_p_{p}.gexf")
    graphs.append((p, G))


def analyze_graph(G):
    degrees = [d for n, d in G.degree()]
    avg_degree = sum(degrees) / len(degrees)
    clustering = nx.average_clustering(G)
    components = list(nx.connected_components(G))
    num_components = len(components)
    largest_cc = max(components, key=len)
    subgraph = G.subgraph(largest_cc)
    try:
        avg_path_length = nx.average_shortest_path_length(subgraph)
    except:
        avg_path_length = None

    partition = community.best_partition(G)
    modularity = community.modularity(partition, G)
    num_communities = len(set(partition.values()))

    return {
        "Vertices": G.number_of_nodes(),
        "Edges": G.number_of_edges(),
        "Avg Degree": avg_degree,
        "Clustering Coef": clustering,
        "Avg Path Length": avg_path_length,
        "Connected Components": num_components,
        "Communities (Louvain)": num_communities,
        "Modularity": modularity
    }

# Analyze all graphs
results = []
for p, G in graphs:
    metrics = analyze_graph(G)
    metrics["Edge Prob"] = p
    results.append(metrics)

# Create summary table
df = pd.DataFrame(results)
print(df)
