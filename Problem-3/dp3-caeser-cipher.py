def translateMessage(do, message, key):
	if do == "d":
		key = -key
	transMessage = ""

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord("Z"):
					num -= 26
				elif num < ord("A"):
					num += 26
			if symbol.islower():
				if num > ord("z"):
					num -= 26
				elif num < ord("a"):
					num += 26
			transMessage += chr(num)
		else:
			transMessage += symbol
	return transMessage


do = input("Do you want to (e)ncrypt or (d)ecrypt? ")
message = input("Type your message : ")
key = int(input("Enter a key number between -26 and 26: "))
translated = translateMessage(do, message, key)
print("Your translated message is : " + translated)

