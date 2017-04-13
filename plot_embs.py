#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Plot w2v Embeddings
# A Abdelali Last Update: Tue Feb 21 22:47:43 AST 2017
# QCRI-2017

import os, sys
import re
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def load_emb(fname):

	vectors = []
	labels = []


	fin = open(fname, 'rb')

	for line in fin:
		if(len(re.split("\s+", line))<5):
			continue
		vec = np.array(re.split("\s+", line.strip())[1:], dtype=np.float)
		labels.append(re.split("\s+", line.strip())[0])
		vectors.append(vec)

	fin.close()
	
	return np.array(vectors), np.array(labels )
 
def main(filename):


	print("Processing: "+filename)

	vec,lab = load_emb(filename)

	model = TSNE(n_components=2, random_state=0)

	# t-SNE projection 
	Xfit = model.fit_transform(vec)
	
	#xmax, ymax = Xfit.max(axis=0)
	xmax = 300
	ymax = 300
	plt.axis([-xmax, xmax, -ymax, ymax])

	# Regexp for English vs Arabic 
	eng_regexp = re.compile(r'[A-Za-z]')

	for i in range(Xfit.shape[0]):
		(x1,y1) = 10*Xfit[i]
	
		if i < min(600,Xfit.shape[0]):
			#print("View"+lab[i].decode('utf-8'))
			if(eng_regexp.search(lab[i].decode('utf-8'))):
				cl = 'bs'
			else:
				cl = 'ro'
			#print("View: "+lab[i].decode('utf-8')+" : "+cl)
			plt.plot(x1,y1,cl)	
			plt.annotate(lab[i].decode('utf-8'), (x1+5,y1+5), xytext=(x1+5, y1+5)) 

	plt.grid(True)
	plt.show()

if __name__ == '__main__':

	# parse user input
	if(len(sys.argv)!=2):
		print("Usage: "+sys.argv[0]+" filename\n\t filename: word2vec embeddings\n\n")
	else:
		main(sys.argv[1])

