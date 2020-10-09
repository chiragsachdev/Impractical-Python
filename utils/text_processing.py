import nltk
import re
import collections

def tokenize(data):
	'''function that returns list of tokens from the string passed as a parameter
	The input data is processed by converting to lowecase, removing extra tabs and spaces followed by seperating hypthenated words and removing punctuations  
	:param data (str): input string
	:return (list:str): list of tokens
	'''
	data = data.lower()
	punctuations = ".,:;\'\"?!@#$%^&*()_-[]\{\}|\\<>/`~\n"
	for ch in punctuations:
		data = data.replace(ch, ' ')
	pattern = r'^\s*|\s\s*'
	data = re.sub(pattern, ' ', data).strip()
	tokens = data.split(' ')
	return (tokens)

def remove_stopwords(tokens):
	'''function to remove stopwords from a list of tokens
	:param data (list:str): list of tokens
	:return (list:str): list of tokens
	'''
	stopwords = nltk.corpus.stopwords.words('english')
	filtered_data = [word for word in tokens if word not in stopwords]
	return (filtered_data)

def get_wordcount(tokens):
	'''function to count occurance of each tokens in a list of tokens
	:param data (list:str): list of tokens
	:return (dict:{str:int}): dictionary of tokens and their counts
	'''
	return(dict(collections.Counter(tokens)))

def get_encoding_vector(text, threshold = 0.9):
	'''function to generate encoding vector from input text which covers data from tokens making up to the theshold% of the data 

	:param text: str: input text
	:param threshold: float: decimal value of the % of the data to be covered
	:return (list: str): returns list of unique tokens compridsing of the threshold*100% of the data
	'''
	tokens = tokenize(text)
	tokens_filtered = remove_stopwords(tokens)
	counts = get_wordcount(tokens_filtered)
	counts_sorted = dict(sorted(counts.items(), key = lambda k: k[1], reverse = True))
	total_count = sum(counts_sorted.values())
	total = 0
	encoding = []
	for tok in counts_sorted:
		total += counts_sorted[tok]
		encoding.append(tok)
		if total/total_count >= threshold:
			break
	
	return (encoding)

def one_hot_encode(encoding, data):
	'''function to encode a list of strings into one hot encoded vectors based on the list/set of encoding provided

	:param encoding: list: str: list of strings of tokens making up the encoding
	:param data: list:str: data entered is in a list of strings
	:return (list: int): returns list of one hot encoded vectors
	'''

	vectors = []
	for item in data:
		item = tokenize(item)
		vector = {tok:0 for tok in encoding}
		for tok in item:
			try:
				vector[tok] += 1
			except:
				continue
		vectors.append(vector)

	return(vectors)

def count_vectorize(encoding, data):
	'''function to encode a list of strings into count vectors based on the list/set of encoding provided

	:param encoding: list: str: list of strings of tokens making up the encoding
	:param data: list:str: data entered is in a list of strings
	:return (list: int): returns list of count encoded vectors
	'''

	vectors = []
	for item in data:
		item = tokenize(item)
		item_counts = get_wordcount(item)
		vector = {tok:0 for tok in encoding}
		for tok in item:
			try:
				vector[tok] += item_counts[tok]
			except:
				continue
			vectors.append(vector)

	return(vectors)
