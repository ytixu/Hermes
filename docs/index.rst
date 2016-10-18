.. hermes documentation master file, created by
   sphinx-quickstart on Mon Oct 10 18:30:52 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hermes 0.2
==========

Hermes is a command-line tool for network science. It provides the users the convenience for constructing and analyzing graphs from CSV files.

Supported analysis for version 0.2 are node centrality measures (degree, closeness, betweenness and eigenvector) and community detection using Louvain method.

Computed values from the analysis can be outputted with the graph in CSV format.

Hermes also offers the functionality to compile graphs stored in CSV files to GEXF format, ready to be displayed on network visualization tools such as `Gephi <https://gephi.org/>`_.

Hermes is based on `NetworkX <https://networkx.github.io/>`_ and `python-louvain <http://perso.crans.org/aynaud/communities/>`_.

--------
Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   command_line_interface
   custom_configurations


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
