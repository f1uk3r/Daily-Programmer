# python3
# sort-sh8t.py  			# Sorts sh88

def sort_shit():
	sorted_shit = sorted(list(map(str, input("Enter space seperated intergers or alphabets: ").split())))
	
	for each in sorted_shit:
		print(each, end=" ")
	print("")
	
if __name__ == '__main__':
	sort_shit()