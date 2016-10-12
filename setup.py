#!/usr/bin/env python

from setuptools import setup

setup(
	name='hermes',
	version='0.1',
	data_file = [('hermes', ['*.cfg'])],
	description='',
	author='Yi Tian Xu',
	author_email='yi.t.xu@mail.mcgill.ca',
	url='https://github.com/ytixu/ns-project-2016',
	install_requires = ['networkx>=1.11', 'python-louvain>=0.5'],
	packages=['hermes', 'hermes.src'],
	scripts=['script/hermes']
)