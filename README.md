# Random-walks

The final project in our Bachelor's degree.

A small Tkinter GUI for measuring the **cover time** of a random walk — the number of
steps a simple random walk needs before it has visited every node of a graph at least
once. You can run it on a random regular graph, a G(n, m) random graph, or a random tree.

## How it works

1. Enter the number of nodes and edges (for a **regular** graph, the second field is the
   degree of every node) and click one of the graph buttons. The graph is drawn on screen
   and its edge list is saved to `output_graph.txt`.
2. Close the plot window, then choose **File → Open**. The program loads the saved graph
   and runs a random walk from node 0 until every node has been visited, then pops up the
   total number of steps, the number of nodes, and the density of the graph.
3. If **Show Graph** is checked, the walk is drawn every ~√n steps (blue = unvisited,
   red = visited, green = current node) and the latest frame is saved to
   `random_walk_2d.png`.

The per-edge traversal counts after every step are appended to `edge_steps.csv`
(one column per edge, one row per step).

## Requirements

- Python 3 with Tkinter (bundled with most installers; on Debian/Ubuntu:
  `sudo apt install python3-tk`)
- [networkx](https://networkx.org/) and [matplotlib](https://matplotlib.org/)

```sh
pip install -r requirements.txt
```

## Running

```sh
python3 gui.py
```

Note: the random walk can only cover a connected graph, so the program refuses to run
on a disconnected saved graph.
