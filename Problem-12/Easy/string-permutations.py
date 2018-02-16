# python 3
# string-permutation.py 			# take a string and returns all the permutation
# Write a small program that can take a string:  "hi!"
# and print all the possible permutations of the string:

from itertools import permutations
import sys

if __name__ == '__main__':
	if len(sys.argv) > 1:
		string_to_permutation = str(sys.argv[1])
	else:
		string_to_permutation = str(input("Enter a String: "))
	permutations = [''.join(p) for p in permutations(string_to_permutation)]
	for each in permutations:
		print(each)