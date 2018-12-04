#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

def read_words(word_list):
	words = []
	with open(word_list, 'r') as word_list:
		for word in word_list.readlines():
			words.append(word.lower().strip())
	return words

def interchange(word):
	return reduce(lambda x,y: x+y, map(lambda x,y: x if y%2 == 0 else x.upper(), word, range(len(word))))

def swap_letter_number(word):
	temp = word.replace('l','1').replace('e','3').replace('a','4').replace('s','5').replace('o','0')
	return temp.replace('L','1').replace('E','3').replace('A','4').replace('S','5').replace('O','0')

def first_mix(words):
	mix = []
	for word in words:
		temp =[]
		temp.append(word)
		temp.append(word.upper())
		temp.append(word.capitalize())
		temp.append(interchange(word))
		temp.append(interchange(word).swapcase())
		mix.append(temp)
	
	for lst in mix:
		lst.extend(map(lambda x: swap_letter_number(x), lst))
		
	return mix

if __name__ == '__main__':
	words = read_words(argv[1])
	mix = first_mix(words)
	print mix
	