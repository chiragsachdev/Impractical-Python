#!/usr/bin/env python3
#==============================================================================#
# Created Date: Monday, October 5th 2020, 6:56:11 pm                           #
# Author: Chirag Sachdev                                                       #
# LinkedIn: https://www.linkedin.com/in/chiragsachdev/                         #
# Github: https://github.com/chiragsachdev/                                    #
#==============================================================================#

import json
import sys 

def load_json(fname):
	'''function to read data from a json file
	:param fname (str): path to file
	:return (str): contents of the file as a string
	:raises exception(str): exception while file handling
	'''
	try:
		with open(fname,'r') as fp:
			data = json.load(fp)
			return (data)
	except Exception as e:
		print("Error opening file: \n{}".format(e), file=sys.stderr)
		print("Exiting", file=sys.stderr)
		exit(1)

def write_json(data, fname, mode='w'):
	'''function to write json data to a file

	:param data (str): data to be written to the file
	:param fname (str): path to file
	:param mode (char) [w, a]: mode to open the file for writing (default: \'w\')
	:raises exception(str): exception while file handling
	'''
	try:
		with open(fname, mode) as fp:
			json.dump(data, fp, ensure_ascii=False, indent=4)
	except Exception as e:
		print("Error opening file: \n{}".format(e), file=sys.stderr)
		print("Exiting", file=sys.stderr)
		exit(1)
