from __future__ import print_function
from random import choice, randint, random
import collections, re, sys
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
		#self.wordct = collections.Counter(corpus)
		for word in corpus:
			self.graph.add_node(word, sandval=randint(0, 10), word=word)
			if prevWord:
				self.graph.add_edge(prevWord, word)
			prevWord = word
		print("order: ", self.graph.order(), file=sys.stderr)
		print("size: ", self.graph.size(), file=sys.stderr)
		self.numAvalanches = 0
		self.numNegAvalanches = 0

	def loop(self, steps=1):
		return [self.step() for i in xrange(steps)]

	def neg_loop(self, steps=1):
		return [self.neg_step() for i in xrange(steps)]

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
				currdegree = self.graph.out_degree(currNode[0])
			elif type(currNode) == str:
				currData = self.graph.node[currNode]
				currdegree = self.graph.out_degree(currNode)
			currData["sandval"] += 1
			words = words + currData["word"] + " "
			if currData["sandval"] >= currdegree:
				self.numAvalanches += 1
				currData["sandval"] -= currdegree
				for neighbor in self.graph.neighbors(currData["word"]):
					if random() > 0.05: #dissipation chance
						nodes.append(neighbor)
			#probability of reduction
		return words

	def decrease(self, chosenNode):
		nodes = [chosenNode]
		words = ""
		while len(nodes) >= 1:
			currNode = nodes.pop()
			if type(currNode) == tuple:
				currData = self.graph.node[currNode[0]]
				currdegree = self.graph.out_degree(currNode[0])
			elif type(currNode) == str:
				currData = self.graph.node[currNode]
				currdegree = self.graph.out_degree(currNode)
			currData["sandval"] -= 1
			if currData["sandval"] < 0:
				words = words + currData["word"] + " "
				self.numNegAvalanches += 1
				currData["sandval"] += currdegree
				for neighbor in self.graph.neighbors(currData["word"]):
					if random() > 0.05: #dissipation chance
						nodes.append(neighbor)
		return words

	def step(self):
		return self.increase(choice(self.corpus))

	def neg_step(self):
		return self.decrease(choice(self.corpus))

if __name__ == '__main__':
	with open("corpus.txt", "r") as corpusFile:
		corpus = corpusFile.read().split()
		net = SandNet(corpus=corpus)
		for i in xrange(10):
			output = net.loop(steps=5000)
			neg_output = net.neg_loop(steps=1000)
		output = filter(lambda x: len(x) > 100, output)
		neg_output = filter(lambda x: len(x) > 100, neg_output)
		# 50 will take out nearly everything, is basically the hope
		for gened_text in output:
			print(gened_text)
			#print(gened_negtext)
