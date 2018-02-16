import math
parts = int(input("How many parts: "))
print ("This is a binomial distribution question with ")
n = int(input("n = "))
p = float(input("p = "))
q = 1-p
print ("q = 1 - p = " + str(q))

print ("This binomial distribution can be approximated as Normal distribution since")
print ("np > 5 and nq > 5")
mean = n * p
sd = math.sqrt(n * p * q)
print ("Since we know that")
print ("Mean (\mu) = np = " + str(mean))
print ("Standard (\sigma) = np = " + str(sd))

def z(x, mean, sd):
	return (x - mean) / sd

print ("Also")
print ("z_{ score } = \\frac{x-\mu}{\sigma}")
sec = 97
for i in range(parts):
	ty = int(input("How many x's: "))
	if ty == 1:
		x1 = float(input(chr(sec) + ") " + "x = "))
		print ("P(x < " + str(x1) + ")=?")
		print ("z = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
		z1 = z(x1, mean, sd)
		print ("z = " + str(z1))
		print ("This implies that")
		print ("P(x < " + str(x1) + ")= P(z < " + str(z1) + ")=")

	elif ty == 2:
		x1 = float(input(chr(sec) + ") " + "x1 = "))
		x2 = float(input("x2 = "))
		print ("P(" + str(x1) + " < x < " + str(x2) + ")=?")
		print ("\\\\ z_1 = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
		z1 = z(x1, mean, sd)
		print ("\\\\ z_1 = " + str(z1))

		print ("\\\\ z_2 = \\frac {" + str(x2) + "-" +  str(mean) +  "}{" + str(sd) + "}")
		z2 = z(x2, mean, sd)
		print ("\\\\ z_2 = " + str(z2))

		print ("This implies that")
		print ("P(" + str(x1) + " < x < " + str(x2) + ")= P(" + str(z1) + " < z < " + str(z2) + ")=")