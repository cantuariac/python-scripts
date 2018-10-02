#!/usr/bin/env python3
# -*- coding: utf-8 -*-s

import sys
import numpy as np
from scipy import ndimage

Ul = '▀'
UL = '█'
uL = '▄'
ul = ' '


class ASCImage(np.ndarray):
	def __new__(cls, shape):
		if type(shape) == tuple:
			obj = super(ASCImage, cls).__new__(cls, shape, np.uint8)
			obj.fill(0)
		elif type(shape) == np.ndarray:
			obj = super(ASCImage, cls).__new__(cls, shape.shape, np.uint8)
			np.copyto(obj, shape)
			#if len(obj.shape)==2:
			#	obj = np.uint8(obj/256*24+231)
		else:
			obj = None
		return obj
	
	def print(self):
		if len(self.shape) == 2:
			for i in range(0, len(self), 2):
				for j in range(0, len(self[i])):
					uc, lc = self[i:i+2, j]
					print(	'\033[48;2;%d;%d;%dm'%(uc, uc, uc),
							'\033[38;2;%d;%d;%dm'%(lc, lc, lc),
							uL, sep='', end='')
				print('\033[0m')
		elif len(self.shape) == 3:
			for i in range(0, len(self), 2):
				for j in range(0, len(self[i])):
					uc, lc = self[i:i+2, j]
					print(	'\033[48;2;%d;%d;%dm'%tuple(uc),
							'\033[38;2;%d;%d;%dm'%tuple(lc),
							uL, sep='', end='')
				print('\033[0m')
	
	def print2(self):
		if len(self.shape) == 2:
			for i in range(0, len(self), 2):
				for j in range(0, len(self[i])):
					uc, lc = self[i:i+2, j]
					print(	'\033[48;5;%dm'%(uc),
							'\033[38;5;%dm'%(lc),
							uL, sep='', end='')
				print('\033[0m')

def imread(filename):
	return ASCImage(ndimage.imread(filename))

def print_chars(a, b, m, s=''):
	for i in range(a, b):
		if not i%m:
			o=sys.stdout.write('\n')
		o=sys.stdout.write(chr(i))
		o=sys.stdout.write(s)
	o=sys.stdout.write('\n')

