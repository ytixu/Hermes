
Installation
============

Clone the github repository or download the source code from

https://github.com/ytixu/Hermes

Go to the directory ``/Hermes`` and run::

	make install

or::

	sudo make install

depending on permission settings on your computer.

Note that Hermes depends on the Python package `NetworkX (>= 1.11) <https://networkx.github.io/>`_ and `python-louvain (>= 0.5) <http://perso.crans.org/aynaud/communities/>`_. If those are found to be missing, the above command will automatically install them for you.

It may be possible that older versions of NetworkX can work with the Hermes' current implementation. We leave the user the freedom to modify the version requirement in ``/Hermes/Makefile``. Nonetheless, future version of Hermes may invoke features of NetworkX that are only available in its latest release.

To visialize the output graphs, you may download `Gephi <https://gephi.org/>`_. You may also choose choose any visualization tool that supports GEXF (Graph Exchange XML Format).

--------------
Testing Hermes
--------------

To test Hermes, run::

	make test_hermes

This will do the following things:

1) Call ``/Hermes/test/test.py`` to create a random edge-list and a node-list under the directory ``/Hermes/test/data``.
2) Trigger command ``hermes`` to create the output, ``/Hermes/out.csv``, with all centrality measures and detected communities as node attributes.
3) Convert ``/Hermes/out.csv`` and ``/Hermes/test/data/edge-list.csv`` to ``out.gexf``.
