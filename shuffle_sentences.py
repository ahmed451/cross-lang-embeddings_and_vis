#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reshuffle words per line
# A Abdelali Last Update: Fri Apr 13 17:49:40 AST 2017
# QCRI-2017

import os, sys
import re
import random


Splitter=re.compile(r'(\s+|[a-z]+|\S+)')

def main():
	for line  in sys.stdin:

		wlist = Splitter.findall(line.strip().lower().replace(' +',' ').replace('\t',' '));
		random.shuffle(wlist)
		print('<s>'),
		print(' '.join(wlist)),
		print(" </s>")
	return

if __name__ == '__main__':
	main()
