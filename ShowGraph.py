import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx


# This class is for showing the graph during the random walk.
class ShowGraph:
    # This function initializes the node lists and the layout.
    def __init__(self, G):
        self.visited_nodes = []
        self.unvisited_nodes = list(G.nodes())
        self.pos = nx.spring_layout(G)  # positions for all nodes

    # This function draws the graph, shows it for 2 seconds and saves it to a file.
    # Blue - not yet visited.
    # Red - visited.
    # Green - current node.
    def show_graph(self, G, current_node):
        nx.draw(G, self.pos, nodelist=self.unvisited_nodes, node_color='b', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=self.visited_nodes, node_color='r', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=[current_node], node_color='g', node_size=250, alpha=0.8, with_labels=True)

        plt.title("Random Walk")
        plt.show(block=False)
        plt.savefig('random_walk_2d.png', dpi=250)
        plt.pause(2)
        plt.close()

    # Mark a node as visited (it will be drawn in red).
    def mark_visited(self, n):
        if n in self.unvisited_nodes:
            self.unvisited_nodes.remove(n)
            self.visited_nodes.append(n)
