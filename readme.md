Bak-Tang-Wiesenfeld text generation
===

It seemed to me that the BTW abelian sandpile model is to the BTW abelian sandpile graph as Ising models are to Markov models. So what would be the analogy to Markov chains? I thought about it, and made something as simple and dumb as possible. It puts out some super interesting results, I felt. Is it discernable from a Markov chain, per se, statistically or whatever? I don't know.

Now, what are these BTW models? [Here is some information](http://en.wikipedia.org/wiki/Abelian_sandpile_model). Now, these are not strictly like the ones that Wikipedia describes: instead of having a lattice where each square has four neighbors, we construe this thing as a directed graph where each node has the neighbors that are the out-directed neighbors of the node. So the reduction-by-4 step is a reduction-by-outdegree step.

The nodes here are the words, and the directed edges are the simplest thing I could think of, which is that every word has a directed edge to the next word.

Run by running `python net.py` inside the directory of the repo. You may have to try a couple of times, because the parameters are set so that the distribution of words is most Zipf-like.

If you want to change the corpus, you can change the `corpus.txt` to what you want. I had interesting results with a corpus of song lyrics and of poetry. Because of the nature of the model, there is a saturation of sorts when the corpus is actually too small to learn properly. So using a big goddamn corpus gives you good results: the checked in repo has the Odyssey but that's just because big files and git don't mix well.

Some example output is in `example_output.txt` and below. It seems a little more lucid to me than Markov Chain output.

>heaven first or dispersed the us, us- from us. hates you. will so will against was did would give on robbed him of me than with frustrate their alone vouchsafed Helen it me itself, grudged us visits me took never brings may itself; you when, however, therefore, and prosper be meant sent has above ground your the Ortygia, where ground? One I water it, me, his all to send had shall grant for fed drove in have grants this, me as put one direct our your me. you. vouchsafes us him help and 
