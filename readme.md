Bak-Tang-Wiesenfeld text generation
===

It seemed to me that the BTW abelian sandpile model is to the BTW abelian sandpile graph as Ising models are to Markov models. So what would be the analogy to Markov chains? I thought about it, and made something as simple and dumb as possible. It puts out some super interesting results, I felt. Is it discernable from a Markov chain, per se, statistically or whatever? I don't know.

Now, what are these BTW models? [Here is some information](http://en.wikipedia.org/wiki/Abelian_sandpile_model). Now, these are not strictly like the ones that Wikipedia describes: instead of having a lattice where each square has four neighbors, we construe this thing as a directed graph where each node has the neighbors that are the out-directed neighbors of the node. So the reduction-by-4 step is a reduction-by-outdegree step.

The nodes here are the words, and the directed edges are the simplest thing I could think of, which is that every word has a directed edge to the next word.

Run by running `python net.py` inside the directory of the repo.

Some example output. It seems a little more lucid to me than Markov Chain output, but this may be a delusion of mine.

>of." "Goddess," answered Medon, "whether overheard Mercury, giver guide "Messenger "or "Mercury, Eurynome, "Bring "all Melanthius, "the names mouth Penelope; "if boldly, Eurymachus, "we used Nestor, Chromius, "now knight Noemon, "what kind before. Later Theoclymenus, Menelaus, "is "Sir, "then Euryclea. "There Ulysses. Agelaus shouted Antinous. Meanwhile Eurynome threw vast themselves perfectly well, eat bread wasted baskets mash well, useless, able clear cold comfort fire; sky spring water." willed surrounded. busily several errands. thousands skins lovely Hebe dress Polycaste, Nestor's youngest dresses Philoetius handed slipped quietly Arete brought ambrosia about. Or If, moreover, cuts While Did Their messenger, corn lands Of these, course, wrapped undisturbed. planted brains out; meat disgrace hither "It rests ultimately "Are "Sir," "First observe sorrowfully, 'My friends, mend Mentor "My sons," child, mother," friend, child," friends," friend," replied Euryalus, "go Ulysses; "she Vulcan, lame "ask Telemachus; Antinous, "by "Have Eumaeus; dear,"  
