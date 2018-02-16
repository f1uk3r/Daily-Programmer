import math

def a(x, y, xy, xx, n):
	return ((y * xx) - (x * xy)) / ((n * xx) - (x*x))

def b(x, y, xy, xx, n):
	return ((n * xy) - (x * y)) / ((n * xx) - (x*x))

def r(x, y, xy, xx, yy, n):
	return ((n * xy) - (x * y)) / math.sqrt(((n * xx) - (x*x)) * ((n * yy) - (y*y)))

option = int(input("Choose 1 for regression, 2 for correlation and 3 for both: "))
if option == 1:
	n = int(input("Enter value of n: "))
	x = int(input("Enter sum of x: "))
	y = int(input("Enter sum of y: "))
	xy = int(input("Enter sum of xy: "))
	xx = int(input("Enter sum of xx: "))
	print ("\\\\ \sum X =" + str(x) + ", \sum Y =" + str(y) + "\\\\ \sum XY =" + str(xy) + ", \sum XX =" + str(xx))
	print ("\\\\ \hat y = a + bx")
	a1 = a(x, y, xy, xx, n)
	print ("\\\\ a = \\frac{\sum Y * \sum XX-\sum X*\sum XY}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ a = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
	b1 = b(x, y, xy, xx, n)
	print ("\\\\ b = \\frac{n\sum XY -\sum X*\sum Y}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ b = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
	print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "x")

elif option == 2:
	n = int(input("Enter value of n: "))
	x = int(input("Enter sum of x: "))
	y = int(input("Enter sum of y: "))
	xy = int(input("Enter sum of xy: "))
	xx = int(input("Enter sum of xx: "))
	yy = int(input("Enter value of yy: "))
	r1 = r(x, y, xy, xx, yy, n)
	print ("\\\\ r = \\frac{n\sum XY -\sum X*\sum Y}{\sqrt{\left(n\sum X^2 -(\sum X)^2\\right)\left(n\sum Y^2 -(\sum Y)^2\\right)}}")
	print ("\\\\ r = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{ \sqrt{(" + str(n) + "*" + str(xx) + " - " + str(x) + "^2)(" + str(n) + "*" + str(yy) + " - " + str(y) + "^2)}} \\approx " + str(r1))

elif option ==3:
	n = int(input("Enter value of n: "))
	x = int(input("Enter sum of x: "))
	y = int(input("Enter sum of y: "))
	xy = int(input("Enter sum of xy: "))
	xx = int(input("Enter sum of xx: "))
	yy = int(input("Enter value of yy: "))
	print ("\\\\ \sum X =" + str(x) + ", \sum Y =" + str(y) + "\\\\ \sum XY =" + str(xy) + ", \sum XX =" + str(xx))
	print ("\\\\ \hat y = a + bx")
	a1 = a(x, y, xy, xx, n)
	print ("\\\\ a = \\frac{\sum Y * \sum XX-\sum X*\sum XY}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ a = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
	b1 = b(x, y, xy, xx, n)
	print ("\\\\ b = \\frac{n\sum XY -\sum X*\sum Y}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ b = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
	print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "x")
	r1 = r(x, y, xy, xx, yy, n)
	print ("\\\\ r = \\frac{n\sum XY -\sum X*\sum Y}{\sqrt{\left(n\sum X^2 -(\sum X)^2\\right)\left(n\sum Y^2 -(\sum Y)^2\\right)}}")
	print ("\\\\ r = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{ \sqrt{(" + str(n) + "*" + str(xx) + " - " + str(x) + "^2)(" + str(n) + "*" + str(yy) + " - " + str(y) + "^2)}} \\approx " + str(r1))
