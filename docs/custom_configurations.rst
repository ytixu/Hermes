
Customize Hermes
================

You can locate Hermes' configuration file ``hermes/config.cfg``.::

	[Constructor]
	delimiter = ,
	quotechar = "
	edge_attributes = label,weight
	node_attributes = label,weight
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

-----------
Constructor
-----------

The ``Constructor`` section determines the configuration of the input ``.csv`` files.

1. ``delimiter`` and ``quotechar``
2. ``source``, ``target`` and ``edge_attributes`` dictates the header of the edge-list. You can append new edge attributes to ``edge_attributes``.
3. ``id`` and ``node_attributes`` dictates the header of the node-list. You can append new node attributes to ``node_attributes``.

---------------------
Centrality parameters
---------------------

The configuration related to centrality are based on the input parameters to the methods ``closeness_centrality``, ``betweenness_centrality`` and ``eigenvector_centrality`` in NetworkX. Please refer NetworkX's documentation for more details.