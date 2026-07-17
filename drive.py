import networkx as nx
import matplotlib.pyplot as plt


# This class is responsible for building the graph.
class Drive:

    # Build and draw a random d-regular graph (self.e is the degree here).
    def regular_graph(self):
        G = nx.random_regular_graph(self.e, self.v)
        self.wr(G)
        self.show(G)

    # Build and draw a uniformly random labeled tree.
    def tree_graph(self):
        G = nx.random_labeled_tree(self.v)
        self.wr(G)
        self.show(G)

    # Build and draw a G(n, m) random graph with v nodes and e edges.
    def random_graph(self):
        G = nx.gnm_random_graph(self.v, self.e)
        self.wr(G)
        self.show(G)

    # Write the graph's edge list to the output file.
    def wr(self, G):
        nx.write_edgelist(G, "output_graph.txt")

    # Set the number of nodes.
    def update_v(self, v_input):
        self.v = v_input

    # Set the number of edges (or the degree, for regular graphs).
    def update_e(self, e_input):
        self.e = e_input

    # Show the graph to the user.
    def show(self, G):
        nx.draw(G, with_labels=True)
        plt.title("Generated graph (close this window to continue)")
        plt.show()
