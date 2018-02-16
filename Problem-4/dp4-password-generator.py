import string
import random

list1 = list(string.ascii_letters)
list2 = list1 + list(string.digits)
list3 = list(string.printable)

a = int(input("""
What type of password do you want?
Press 1 for only alphabets.
Press 2 for only digits and alphabets.
Press 3 for any printable.
"""))
if a == 1:
	finalList = list1
elif a == 2:
	finalList = list2
elif a==3:
	finalList = list3
else:
	raise IndexError("Choose from 1, 2 or 3.")

howMany = int(input("How many passwords do you want? "))
letters = int(input("How long do you want your password to be? "))

for i in range(howMany):
		passwordList = random.sample(finalList, letters)
		print(''.join(passwordList))