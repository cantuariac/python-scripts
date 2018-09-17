#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import string
import argparse
import random

def generate_string(lenth, charset, sd=None):
	random.seed(sd)
	return ''.join(random.choice(charset) for _ in range(lenth))

def generate(lenth=16, seed=None, 
			digits=True, lower=False,
			upper=False, punctuation=False, custom=''):
	charset = custom
	if digits: charset += string.digits
	if lower: charset += string.ascii_lowercase
	if upper: charset += string.ascii_uppercase
	if punctuation: charset += string.punctuation
	if len(charset)==0: charset = string.printable
	return ''.join(random.choice(charset) for _ in range(lenth))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
				description="""A simple script to generate random passwords""")
				
	parser.add_argument( "-n", "--lenth", default=16, type=int, dest="lenth",
									help="Lenth of the password to be generated")
					
	parser.add_argument( "-d", "--digits", action='store_true', dest='digits',
									help="Include \"0-9\" in the character set")
					
	parser.add_argument( "-l", "--lowercase", action='store_true', dest='lcase',
									help="Include \"a-z\" in the character set")
					
	parser.add_argument( "-u", "--uppercase", action='store_true', dest='ucase',
									help="Include \"A-Z\" in the character set")
									
	parser.add_argument( "-p", "--punctuation", action='store_true', dest='punctuation',
									help="Include punctuation symbols in the character set")
									
	parser.add_argument( "-c", "--custom", default="", dest="custom",
									help="Include custom characters in th character set")
					
	parser.add_argument( "-s", "--seed", default=None, dest="seed",
									help="Seed for random generation")
					

	args = parser.parse_args()
	
	charset = args.custom
	if args.digits: charset += string.digits
	if args.lcase: charset += string.ascii_lowercase
	if args.ucase: charset += string.ascii_uppercase
	if args.punctuation: charset += string.punctuation
	
	if len(charset)==0:
		charset = string.printable
	
	print(generate_string(args.lenth, charset, args.seed))
