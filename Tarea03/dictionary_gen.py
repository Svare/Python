#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jesús Enrique Pacheco Franco
# 04/Diciembre/2018

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

def swap_letter_special(word):
	temp = word.replace('i','!').replace('o','*').replace('a','@')
	return temp.replace('I','!').replace('O','*').replace('A','@')

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
		if 'i' in lst[0] or 'o' in lst[0] or 'a' in lst[0]:
			lst.extend(map(lambda x: swap_letter_special(x), lst))
		
	return mix

def append_numbers(mix, num):
	choncha = []
	for item in mix:
		temp = []
		for string in item:
			temp.extend(map(lambda x,y: x+str(y), [string]*num, range(num)))
			#temp.extend(map(lambda x,y: str(y)+x, [string]*num, range(num))) # Descomentar para numeros antes de palabra
		choncha.append(temp)
	return choncha


if __name__ == '__main__':
	words = read_words(argv[1])
	mix = first_mix(words)
	choncha = append_numbers(mix, int(argv[2]))

	remix = map(lambda x,y: x + y, mix, choncha)

	with open(argv[3], 'w') as dictionary:
		for current_list in remix:
			for string in current_list:
				dictionary.write(string + '\n')

	special = ['.', '@', '_', '-', ',', ' ']
	
	with open(argv[3], 'a') as dictionary:
		for n in range(len(remix)):
			main_list = remix.pop()
			temp = reduce(lambda x,y: x+y, remix)
			for x in main_list:
				for y in special:
					for z in temp:
						dictionary.write((lambda x,y,z: x+y+z)(x,y,z) + '\n')
			remix.insert(0,main_list)