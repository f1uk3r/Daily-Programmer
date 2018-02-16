# python 3
# is-valid-phone.py 		# checks weather given phone number is valid

import re

tester = re.compile(r'^\(?\d{3}?[)-.]?\s?\d{3}[-.]?\d{4}$')

def check(number, regex):
	if re.match(regex, number):
		print("Valid Number")
	else:
		print("Invalid Number")

def main():
	n = int(input("How many phone numbers to check: "))
	for i in range(n):
		number = str(input("Enter number: "))
		check(number, tester)

if __name__ == '__main__':
	main()