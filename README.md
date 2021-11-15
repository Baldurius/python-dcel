# (D)oubly-(C)onnected (E)dge (L)ist

This python package contains an implementation of a *doubly-connected edge list* structure that can be used to *create, traverse, and manipulate 2-dimensional graphs*.
The main goal is to write a structure that is *easy to use* and *efficient*, e.g., by allowing simultaneous iteration and modification of nodes and edges.

# What is a DCEL?

A doubly-connected edge list is a graph structure that uses a set of linked nodes and half-edges to simplify traversal.
Each edge of the stored graph consists of two half-edges, each starting at one of the endpoints and facing in opposite direction.
At its core, the DCEL stores a list of nodes and half-edges.
Each node holds a reference to one of its outgoing edges.
Each half-edge holds four references:
  * to its starting node
  * its twin half-edge
  * the next half-edge of the edge's face
  * the previous half-edge of the edge's face
  
With this structure, graph traversal becomes a matter of following the network of connected half-edges through the stored references.
To, e.g., get all outgoing edges of a node, one can write:
```python
edge = node.edge
while True:
    yield edge
    edge = edge.twin.nxt
    if edge == node.edge:
      break
```
or use the provided node-edge iterator:
```python
for edge in node.edges:
    yield edge
```

# Run tests and style checker

The project strictly follows the `PEP8` coding style and uses type hints.
To check all source files for errors and run the tests, simply run:

```shell
check.sh
```

Running the script also creates a `htmlcov` directory that contains code coverage information.

# Example: Creating a graph

To use the library, just import the `Dcel` class from the `dcel` package:

```python
from dcel import Dcel

graph = Dcel()

# Create two nodes
node_1 = graph.add_node()
node_2 = graph.add_node()

# Create two half-edges
edge_1 = graph.add_edge()
edge_2 = graph.add_edge()

# Initialize node properties
node_1.edge = edge_1

node_2.edge = edge_2

# Initialize edge properties
edge_1.node = node_1
edge_1.twin = edge_2
edge_1.prv = edge_2
edge_1.nxt = edge_2

edge_2.node = node_2
edge_2.twin = edge_1
edge_2.prv = edge_2
edge_2.nxt = edge_2
```

# License

This project uses the MIT license. For further details see [LICENSE](LICENSE).
