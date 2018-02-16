from operator import mul
from functools import reduce

print ("Legend for type \n 1 for = \n 2 and 3 for less than equal to and < \n 4 and 5 for \ge and > \n 6 and 7 for both inclusive and both exclusive \n 8 and 9 for only second inclusive and only first inclusive")
parts = int(input("How many parts: "))
print ("This is a binomial distribution question with ")
n = int(input("n = "))
p = float(input("p = "))
q = 1-p
print ("q = 1 - p = " + str(q))
print ("where")
print ("P(X = x) = \\binom{n}{x} p^x q^{n-x}")

def ncr(n, x):
	x1 = min(x, n-x)
	if x1 == 0: return 1
	numer = reduce(mul, range(n, n-x, -1))
	denom = reduce(mul, range(1, x+1))
	return numer / denom

def binom1(n, x, p, q):
	return ncr(n, x) * p**x * q**(n-x)

def binom2(n, x, p, q):
	sum = 0
	while x > -1:
		sum += binom1(n, x, p, q)
		x -= 1
	return sum

def binom3(n, x, p, q):
	sum = 0
	x -= 1
	while x > -1:
		sum += binom1(n, x, p, q)
		x -= 1
	return sum

def binom4(n, x, p, q):
	sum = 0
	while x < n+1:
		sum += binom1(n, x, p, q)
		x += 1
	return sum

def binom5(n, x, p, q):
	sum = 0
	x += 1
	while x < n+1:
		sum += binom1(n, x, p, q)
		x += 1
	return sum

def binom6(n, x1, x2, p, q):
	sum = 0
	while x1 < x2 + 1:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return sum

def binom7(n, x1, x2, p, q):
	sum = 0
	x1 += 1
	while x1 < x2:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return sum

def binom8(n, x1, x2, p, q):
	sum = 0
	x1 += 1
	while x1 < x2 + 1:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return sum

def binom9(n, x1, x2, p, q):
	sum = 0
	while x1 < x2:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return sum
sec = 97
for i in range(parts):
	num = int(input("How many x: "))
	ty = int(input("Type of x:"))
	if num == 1:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		if ty == 1:
			ans = binom1(n, x, p, q)
			print ("P(X = x) = " + str(ans))
		elif ty == 2:
			ans = binom2(n, x, p, q)
			print ("P(X \le x) = " + str(ans))
		elif ty == 3:
			ans = binom3(n, x, p, q)
			print ("P(X < x) = " + str(ans))
		elif ty == 4:
			ans = binom4(n, x, p, q)
			print ("P(X \ge x) = " + str(ans))
		elif ty == 5:
			ans = binom5(n, x, p, q)
			print ("P(X > x) = " + str(ans))
		
	elif num == 2:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		x2 = int(input("x2 = "))
		sec += 1 
		if ty == 6:
			ans = binom6(n, x1, x2, p, q)
			print ("P(" + str(x1) + "\le X \le" + str(x2) + ") = " + str(ans))
		if ty == 7:
			ans = binom7(n, x1, x2, p, q)
			print ("P(" + str(x1) + "< X <" + str(x2) + ") = " + str(ans))
		if ty == 8:
			ans = binom8(n, x1, x2, p, q)
			print ("P(" + str(x1) + "< X \le" + str(x2) + ") = " + str(ans))
		if ty == 9:
			ans = binom9(n, x1, x2, p, q)
			print ("P(" + str(x1) + "\le X <" + str(x2) + ") = " + str(ans))
		