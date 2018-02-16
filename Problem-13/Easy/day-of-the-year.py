# python 3
# day-of-the-year.py 				# tells which day of the year is it

days_1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def tell_day(day, month, leap):
	count = day
	if leap == 1:
		if month>1:
			for i in range(0, month-1):
				count += days_2[i]
				print(count)
	elif leap == 0:
		if month>1:
			for i in range(0, month-1):
				count += days_1[i]
				print(count)
	return count

def main():
	print("Enter 1 for January, 2 for Feb ... 12 for December")
	leap = int(input("Is leap year(1 for yes, 0 for no): "))
	month = int(input("Enter month index: "))
	day = int(input("Enter day: "))
	print(tell_day(day, month, leap))

if __name__ == '__main__':
	main()