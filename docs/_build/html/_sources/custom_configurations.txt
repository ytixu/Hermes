
Customize Hermes
================

You can locate Hermes' configuration file ``/Hermes/hermes/config.cfg``. Once Hermes package is installed, you can also find the configuation file in the ``/Hermes/build`` directory.::

	[Constructor]
	delimiter = ,
	quotechar = "
	edge_attributes = label,weight
	node_attributes = label,weight,closeness_centrality,louvain_community,betweenness_centrality,eigenvector_centrality,degree_centrality
	float_column = weight,closeness_centrality,betweenness_centrality,eigenvector_centrality,degree_centrality
	source = source
	target = target
	id = id

	# default settings for centrality
	# empty value will be set to None

	[getClosenessCentrality]
	u =
	distance =
	normalized = True

	[getBetweennessCentrality]
	k =
	normalized = True
	weight =
	endpoints = False
	seed =

	[getEigenvectorCentrality]
	max_iter = 100
	tol = 1e-06
	nstart =
	weight = weight

	[Default]
	edge-list = edge-list.csv
	node-list = node-list.csv
	convert-edge-list = edge-list.csv
	convert-node-list = out.csv
	output-file = out
	analysis = centrality,modularity

-----------
Constructor
-----------

The ``Constructor`` section determines the formatting of the input CSV files.

1. ``delimiter`` and ``quotechar`` to specify the `dialects <https://docs.python.org/2/library/csv.html#dialects-and-formatting-parameters>`_.
2. ``source``, ``target`` and ``edge_attributes`` dictates the header of the edge-list. You can append new edge attributes to ``edge_attributes``.
3. ``id`` and ``node_attributes`` dictates the header of the node-list. You can append new node attributes to ``node_attributes``.
4. Any column that need to be considered to contain float values should be listed in ``float_column``.

---------------------
Centrality parameters
---------------------

The configuration related to centrality are based on the input parameters to the methods `closeness_centrality <https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.bipartite.centrality.closeness_centrality.html>`_, `betweenness_centrality <https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.bipartite.centrality.betweenness_centrality.html>`_ and `eigenvector_centrality <https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.eigenvector_centrality.html>`_ in NetworkX. Please refer NetworkX's documentation for more details.

------------------------------
Default command-line arguments
------------------------------

In the ``Default`` section,

1. ``edge-list`` and ``node-list`` dictates the default edge-list and node-list input files for centrality or modularity analysis.
2. ``convert-edge-list`` and ``convert-node-list`` dictates the default edge-list and node-list input files to convert to GEXF format.
3. ``output-file`` dictates the default output file name.
4. ``analysis`` dictates the defeault analysis that Hermes will preform.



