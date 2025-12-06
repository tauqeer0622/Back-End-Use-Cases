class Graph:
    def __init__(self):
        # adjacency list: node -> set of neighbors
        self.adj = {}

    def add_edge(self, u, v):
        """Add an undirected edge u–v"""
        if u not in self.adj:
            self.adj[u] = set()
        if v not in self.adj:
            self.adj[v] = set()

        self.adj[u].add(v)
        self.adj[v].add(u)

    def add_node(self, n):
        """Add a node (useful for isolated vertices)"""
        if n not in self.adj:
            self.adj[n] = set()

    def welsh_powell(self):
        """Perform Welsh–Powell graph coloring."""
        # ensure adjacency sets
        adj_sets = {n: set(neighs) for n, neighs in self.adj.items()}

        # catch neighbors not added as keys (rare but safe)
        all_nodes = set(adj_sets.keys())
        for neighs in adj_sets.values():
            for n in neighs:
                if n not in adj_sets:
                    adj_sets[n] = set()
                    all_nodes.add(n)

        # sort nodes by degree (descending)
        nodes_sorted = sorted(all_nodes, key=lambda x: (-len(adj_sets[x]), x))

        colors = {}
        current_color = 0

        for node in nodes_sorted:
            if node not in colors:
                current_color += 1
                colors[node] = current_color

                for other in nodes_sorted:
                    if other in colors:
                        continue

                    # check if safe to color
                    safe = True
                    for nb in adj_sets[other]:
                        if colors.get(nb) == current_color:
                            safe = False
                            break

                    if safe:
                        colors[other] = current_color

        return colors, current_color
    def display(self):
        print(self.adj)


# ----------------------------------------
# Example usage
# ----------------------------------------
g=Graph()
edges = [("A", "B"),("A", "C"), ("A", "D"),
        ("B", "C"),("C", "D"), ("C", "E"),
        ("D", "E"),("E", "F"),("G", "H")]
for u, v in edges:
    g.add_edge(u, v)

# Add isolated vertex
g.add_node("I")

colors, k = g.welsh_powell()

print("Coloring Result:")
for node in sorted(colors):
    print(f"{node}: Color {colors[node]}")

print("\nTotal Colors Used:", k)

g.display()
