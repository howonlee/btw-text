import collections, re, operator, math, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
	with open(sys.argv[1], "r") as ex_out:
		words = ex_out.read()
		patt = re.compile('([^\s\w]|_)+')
		words = patt.sub('', words).lower()
		wordlist = words.split()
		ct = collections.Counter(wordlist)
		word_counts = np.array(map(operator.itemgetter(1), ct.most_common()))
		plt.hist(word_counts, log=True)
		plt.show()
