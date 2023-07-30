"""
File: boggle.py
Name:Ray
----------------------------------------
make a boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	find all the words on the board
	"""
	start = time.time()
	ans = []
	letters = {}
	dictionary = read_dictionary()
	if not user_input(letters):
		return
	for x in range(4):
		for y in range(4):
			word = letters[(x, y)]
			searching(x, y, word, letters, dictionary, ans, [(x, y)])
	print('There are', len(ans), 'words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def searching(x, y, word, letters, dictionary, ans, used_location):
	if len(word) > 3:
		if word not in ans and word in dictionary:
			ans.append(word)
			print('Found:', word)
	for i in range(-1, 2):
		for j in range(-1, 2):
			new_x = x + i
			new_y = y + j
			# choose
			if (new_x, new_y) not in used_location:
				if -1 < new_x < 4 and -1 < new_y < 4:
					word += letters[(new_x, new_y)]
					used_location.append((new_x, new_y))
					# explore
					if has_prefix(word, dictionary):
						searching(new_x, new_y, word, letters, dictionary, ans, used_location)
					# un-choose
					used_location.pop()
					word = word[:len(word)-1]


def user_input(letters):
	for i in range(4):
		data = input(str(i + 1) + ' row of letters: ').lower().strip().split(' ')
		if len(data) != 4:
			print('Illegal input')
			return
		for ch in data:
			if len(ch) != 1:  # make only a letter
				print('Illegal input')
				return
		for j in range(4):
			letters[(i, j)] = data[j]
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = set()
	with open(FILE, 'r') as file:
		for line in file:
			line = line.strip()
			if 17 > len(line) > 3:
				dictionary.add(line)
	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param dictionary:
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
