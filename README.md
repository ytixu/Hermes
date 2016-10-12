# Hermes 0.1

Hermes is a command-line tool for network science.It is based on [NetworkX](https://networkx.github.io/) and [python-louvain](http://perso.crans.org/aynaud/communities/).

Key features:
* Construct network from CSV files
* Compute centrality measures (degree, closeness, betweenness and eigenvector)
* Preform community detection using Louvain method
* Output to GEXF format

![Example graph from test visualized with Gephi](https://ytixu.github.io/Hermes/docs/graph-example.png)

## Quick start

### Installation

Clone this github repository or download the source.

Go to the directory ``/Hermes`` and run

	make install

or

	sudo make install

depending on permission settings on your computer.

Now, you can use the command ``hermes`` on your terminal. Refer to the [online documentation](https://ytixu.github.io/Hermes/docs/_build/html/command_line_interface.html) for detail on its usage.

### Testing

To test Hermes, run

	make test_hermes

This will call ``/Hermes/test/test.py`` to create a random edge-list and a node-list under the directory ``/Hermes/test/data``. Then, the command ``hermes`` will be triggered to create the output, ``out.gexf``, with all centrality measures and detected communities as node attributes.

## Documentation

Online documentation available here:

https://ytixu.github.io/Hermes/docs/_build/html/index.html