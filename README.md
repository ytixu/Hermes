# Hermes 0.1

Hermes is a command-line tool for network science.It is based on `NetworkX <https://networkx.github.io/>`_ and `python-louvain <http://perso.crans.org/aynaud/communities/>`_.

Key features:
* Construct network from CSV files
* Compute centrality measures (degree, closeness, betweenness and eigenvector)
* Preform community detection using Louvain method
* Output to GEXF format

## Installation

Clone this github repository or download the source.

Go to the directory ``/Hermes`` and run::

	make install

or::

	sudo make install

depending on permission settings on your computer.

## Documentation

Please refer to the online documentation available here:

https://ytixu.github.io/Hermes/docs/_build/html/index.html