#!/usr/bin/env python3
#==============================================================================#
# Created Date: Monday, October 5th 2020, 8:56:27 pm                           #
# Author: Chirag Sachdev                                                       #
# LinkedIn: https://www.linkedin.com/in/chiragsachdev/                         #
# Github: https://github.com/chiragsachdev/                                    #
#==============================================================================#

from chirags_helpers import file_handling as handler
from chirags_helpers import text_processing as texter
from nltk.corpus import words

def check_palindrome(s):
	'''function to check if the given string is a palindrome

	:param s: str: input string
	:return (bool): returns boolean value if the string is a palindrome
	'''
	return (True if s == s[::-1] else False)

def find_palindromes(fname):
	'''function to find palindromes from a given file

	:param fname: str: path to file
	:returns (list:str): list of palindromes found in the file
	'''

	text = handler.load_file(fname)
	text = texter.tokenize(text)
	palindromes = []
	for word in text:
		if (check_palindrome(word)):
			palindromes.append(word)
	
	return (palindromes)

def find_palingrams(text):
	'''function to generate 2 word palindromes from a given dictionary list

	:param fname: list:str: list of words
	:returns (list:str): list of palingrams generated in the file
	'''

	palingrams = []
	for word in text:
		if (check_palindrome(word)):
			continue
		stack = [word[0]]
		for i in range(1, len(word) - 1):
			stack.append(word[i])
			if (check_palindrome(word[i:])):
				word2 = ''.join(stack)[::-1]
				if word2 in text:
					palingrams.append((word, word2))
					break
	
	return (palingrams)

def main():
	fname = input('Enter path of dictionary file or press enter to use the default dictionary: ')
	if len(fname) > 0:
		text = handler.load_file(fname)
		text = texter.tokenize(text)
	else:
		text = words.words()
	
	palingrams = find_palingrams(text)
	print(palingrams)
	exit(0)

if __name__=='__main__':
	main()
