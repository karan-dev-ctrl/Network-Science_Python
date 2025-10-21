import networkx as nx

# Step 1: Load graph from CSV
G = nx.Graph()
with open("KarateClub.csv") as f:
    for line in f:
        u, v = map(int, line.strip().split(";")) #removes unnecessary spaces(line.strip)
        G.add_edge(u, v)



# Step 2: To identify the louvain_communities()
lv_communities = nx.community.louvain_communities(G, seed=123)
print("louvain_communitie : ", lv_communities)


#Step 3: To identify the label_propagation_communities()
label_communities = nx.community.label_propagation_communities(G)
print("label_propagation_communities : ", label_communities)



#Step 4 : To determine kernighan_lin_bisection() using recursion_kl_bisection method (for 4 communities)
def recursive_kl_bisection(G, target_comm=4, seed=None):


    #starts from all communities
    communities = [set(G.nodes())] 

    while len(communities) < target_comm:


        #find the largest split of communities

        largest_comm = max(communities)
        subgraph = G.subgraph(largest_comm)

        # skip if it is less than 2
        if subgraph.number_of_nodes() < 2:
            break
        # here bisect into two sets
        try:
            part1, part2 = nx.community.kernighan_lin_bisection(subgraph, seed=seed)
        except nx.NetworkXError:
            break


        communities.remove(largest_comm)
        communities.append(set(part1))
        communities.append(set(part2))

    return communities


kl_communities = recursive_kl_bisection(G, target_comm=4, seed=None)

#print the final output of 4 communities 
print("kernighen lee with 4 communities : ")

for i, comm in enumerate(kl_communities, 1):
    print(f"community {i}: {sorted(comm)}")


