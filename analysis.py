import collections, re, operator, math, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "put in a text file as argument"
		sys.exit(1)
	with open(sys.argv[1], "r") as ex_out:
		words = ex_out.read()
		patt = re.compile('([^\s\w]|_)+')
		words = patt.sub('', words)
		wordlist = words.split()
		ct = collections.Counter(wordlist)
		#this is to obtain the log-log property
		#so it's not actually the log-log graph, but looks exactly like it
		word_counts = np.array(map(lambda x: math.log(x), map(operator.itemgetter(1), ct.most_common())))
		plt.hist(word_counts)
		plt.yscale('log')
		plt.show()
