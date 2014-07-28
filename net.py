import numpy as np
import numpy.random as npr
from random import choice, randint
import uuid
import collections

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

import networkx as nx

class SandNet(object):
	"""
	Bak Tang Wiesenfeld self-organized criticality model for networks here
	Not to be confused with the sand-graph in the sand model, which _makes_ a graph _from_ the lattice
	here, there is no lattice, just the graph
	"""
	def __init__(self, corpus):
		self.corpus = corpus
		self.graph = nx.DiGraph()
		prevWord = None
		wordct = collections.Counter()
		for word in corpus:
			self.graph.add_node(word, sandval=randint(0, 25), word=word)
			if prevWord:
				self.graph.add_edge(prevWord, word)
			prevWord = word
		print "order: ", self.graph.order()
		print "size: ", self.graph.size()
		self.numAvalanches = 0

	def loop(self, steps=1):
		return [self.step() for i in xrange(steps)]

	def increase(self, chosenNode):
		"""
		Increase
		should be iterative, not recursive this time
		"""
		nodes = [chosenNode]
		words = ""
		while len(nodes) >= 1:
			currNode = nodes.pop()
			if type(currNode) == tuple:
				currData = self.graph.node[currNode[0]]
				currOutdegree = self.graph.out_degree(currNode[0])
			elif type(currNode) == str:
				currData = self.graph.node[currNode]
				currOutdegree = self.graph.out_degree(currNode)
			currData["sandval"] += 1
			if currData["sandval"] >= currOutdegree:
				self.numAvalanches += 1
				currData["sandval"] -= currOutdegree
				words = words + currData["word"] + " "
				for neighbor in self.graph.neighbors(currData["word"]):
					nodes.append(neighbor)
		return words

	def step(self):
		return self.increase(choice(self.graph.nodes(data=True)))

if __name__ == '__main__':
	with open("corpus.txt", "r") as corpusFile:
		corpus = corpusFile.read().split()
		net = SandNet(corpus=corpus)
		output = net.loop(steps=100)
		output = filter(lambda x: len(x) > 1, output)
		print output
