
Command-Line Interface
======================

``hermes`` works as the follwing:

1. Build graph from ``.csv``, ``.gexf`` or ``.gpickled`` file
2. Run centrality measure statistics and/or community detection
3. Output graph to ``.gpickle`` or ``.gexf`` file

Usage::

	hermes -n <node-list-file> -e <edge-list-file> -d -g -i <input-graph-object-file> -g -o <output-file> <command> <command> <command> ...

Run ``hermes -h`` to display usage information on the command line.

-----------------------------------
Input file options and requirements
-----------------------------------

``.gpickled`` and ``.gexf`` files should be usually generated from NetworkX's `write_gpickle <http://networkx.readthedocs.io/en/networkx-1.11/reference/generated/networkx.readwrite.gpickle.write_gpickle.html>`_ and `write_gexf <http://networkx.readthedocs.io/en/networkx-1.11/reference/generated/networkx.readwrite.gexf.write_gexf.html>`_ methods respectively. Use the option ``-i`` or ``--ifile`` to input ``.gpickled`` file. Add ``-g`` before the option to indicate that the file has extension ``.gexf``.

For ``.csv`` input file, two formats are accepted.

***********************
1. The edge-list format
***********************

Edge-lists must have a header that includes ``source`` and ``target``, indicating the column for the unique indentifiers of the source and target nodes. ``label`` and ``weight`` can also be added as edge attributes. For customizing the header, refer to `Customize Hermes > Constructor <./custom_configurations.html#constructor>`_.

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

Note-lists must have a header that includes ``id``, indicating the column for the unique indentifier of the node. ``label`` and ``weight`` can also be added as node attributes. For customizing the header, refer to `Customize Hermes > Constructor <./custom_configurations.html#constructor>`_.

Use ``-n`` or ``--node-list`` to input file of this format.

Example::

	id,label,weigth
	1,Lemuria,323
	2,Avalon,665
	3,Babylon,60
	4,Atlantis,33
	5,Montreal,4
	...

Node-lists allow users to specify more information about the nodes. Therefore, they are usually accompanied with an edge-list. When using both at the same time, user should make sure that the unique indentifiers match between the two files.

-------------------
Output file options
-------------------

Use ``-o`` or ``--ofile`` to indicate the output file name (file extension can be ommitted). Add ``-g`` before the option to output in GEXF format, otherwise hermes will output a ``.gpickle`` file.

If no output file name is inputted, hermes will output to ``out.gexf`` (in GEXF format) by defaut.

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

``modularity``: preform community detection

If no command is inputted as an argument, hermes will run all the analysis.

All centrality measures are computed using NetworkX. Modularity is computed using python-louvain.

--------
Examples
--------

``hermes -e test/data/random-edge-list.csv -n test/data/random-node-list.csv``

This will compute all centrality measure statistics and run community detection on the graph constructed with edge-list ``test/data/random-edge-list.csv`` and node-list ``test/data/random-node-list.csv``. The output will be found in file ``out.gexf`` under the directory where ``hermes`` is called.

``hermes -i example.gpickle -g -o result eigenvector-centrality modularity``

This will load the graph in ``example.gpickle``, compute eigenvector centrality and communities, and save output to ``result.gexf``

``hermes -g -i example.gpickle -o result``

This will throw an error as hermes will try to load ``example.gpickle`` as a ``.gexf`` file.