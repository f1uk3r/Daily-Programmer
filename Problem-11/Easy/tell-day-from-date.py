# python 3
# tell-day-from-date.py 		#give arguments for date returns day of week
# The program should take three arguments. The first will be a day, 
# the second will be month, and the third will be year. Then, 
# your program should compute the day of the week that date will fall on.

import datetime
import calendar
import sys

def get_day(day, month, year):
	date = datetime.datetime(int(year), int(month), int(day))
	print(calendar.day_name[date.weekday()])

if __name__ == '__main__':
	get_day(sys.argv[1], sys.argv[2], sys.argv[3])