# python 3
# 99-bottles.py - Writes lyrics of 99 Bottles of beer

def main():
	beerBottles = 99
	while beerBottles != 0:
		print(str(beerBottles) + " bottles of beer on the wall, " + str(beerBottles) + " bottles of beer.")
		beerBottles -= 1
		if beerBottles != 0:
			print("Take one down and pass it around, " + str(beerBottles) + " bottles of beer on the wall.")
		else:
			print("Take one down and pass it around, no more bottles of beer on the wall.")
	print("No more bottles of beer on the wall, no more  bottles of beer.")
	print("Go to the store and buy some more, 99 bottles of beer on the wall.")

if __name__ == "__main__":
	main()