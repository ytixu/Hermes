
Command Line Interface
======================

The ``hermes`` pipeline works as the follwing

* Build graph from ``.csv``, ``.gexf`` or ``.gpickled`` file
* Run centrality measure statistics and/or community detection
* Output graph to ``.gpickle`` or ``.gexf`` file

Usage::

	hermes -n <node-list-file> -e <edge-list-file> -d -g -i <input-graph-object-file> -g -o <output-file> <command> <command> <command> ...

Run ``hermes -h`` to display usage information on the command line.

-----------------------------------
Input file options and requirements
-----------------------------------

``.gpickled`` and ``.gexf`` are usually files generated from NetworkX's ``write_gpickle`` and ``white_gexf`` methods respectively. Use the option ``-i or --ifile`` to input ``.gpickled`` file. Add ``-g`` before the option to indicate that the file has extension ``.gexf``.

For ``.csv`` input file, two formats are used.

***********************
1. The edge-list format
***********************

Edge list must have a header that includes ``source`` and ``target``. ``label`` and ``weight`` can also be added.

Use ``-e`` or ``--edge-list`` to input file of this format.

Use ``-d`` or ``--directed`` to indicate that the graph is directed.

Example::

	source,target,label,weigth
	1,5,opal,57
	1,7,lemon,99
	1,8,indigo,75
	1,12,methane,48
	1,6,ivy,14
	...

***********************
2. The node-list format
***********************

Note list must have a header that includes ``id``. ``label`` and ``weight`` can also be added.

Use ``-n`` or ``--node-list`` to input file of this format.

Example::

	id,label,weigth
	1,Lemuria,323
	2,Cyclopean,665
	3,Babylon,60
	4,Atlantis,33
	5,Montreal,4
	...

Note that edge-list and node-list can be used at the same time.



-------------------
Output file options
-------------------

Use ``-o`` or ``--ofile`` to indicate the output file name (extension can be ommitted). Add ``-g`` before the option to output in ``.gexf`` format, otherwise hermes will output in ``.gpickle`` format.

If no output file name is inputted, hermes will output to ``out.gexf`` (in ``.gexf`` format) by defaut.

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