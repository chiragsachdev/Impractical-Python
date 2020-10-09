#!/usr/bin/env python3
#==============================================================================#
# Created Date: Sunday, October 4th 2020, 6:01:50 pm                           #
# Author: Chirag Sachdev                                                       #
# LinkedIn: https://www.linkedin.com/in/chiragsachdev/                         #
# Github: https://github.com/chiragsachdev/                                    #
#==============================================================================#

import sys

def load_file(fname):
	'''function to read data from a file
	:param fname (str): path to file
	:return (str): contents of the file as a string
	:raises exception(str): exception while file handling
	'''
	try:
		with open(fname,'r') as fp:
			data = fp.read()
			return (data)
	except Exception as e:
		print("Error opening file: \n{}".format(e), file=sys.stderr)
		print("Exiting", file=sys.stderr)
		exit(1)
		
def write_file(data, fname, mode='w'):
	'''function to write data to a file
	
	:param data (str): data to be written to the file
	:param fname (str): path to file
	:param mode (char) [w, a]: mode to open the file for writing (default: \'w\')
	:raises exception(str): exception while file handling
	'''
	try:
		with open(fname, mode) as fp:
			data = fp.write()
	except Exception as e:
		print("Error opening file: \n{}".format(e), file=sys.stderr)
		print("Exiting", file=sys.stderr)
		exit(1)
