# python3
# morse-code.py - decode/code morse code

morseLegend = [
				["A", ".-"],
				["B", "-..."],
				["C", "-.-."],
				["D", "-.."],
				["E", "."],
				["F", "..-."],
				["G", "--."],
				["H", "...."],
				["I", ".."],
				["J", ".---"],
				["K", "-.-"],
				["L", ".-.."],
				["M", "--"],
				["N", "-."],
				["O", "---"],
				["P", ".--."],
				["Q", "--.-"],
				["R", ".-."],
				["S", "..."],
				["T", "-"],
				["U", "..-"],
				["V", "...-"],
				["W", ".--"],
				["X", "-..-"],
				["Y", "-.--"],
				["Z", "--.."],
				["1", ".----"],
				["2", "..---"],
				["3", "...--"],
				["4", "....-"],
				["5", "....."],
				["6", "-...."],
				["7", "--..."],
				["8", "---.."],
				["9", "----."],
				["0", "-----"],
				[" ", "/"]
]

def decodeMorse(text):
	for each in morseLegend:
		if each[1]==text:
			return each[0]

def encodeMorse(text):
	for each in morseLegend:
		if each[0]==text:
			return each[1]

def main():
	encodeOrDecode = int(input("Enter 1 to encode Morse Code or 2 to decode Morse Code: "))
	if encodeOrDecode == 1:
		code = list(map(str, input("Enter your code: ")))
		for every in code:
			print(encodeMorse(every), end="")
	elif encodeOrDecode == 2:
		code = list(map(str, input("Enter your code: ").split()))
		for every in code:
			print(decodeMorse(every), end="")
	print("")
	
if __name__ == "__main__":
	main()