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
	install_requires = ['networkx', 'python-louvain'],
	packages=['hermes', 'hermes.src'],
	scripts=['script/hermes']
)