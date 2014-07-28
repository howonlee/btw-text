import collections, re, operator, math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
	with open("example_output.txt", "r") as ex_out:
		words = ex_out.read()
		patt = re.compile('([^\s\w]|_)+')
		words = patt.sub('', words).lower()
		wordlist = words.split()
		ct = collections.Counter(wordlist)
		word_keys = map(operator.itemgetter(0), ct.most_common())
		word_counts = map(lambda x: math.log(x), map(operator.itemgetter(1), ct.most_common()))
		indexes = np.arange(len(word_keys))
		width = 0.7
		plt.bar(indexes, word_counts, width)
		plt.xticks(indexes + width * 0.5, word_keys)
		plt.show()
