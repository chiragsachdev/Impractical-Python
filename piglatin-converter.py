#!/usr/bin/env python3
#==============================================================================#
# Created Date: Monday, October 5th 2020, 9:35:19 pm                           #
# Author: Chirag Sachdev                                                       #
# LinkedIn: https://www.linkedin.com/in/chiragsachdev/                         #
# Github: https://github.com/chiragsachdev/                                    #
#==============================================================================#

import re

def convert(s):
	'''function to convert in input string into pig-latin
	if a word begins with a consonent, we move the consonent to the end of the word and add \'ay\' at the end. If the word begins with a vowel, then we add \'way\' at the end of the word.

	:param s: input string
	:returns (str):  string converted to pig latin
	'''

	s=s.lower()
	punctuations = ".,:;?!@#$%^&*()_[]\{\}|\\<>/`~\n"
	for ch in punctuations:
		s = s.replace(ch, ' ')
	pattern = r'^\s*|\s\s*'
	s = re.sub(pattern, ' ', s).strip()
	words = s.split()
	for i in range(len(words)):
		if (re.match(r'\b[aeiou][a-zA-Z]+\b|\b[aeiou]\b', words[i])):
			words[i] += 'way'
		elif (re.match(r'\b[a-zA-Z]+\b', words[i])):
			words[i] = words[i][1:] + words[i][0] +'ay'
	return (' '.join(words))
		
def main():
	while (1):
		s = input('Enter string and press enter to convert text\nEnter QQ/qq to exit: ')
		if s.upper() == 'QQ':
			break
		print(convert(s), '\n')
	print('Exiting...\n')
	exit(0)

if __name__=='__main__':
	main()