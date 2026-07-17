import math
import random
from tkinter import messagebox

import networkx as nx

from ShowGraph import ShowGraph

CSV_FILE = 'edge_steps.csv'


# This class is for the random walk on the given graph.
class GraphFromTxt:
    # This function initializes the graph we saved before.
    def __init__(self, path="output_graph.txt"):
        with open(path, "r") as file:
            lines = file.readlines()
        self.G = nx.parse_edgelist(lines, nodetype=int)
        self.show = ShowGraph(self.G)
        self.G_edges = sorted(self.G.edges())
        self.stepped_edges = [0] * len(self.G_edges)
        # Map both directions of every edge to its index in G_edges.
        self.edge_index = {}
        for i, (u, v) in enumerate(self.G_edges):
            self.edge_index[(u, v)] = i
            self.edge_index[(v, u)] = i

    # How many times a node was stepped on.
    def stepped(self, G, node):
        return G.nodes[node]['step']

    # Get the index of an edge (in either direction) in G_edges.
    def get_index_of_edge(self, node1, node2):
        return self.edge_index.get((node1, node2), -1)

    # Check if the graph is already covered (every node visited at least once).
    def is_covered(self, G):
        for node in G.nodes():
            if self.stepped(G, node) == 0:
                return False
        return True

    # This is the main function of the random walk. It runs until the graph is
    # covered and returns the total number of steps.
    def random_walk(self, G, s, count_steps, show_graph):
        mod = max(int(math.sqrt(len(G.nodes()))), 1)
        current = s
        while not self.is_covered(G):
            next_node = self.random_neighbor(G, current)
            G.nodes[next_node]['step'] += 1
            self.show.mark_visited(next_node)
            # Show the graph every `mod` steps.
            if show_graph == 1 and count_steps % mod == 1:
                try:
                    self.show.show_graph(G, next_node)
                except Exception as err:
                    print("Could not draw the graph:", err)
            count_steps = count_steps + 1
            index = self.get_index_of_edge(current, next_node)
            if index != -1:
                self.stepped_edges[index] += 1
            self.edge_steps_to_csv(self.stepped_edges)
            current = next_node
        return count_steps

    # Start a new CSV file with one column per edge.
    def init_csv(self):
        with open(CSV_FILE, 'w') as file:
            file.write(','.join('{}-{}'.format(u, v) for u, v in self.G_edges))
            file.write('\n')

    # Append the current per-edge step counts as a CSV row.
    def edge_steps_to_csv(self, row):
        with open(CSV_FILE, 'a') as file:
            file.write(','.join(str(x) for x in row))
            file.write('\n')

    # This function runs the whole random walk and reports the result.
    def run_random(self, show_graph):
        nodes = sorted(self.G.nodes())
        if not nodes:
            messagebox.showerror('Error!', 'The saved graph has no edges, so there is nothing to walk on.')
            return 0
        if not nx.is_connected(self.G):
            messagebox.showerror('Error!', 'The saved graph is not connected, so a random walk cannot cover it.')
            return 0
        nx.set_node_attributes(self.G, 0, 'step')
        s = nodes[0]
        self.G.nodes[s]['step'] += 1
        self.show.mark_visited(s)
        self.init_csv()
        counter = self.random_walk(self.G, s, 1, show_graph)
        messagebox.showinfo('Done!', "Number of steps: " + str(counter)
                            + "\nNumber of nodes: " + str(len(nodes))
                            + "\nThe density of the graph: " + str(nx.density(self.G)))
        return counter

    # Pick the next node from the current node's neighbours, uniformly at random.
    def random_neighbor(self, G, node):
        return random.choice(list(G.adj[node]))
