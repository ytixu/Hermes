
Command-Line Interface
======================

``hermes`` can be called for two usages.

1. Compute centrality measure statistics and/or community detection on input graph and output to CSV files.

	Usage::

		hermes [-n <node-list-file>] [-e <edge-list-file>] [-d] [-o <output-file>] [<command>] [<command>] [<command>] ...

2. Convert graph stored in CSV files to a GEXF file.

	Usage::

		hermes convert [-n <node-list-file>] [-e <edge-list-file>] [-d] [-o <output-file>]

Run ``hermes -h`` to display usage information on the command line.

-----------------------------------
Input file options and requirements
-----------------------------------

***********************
1. The edge-list format
***********************

Edge-lists must have a header that includes ``source`` and ``target``, indicating the columns for the unique identifiers of the source and target nodes.

``label`` and ``weight`` can also be added as edge attributes but are not required. For customizing the header, refer to `Customize Hermes > Constructor <./custom_configurations.html#constructor>`_.

Use ``-e`` or ``--edge-list`` to input file of this format.

Use ``-d`` or ``--directed`` to indicate that the graph is directed.

Example::

	source,target,label,weigth
	1,5,opal,57
	1,7,malachite,99
	1,8,indigo,75
	1,12,arsenic,48
	1,6,ivory,14
	...

***********************
2. The node-list format
***********************

Note-lists must have a header that includes ``id``, indicating the column for the unique identifier of the node.

``label`` and ``weight`` can also be added as node attributes but are not required. For customizing the header, refer to `Customize Hermes > Constructor <./custom_configurations.html#constructor>`_.

Use ``-n`` or ``--node-list`` to input file of this format.

Example::

	id,label,weigth
	1,Lemuria,323
	2,Avalon,665
	3,Babylon,60
	4,Atlantis,33
	5,Montreal,4
	...

Node-lists allow users to specify more information about the nodes. User may choose to only input an edge-list if no such information is needed.

If no edge-list and no node-list files are provided, Hermes will by default use ``edge-list.csv`` and ``node-list.csv``. For customizing the default input file, refer to `Customize Hermes > Default command-line arguments <./custom_configurations.html#default-command-line-arguments>`_.

-------------------
Output file options
-------------------

Use ``-o`` or ``--ofile`` to indicate the output file name (file extension can be ommitted).

If no output file name is inputted, hermes will output to ``out-node-list.csv`` or ``out.gexf`` by default. For customizing the default output file, refer to `Customize Hermes > Default command-line arguments <./custom_configurations.html#default-command-line-arguments>`_.

-----------------
Command arguments
-----------------

You can choose which analysis for hermes to run.

``degree-centrality``: compute degree centrality (the default is in-degree if the graph is directed)

``in-degree-centrality``: compute in-degree centrality

``out-degree-centrality``: compute out-degree centrality

``closeness-centrality``: compute closeness centrality

``betweenness-centrality``: compute betweenness centrality

``eigenvector-centrality``: compute eigenvector centrality

``centrality``: compute all centrality values (depending on whether the graph is directed or not)

``modularity``: preform community detection (only for non-directed graph)

If no command is inputted as an argument, hermes will run the analysis for ``centrality`` and ``modularity``. For customizing this behavior, refer to `Customize Hermes > Default command-line arguments <./custom_configurations.html#default-command-line-arguments>`_.

All centrality measures are computed using NetworkX. Modularity is computed using python-louvain.